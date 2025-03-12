# CloudCare

<p align="left">
<img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
</p>

## Índice:
- [CheckList](#checklist)
- [Descripción](#descripción)
- [Estructura de GitHub](#estructura-de-github)
- [Autores](#autores)
- [Tecnologias utilizadas](#tecnologias-utilizadas)

## CheckList

### Desarrollo del frontend

- Inicializar el proyecto de Angular ✅ 
- Crear la interfaz de usuario:
    - Diseñar un chat medico interactivo.
    - Implementar componentes para:
        - Mostrar respuestas textuales.
        - Visualizar gráficos y tablas (Chart.js o D3.js).
        - Sugerir acciones basadas en respuestas.
    - Integrar con la API backend.
- Implementar visualizaciones:
    - Gráficos de evolución de parámetros clínicos (ej: HbA1c, creatinina).
    - Tablas de medicación actual.
    - Alertas visuales para valores críticos.
- Mejorar la experiencia de usuario:
    - Destacar términos médicos clave.
    - Añadir botones de acción rápida (ej: "Ver guía completa", "Ajustar medicación").
    - Asegurar que la interfaz sea responsive y accesible.

### Configurar de AWS:
- Crear una cuenta de AWS.
- Configurar servicios clave:
    - AWS Bedrock (para modelos de IA).
    - Amazon S3 (para almacenar guías clínicas y datos).
    - AWS Lambda (para el backend).
    - Amazon DynamoDB (para gestión de contexto).
    - Amazon OpenSearch (para RAG). <--- Este hay que verlo, no estoy seguro  
- Configurar IAM roles y políticas de seguridad.
- Crear el diagrama de la estructura y de la base de datos.

### Desarrollo del backend y la IA  
- Crear API Gateway para manejar solicitudes.  
- Implementar funciones Lambda para:
    - Procesar preguntas médicas.
    - Gestionar el historial de conversaciones (DynamoDB).
    - Integrar AWS Bedrock para generar respuestas.
- Crear un dataset sintético de diálogos médicos (100+ ejemplos).
- Fine-tunar el modelo en AWS Bedrock (si es necesario).
- Implementar técnicas de prompt engineering:
    - Few-shot prompting con ejemplos médicos.
    - Chain-of-thought prompting para respuestas detalladas.
- Validar respuestas contra guías clínicas para evitar alucinaciones.
- Implementar gestión de contexto:
    - Guardar historial de conversaciones en DynamoBD.
    - Implementar memoria de contexto para preguntas encadenadas.
- Configurar caching:
    - Usar Redis para cachear respuestas frecuentes y reducir costos.

### Integración y pruebas
Ya veremos lo que hacemos aquí

## Descripción
Este proyecto tiene como objetivo desarrollar un asistente basado en inteligencia artificial que automatice la generación de resúmenes evolutivos para pacientes hospitalizados al momento del alta médica. El asistente está diseñado para reducir la carga administrativa del personal sanitario y mejorar la calidad y estandarización de los informes clínicos.

## Estructura de GitHub
Por ahora dispondremos las carpetas del proyecto tal que así:
```
medical-assistant/  
├── backend/  
│   ├── api/                  # API Gateway/Lambda  
│   ├── data_processing/      # Scripts de ETL  
│   └── prompts/              # Plantillas de prompts médicos  
├── frontend/  
│   ├── src/app/  
│   │   ├── chat/             # Componente de chat  
│   │   └── visualizations/   # Gráficos y tablas  
├── ml/  
│   ├── data/                 # Datos sintéticos  
│   ├── evaluation/           # Scripts de evaluación  
│   └── models/               # Config Bedrock  
├── docs/  
│   ├── architecture.md       # Diagrama de arquitectura  
│   └── presentation/         # Material para la presentación  
└── .github/  
    └── workflows/            # CI/CD para despliegue AWS  
````

### Flujo de Ramas: 
Estas ramas son las que me ha recomendado ChatGpt

1. `main` → Solo código estable.
2. `dev` → Integración diaria.
3. Ramas específicas:
    - `feat/medical-rag`
    - `feat/context-management`
    - `feat/visualizations`

## Autores

| [<img src="https://avatars.githubusercontent.com/u/147926495?s=400&u=c32592a471205ad1232e7f95aa0a8d687bb47b37&v=4" width=115><br><sub>Fernado Osuna Granados</sub>](https://github.com/fog-3) |  [<img src="https://avatars.githubusercontent.com/u/160588229?v=4" width=115><br><sub>Pablo Gámez Guerrero</sub>](https://github.com/Zemag17) |  [<img src="https://avatars.githubusercontent.com/u/182810285?v=4" width=115><br><sub>Hugo Macías Jiménez</sub>](https://github.com/hugooomaciias) |  [<img src="https://avatars.githubusercontent.com/u/124665173?v=4" width=115><br><sub>Jesús Alcázar Pérez</sub>](https://github.com/jesusAlcPer25) |
| :---: | :---: | :---: | :---: |

## Tecnologias utilizadas

![Angular](https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white)
![Python](https://img.shields.io/badge/python-ffde57?style=for-the-badge&logo=python&logoColor=4584b6)
![Amazonwebservices](https://img.shields.io/badge/AWS-20232A?style=for-the-badge&logo=amazonwebservices&logoColor=FF8000)
