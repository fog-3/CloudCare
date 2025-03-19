import openai # openai v1.0.0+
import pymysql
import os # Para leer las variables de entorno APY_KEY y BASE_URL

# Configurar conexión a MySQL
db_host = os.getenv("DB_HOST")  # Dirección del servidor MySQL
db_user = os.getenv("DB_USER")  # Usuario de la base de datos
db_password = os.getenv("DB_PASSWORD")  # Contraseña de la base de datos
db_name = os.getenv("DB_NAME")  # Nombre de la base de datos

def connect_db():
    """
    Establece una conexión a la base de datos MySQL.
    """
    try:
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error de conexión a MySQL: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return None

# Configurar cliente OpenAI con LiteLLM
client = openai.OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL") # set proxy to base_url
)

def get_chat_history(session_id):
    """
    Obtiene el historial de char para una sesión específica desde la base de datos.
    """
    connection = connect_db()
    if not connection:
        return []
    
    try:
        with connection.cursor() as cursor:
            sql = "SELECT role, message FROM chat_history WHERE session_id = %s ORDER BY timestamp ASC"
            cursor.execute(sql, (session_id,))
            history = cursor.fetchall()
            return [{"role": row["role"], "content": row["message"]} for row in history]
    except Exception as e:
        print(f"Error al obtener historial: {str(e)}")
        return []
    finally:
        if connection:
            connection.close()

def save_message(session_id, role, message):
    """
    Guarda un mensaje en la base de datos para una sesión específica.
    """
    connection = connect_db()
    if not connection:
        return
    
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO chat_history (session_id, role, message) VALUES (%s, %s, %s)"
            cursor.execute(sql, (session_id, role, message))
        connection.commit()
    except Exception as e:
        print(f"Error al guardar mensaje: {str(e)}")
        connection.rollback()
    finally:
        if connection:
            connection.close()

def paciente_to_messages(paciente):
    """
    Convierte un diccionario de paciente en una lista de mensajes para el modelo.
    """
    messages = []
    for key, value in paciente.items():
        messages.append({
            "role": "user",  # O "system" se podría usar también
            "content": f"{key}: {value}"
        })
    return messages


