import openai # openai v1.0.0+
import os # Para leer las variables de entorno
from langchain_core.messages import HumanMessage

client = openai.OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL") # set proxy to base_url
)

# request sent to model set on litellm proxy, litellm --model

# Crear mensaje usando LangChain
pregunta = HumanMessage(content="Genera un resumen evolutivo para el paciente con diagnóstico de insuficiencia cardíaca.")

# Enviar mensaje al modelo usando OpenAI client
response = client.chat.completions.create(
    model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
    messages=[
        {"role": "system", "content": "Eres un asistente médico especializado en resúmenes clínicos."},
        {"role": "user", "content": pregunta.content}
    ]
)

# Imprimir respuesta del modelo
print(response.choices[0].message.content)