import openai
import os

client = openai.OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

def lambda_handler(event, context):
    """
    Lambda que solicita gráficos en formato LaTeX o HTML a OpenAI.
    """
    question = event.get("question", "Muestra un gráfico de barras de pacientes por edad")

    response = client.chat.completions.create(
        model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
        messages=[
            {"role": "system", "content": (
                "Tu tarea es generar gráficos en formato HTML + JavaScript usando la librería Chart.js "
                "según la pregunta médica del usuario. "
                "La respuesta debe contener solo el código HTML del gráfico, sin explicaciones, sin texto adicional, "
                "y sin encabezados como 'Aquí tienes un gráfico...'. "
                "La salida debe ser un código funcional que pueda insertarse directamente en una página web."
            )},
            {"role": "user", "content": question}
        ]
    )

    response_text = response.choices[0].message.content

    return {
        "statusCode": 200,
        "body": {
            "response": response_text
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