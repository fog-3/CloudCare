<a id="top"></a>
# <img src="frontend/src/assets/images/CloudCare-logo-sin-letras-readme.png" alt="cc-icon" width="45" /> CloudCare

Proyecto realizado para la dathaton de 2025 organizada por Dedalus en Málaga junto a diferentes [organizadores](#entidades-colaboradoras-de-la-dathaton) más.

![Video demo Cloudcare](frontend/src/assets/Gif2_CloudCare.gif)


## Índice:
- [Descripción del reto a abordar](#descripción-del-reto-a-abordar)
- [Descripción de nuestra solución](#descripción-de-nuestra-solución)
- [Como Compilar el proyecto](#como-compilar-el-proyecto)
- [Estructura de GitHub](#estructura-de-github)
- [Autores](#autores)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Entidades colaboradoras de la dathaton](#entidades-colaboradoras-de-la-dathaton)


## Descripción del reto a abordar
### Reto 1:

Este proyecto tiene como objetivo desarrollar un asistente basado en inteligencia artificial que automatice la generación de resúmenes evolutivos para pacientes hospitalizados al momento del alta médica. El asistente está diseñado para reducir la carga administrativa del personal sanitario y mejorar la calidad y estandarización de los informes clínicos.

## Descripción de nuestra solución
Nuestro equipo decidión hacer una aplicación en la que tú como médico puedes buscar a un paciente y luego seleccionarlo puedes ver un historial de datos como por ejemplo la primera analítica de cuando ingresó, un historial de notas que ha hecho el médico, la razon por la que entró el paciente...

Tras esto, puedes seleccionar en el apartado lateral los datos de las anlíticas del paciente, las cuales están organizadas por fechas y horas. Esto te mostrará un panel con gráficos sobre los parámetros de las analíticas y si están entre los valores normales o no.

Como último tenemos y lo más importante el médico tiene la posibilidad de preguntarle a un ChatBot datos sobre el paciente, así como pedirle un resumen evolutivo del paciente, o incluso un gráfico con sus datos.

<p style="text-align: left;">
    <a href="#top">⬆️ volver arriba</a>
</p>

## Como compilar el proyecto


## Estructura de GitHub
Por ahora dispondremos las carpetas del proyecto tal que así:

```markdawn
CloudCare/  
├── backend/  
│   ├── api/                  # API Gateway/Lambda  
│   ├── data_processing/      # Scripts de ETL  
│   └── prompts/              # Plantillas de prompts médicos  
├── frontend/  
│   ├── src/app/  
│   │   ├── chat/             # Componente de chat  
│   │   └── visualizations/   # Gráficos y tablas  
├── ml/  
│   ├── data/                 # Datos sintéticos y copia de seguridad sql
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

![Angular](https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white) &nbsp;
![Python](https://img.shields.io/badge/python-ffde57?style=for-the-badge&logo=python&logoColor=4584b6) &nbsp;
![AWS Lambda](https://img.shields.io/badge/AWS_Lambda-20232A?style=for-the-badge&logo=awslambda&logoColor=FF8000) &nbsp;
![AWS Lambda](https://img.shields.io/badge/Amazon_API_Gateway-6e649e?style=for-the-badge&logo=amazonapigateway&logoColor=white) &nbsp;
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=00000) &nbsp;
![SpringBoot](https://img.shields.io/badge/Springboot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white) &nbsp;
![Maven](https://img.shields.io/badge/Maven-white?style=for-the-badge&logo=apachemaven&logoColor=C71A36) &nbsp;
![Html](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white) &nbsp;
![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css&logoColor=white) &nbsp;
![Html](https://img.shields.io/badge/TypeScript-white?style=for-the-badge&logo=typescript&logoColor=3178C6)


<p align="center">
<img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
</p>

## Entidades colaboradoras de la dathaton

<div align="center">
<img src="https://www.dedalushackathon.com/wp-content/uploads/2022/10/Logo-Dedalus_Fondo-Azul.png" alt="Logo-Dedalus_Fondo-Azul" width="140" /> &nbsp;&nbsp;&nbsp;
<img src="https://www.dedalushackathon.com/wp-content/uploads/2023/02/Logo-ETSII-Malaga.png" alt="Logo-ETSII-Malaga" width="150" /> &nbsp;&nbsp;&nbsp; <img src="https://www.dedalushackathon.com/wp-content/uploads/2023/02/Logo-ETSII-Sevilla.png" alt="Logo-ETSII-Sevilla" width="230" />
</div>
<br><br>

<div align="center">
<img src="https://www.dedalushackathon.com/wp-content/uploads/2023/02/logo-malaga-tech-park.png" alt="logo-malaga-tech-park" width="130" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://www.dedalushackathon.com/wp-content/uploads/2023/02/logo-aws.png" alt="logo-aws" width="100" />
</div>
<br><br>

Más información sobre la dathaton en este link: [Dathaton 2025 Malaga](https://www.dedalushackathon.com/datathon-andalucia).

<p style="text-align: left;">
    <a href="#top">⬆️ volver arriba</a>
</p>
