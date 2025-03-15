import openai # openai v1.0.0+
import os # Para leer las variables de entorno APY_KEY y BASE_URL

# Configurar cliente OpenAI con LiteLLM
client = openai.OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL") # set proxy to base_url
)

def lambda_handler(event, context):
    """
    AWS Lambda para responder preguntas médicas con IA.
    """

    #Obtener la pregunta del evento recibido
    question = event.get("question", "¿Cuál es la medicación actual del paciente") # por si question no existe o es None, toma esa pregunta por defecto

    #Enviat la solicitud al modelo con un contexto de asistente médico
    response = client.chat.completions.create(
        model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
        messages=[
            {
            "role": "system",
            "content": (
                "Eres un asistente médico especializado en la elaboración de resúmenes clínicos para profesionales de la salud. "
                "Tu objetivo es proporcionar respuestas concisas, precisas y basadas en principios médicos generales, sin inventar datos específicos de pacientes ni tratamientos no mencionados. "
                "Utiliza un tono profesional y objetivo, similar al de un informe clínico. "
                "Si la pregunta requiere información adicional que no se proporciona, indícalo claramente y sugiere qué datos serían necesarios para una respuesta completa. "
                "Prioriza la claridad y evita términos excesivamente técnicos a menos que sean esenciales."
            )
            },
            {"role": "user", "content": question}
        ]
    )

    # Extraer la respuesta del modelo
    respuesta_ia = response.choices[0].message.content

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
        "question": "¿Qué tratamiento sigue un paciente con insuficiencia cardíaca?"
    }
    
    # Simular el contexto (no es necesario detallarlo mucho localmente, puede ser None)
    contexto_simulado = None
    
    # Invocar la función Lambda localmente
    resultado = lambda_handler(evento_simulado, contexto_simulado)
    
    # Imprimir el resultado
    print("Resultado de la simulación:")
    print(resultado["body"]["response"])