import openai # openai v1.0.0+
import os # Para leer las variables de entorno APY_KEY y BASE_URL
from langchain_core.messages import HumanMessage

# Configurar cliente OpenAI con LiteLLM
client = openai.OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL") # set proxy to base_url
)

# Crear mensaje usando LangChain
pregunta = HumanMessage(content="Genera un resumen evolutivo para el paciente con diagnóstico de insuficiencia cardíaca.")

# Enviar mensaje al modelo usando OpenAI client
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
        {"role": "user", "content": pregunta.content}
    ]
)

# Imprimir respuesta del modelo
print(response.choices[0].message.content)