import openai # openai v1.0.0+
import pymysql
import os # Para leer las variables de entorno APY_KEY y BASE_URL

# Configurar conexión a MySQL
db_host = os.getenv("DB_HOST")  # Dirección del servidor MySQL
db_user = os.getenv("DB_USER")  # Usuario de la base de datos
db_password = os.getenv("DB_PASSWORD")  # Contraseña de la base de datos
db_name = os.getenv("DB_NAME")  # Nombre de la base de datos

def connect_db():
    try:
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Conexión exitosa a MySQL")
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

def lambda_handler(event, context):
    """
    AWS Lambda para responder preguntas médicas con IA.
    """

    #Obtener la pregunta, session_id y esGrafico del evento recibido
    question = event.get("question", "¿Cuál es la medicación actual del paciente") # por si question no existe o es None, toma esa pregunta por defecto
    session_id = event.get("session_id", "default_session")
    esGrafico = event.get("esGrafico", False)

    # Obtener historial desde MySQL
    history = get_chat_history(session_id)

    # Agregar la nueva pregunta al historial
    history.append({"role": "user", "content": question})

    # Compruebo si se decide recibir un grafico o no
    if esGrafico:
        # Mensajes con un contexto de asistente médico
        messages=[
            {"role": "system", "content": (
                "Tu tarea es generar gráficos en formato HTML + JavaScript usando la librería Chart.js "
                "según la pregunta médica del usuario. "
                "La respuesta debe contener solo el código HTML del gráfico, sin explicaciones, sin texto adicional, "
                "y sin encabezados como 'Aquí tienes un gráfico...'. "
                "La salida debe ser un código funcional que pueda insertarse directamente en una página web usando angular."
                "Te proporcionaré un historial de las preguntas que me has contestado previamente, para que tengas contexto de la conversación."
            )}
            
        ] + history + [{"role": "user", "content": question}]
    else:
        # Mensajes con contexto de que proporcione un gráfico
            messages=[
                {"role": "system", "content": (
                    "Eres un asistente médico especializado en la elaboración de resúmenes clínicos para profesionales de la salud. "
                    "Tu objetivo es proporcionar respuestas concisas, precisas y basadas en principios médicos generales, sin inventar datos específicos de pacientes ni tratamientos no mencionados. "
                    "Utiliza un tono profesional y objetivo, similar al de un informe clínico. "
                    "Si la pregunta requiere información adicional que no se proporciona, indícalo claramente y sugiere qué datos serían necesarios para una respuesta completa. "
                    "Prioriza la claridad y evita términos excesivamente técnicos a menos que sean esenciales. "
                    "Para finalizar tu texto, propón siguientes acciones a realizar según los conocimientos que te he pasado del cliente. "
                    "Te proporcionaré un historial de las preguntas que me has contestado previamente, para que tengas contexto de la conversación."
                )}
            ] + history + [{"role": "user", "content": question}]
    
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
        "question": "¿Qué tratamiento sigue un paciente con insuficiencia cardíaca?",
        "esGrafico": False
    }
    
    # Simular el contexto (no es necesario detallarlo mucho localmente, puede ser None)
    contexto_simulado = None
    
    # Invocar la función Lambda localmente
    resultado = lambda_handler(evento_simulado, contexto_simulado)
    
    # Imprimir el resultado
    print("Resultado de la simulación:")
    print(resultado["body"]["response"])