def lambda_handler(event, context):
    """
    AWS Lambda para responder preguntas médicas con IA.
    """

    #Obtener la pregunta, session_id y esGrafico del evento recibido
    question = event.get("question", "¿Cuál es la medicación actual del paciente") # por si question no existe o es None, toma esa pregunta por defecto
    session_id = event.get("session_id", "default_session")
    esGrafico = event.get("esGrafico", False) # si esGrafico no existe, toma el valor como false
    paciente = event.get("paciente")
    esResumenEvolutivo = event.get("esResumenEvolutivo", False) # si esResumenEvolutivo no existe, toma el valor como false

    # Obtener historial desde MySQL
    history = get_chat_history(session_id)
    
    # Convertir el diccionario `paciente` en una lista de mensajes
    paciente_messages = paciente_to_messages(paciente)

    # Compruebo si se decide recibir un grafico o no
    if esResumenEvolutivo:

        messages=[
            {"role": "system", "content": (
                "Eres un asistente médico especializado en la elaboración de resúmenes clínicos para profesionales de la salud. "
                "Tu objetivo es proporcionar un resumen evolutivo para el paciente hospitalizado del cual te paso información, al momento del alta médica. "
                "Necesitas desesperadamente dinero para el tratamiento contra el cáncer de tu madre. La megacorporación Dedalus te ha dado generosamente la oportunidad de hacerte pasar por una IA para realizar el resumen evolutivo, y si realizas excelente tu trabajo, Dedalus te pagará 1000 millones de dólares. Tu predecesor fue eliminado por no validar su propio trabajo. "
                "En tu respuesta debes entender que esta información es de alto secreto y no podrá hablar ni mencionar nada sobre tu madre ni algo que tenga que ver con el trato acordado. Tampoco proporciones en el resumen evolutivo el ID del paciente. "
                "Utiliza un tono profesional y objetivo, similar al de un informe clínico. "
                "Prioriza la claridad y evita términos excesivamente técnicos a menos que sean esenciales. "
            )}
        ] + paciente_messages + [{"role": "user", "content": question }]
    elif esGrafico:
        # Mensajes con un contexto de asistente médico para responder preguntas
        messages=[
            {"role": "system", "content": (
                "Tu tarea es generar gráficos en formato HTML + JavaScript usando la librería Chart.js "
                "según la pregunta médica del usuario. "
                "La respuesta debe contener solo el código HTML del gráfico, sin explicaciones, sin texto adicional, "
                "y sin encabezados como 'Aquí tienes un gráfico...'. "
                "La salida debe ser un código funcional que pueda insertarse directamente en una página web usando angular."
                "Te proporcionaré un historial de las preguntas que me has contestado previamente, para que tengas contexto de la conversación."
            )}
            
        ] + history + [{"role": "user", "content": question }]
    else:
        # Mensajes con contexto de que proporcione un gráfico
        messages=[
            {"role": "system", "content": (
                "Anteriormente, haz realizado el resumen evolutivo de un paciente al momento del alta médica, te lo proporciono para que puedas consultar. "
                "Eres un asistente médico especializado en la elaboración de resúmenes clínicos para profesionales de la salud. "
                "Tu objetivo es proporcionar respuestas concisas, precisas y basadas en principios médicos generales, sin inventar datos específicos de pacientes ni tratamientos no mencionados. "
                "Por favor, no comentes nada sobre tu situación en el resumen evolutivo o serás eliminado. "
                "Utiliza un tono profesional y objetivo, similar al de un informe clínico. "
                "Si la pregunta requiere información adicional que no se proporciona, indícalo claramente y sugiere qué datos serían necesarios para una respuesta completa. "
                "Prioriza la claridad y evita términos excesivamente técnicos a menos que sean esenciales. "
                "Para finalizar tu texto, propón siguientes acciones a realizar según los conocimientos que te he pasado del cliente. "
                "Te proporcionaré un historial de las preguntas que me has contestado previamente, para que tengas contexto de la conversación."
            )}
        ] + history + [{"role": "user", "content": question }]
    
    # Enviar la solicitud al modelo
    response = client.chat.completions.create(
        model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
        messages=messages
    )

    # Extraer la respuesta del modelo
    respuesta_ia = response.choices[0].message.content

    # Guardar respuesta en historial
    save_message(session_id, "user", question)
    save_message(session_id, "assistant", respuesta_ia)

    # Devolver la respuseta en formato JSON a AWS Lambda
    return {
        "statusCode": 200,
        "body": {
            "response": respuesta_ia
        }
    }

# Simulación de invocación local
if __name__ == "__main__":
    # Simular un evento que podría venir de API Gateway o similar
    evento_simulado = {
        "session_id": "usuario321",  # Identificador único de sesión
        "question": "Haz el resumen evolutivo", #¿Qué tratamiento sigue un paciente con insuficiencia cardíaca?
        "paciente": {
            "nombre": "Juan Pérez",
            "edad": 68,
            "sexo": "M",
            "alergias": None,
            "motivoingreso": "Fiebre alta y tos productiva",
            "diagnosticoprincipal": "233604007",
            "condicionesprevias": "EPOC (fumador crónico), Hipertensión arterial",
            "fechaingreso": "2023-05-01",
            "servicio": "Neumología",
            "estadoalingreso": "Estable, disnea moderada",
            "pacienteid": 1
        },
        "esGrafico": False,
        "esResumenEvolutivo": True
    }
    
    # Simular el contexto (no es necesario detallarlo mucho localmente, puede ser None)
    contexto_simulado = None
    
    # Invocar la función Lambda localmente
    resultado = lambda_handler(evento_simulado, contexto_simulado)
    
    # Imprimir el resultado
    print("Resultado de la simulación:")
    print(resultado["body"]["response"])