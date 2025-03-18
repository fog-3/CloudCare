import plotly.graph_objects as go
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('../../ml/data/resumen_evolucion_Limpio.csv')
df = df.ffill()
#df = df.fillna(method='ffill')
#df.to_csv('c:/Users/alcaz/Git/CloudCare/ml/data/resumen_evolucion_limpioProp.csv', index=False)

# Convertir columnas a valores numéricos
for columna in df.columns:
    df[columna] = pd.to_numeric(df[columna], errors='coerce')


# Definir los rangos normales para cada columna
rangos_normales = {
    'PresionSistolica': (90, 140, "mmHg"),               # mmHg , "hipertensión", "hipotensión"
    'PresionDiastolica': (60, 90, "mmHg"),               # mmHg , "hipertensión", "hipotensión"
    'FrecuenciaCardiaca': (60, 100, "lpm"),               # lpm , "bradicardia", "taquicardia"
    'Temperatura': (36.5, 39.2, "°C"),                     # °C , "hipotermia", "fiebre alta"
    'SaturacionOxigeno': (89, 98, "%"),                       # % , "hipoxemia", "hipoxemia"
    'Glucosa': (70, 180, "mg/dL"),                     # mg/dL , "hipoglucemia", "hiperglucemia"
    'Leucocitos': (4000, 11000, "células/μL"),            # células/μL , "leucopenia", "leucocitosis"
    'Hemoglobina': (12, 16, "g/dL"),                           # g/dL (ajusta según sexo) , "anemia", "policitemia"
    'Plaquetas': (150000, 450000, "plaquetas/μL"),  # plaquetas/μL , "trombocitopenia", "trombocitosis"
    'Colesterol': (0, 200, "mg/dL"),                # mg/dL , "hipocolesterolemia", "hipercolesterolemia"
    'HDL': (40, 60, "mg/dL"),                             # mg/dL , "variaciones", "variaciones"
    'LDL': (0, 130, "mg/dL"),                           # mg/dL
    'Trigliceridos': (0, 150, "mg/dL"),                 # mg/dL
    'Sodio': (135, 145, "mmol/L"),                      # mmol/L
    'Potasio': (3.5, 5.1, "mmol/L"),                    # mmol/L
    'Cloro': (98, 107, "mmol/L"),                       # mmol/L
    'Creatinina': (0.6, 1.2, "mg/dL"),                  # mg/dL
    'Urea': (7, 20, "mg/dL"),                           # mg/dL
    'AST': (10, 40, "U/L"),                             # U/L
    'ALT': (7, 56, "U/L"),                              # U/L
    'Bilirrubina': (0.1, 1.2, "mg/dL"),                 # mg/dL
    'pH': (7.35, 7.45, "pH"),                           # pH
    'pCO2': (35, 45, "mmHg"),                           # mmHg
    'pO2': (75, 100, "mmHg"),                           # mmHg
    'HCO3': (22, 28, "mmol/L"),                         # mmol/L
    'Lactato': (0.5, 2.2, "mmol/L")                     # mmol/L
}

rangos_normales_extendidos = {
    'PresionSistolica': (70, 180),       # mmHg (más amplio para incluir hipotensión e hipertensión severa)
    'PresionDiastolica': (40, 110),      # mmHg (más amplio para incluir hipotensión e hipertensión severa)
    'FrecuenciaCardiaca': (50, 120),     # lpm (más amplio para incluir bradicardia y taquicardia)
    'Temperatura': (35.0, 40.0),         # °C (más amplio para incluir hipotermia y fiebre alta)
    'SaturacionOxigeno': (85, 100),      # % (más amplio para incluir hipoxemia)
    'Glucosa': (50, 250),                # mg/dL (más amplio para incluir hipoglucemia e hiperglucemia)
    'Leucocitos': (3000, 15000),         # células/μL (más amplio para incluir leucopenia y leucocitosis)
    'Hemoglobina': (10, 18),             # g/dL (más amplio para incluir anemia y policitemia)
    'Plaquetas': (100000, 500000),       # plaquetas/μL (más amplio para incluir trombocitopenia y trombocitosis)
    'Colesterol': (0, 250),              # mg/dL (más amplio para incluir hipercolesterolemia)
    'HDL': (30, 70),                     # mg/dL (más amplio para incluir variaciones)
    'LDL': (0, 160),                     # mg/dL (más amplio para incluir hiperlipidemia)
    'Trigliceridos': (0, 200),           # mg/dL (más amplio para incluir hipertrigliceridemia)
    'Sodio': (130, 150),                 # mmol/L (más amplio para incluir hiponatremia e hipernatremia)
    'Potasio': (3.0, 5.5),               # mmol/L (más amplio para incluir hipokalemia e hiperkalemia)
    'Cloro': (95, 110),                  # mmol/L (más amplio para incluir hipocloremia e hipercloremia)
    'Creatinina': (0.5, 2.0),            # mg/dL (más amplio para incluir insuficiencia renal)
    'Urea': (5, 30),                     # mg/dL (más amplio para incluir insuficiencia renal)
    'AST': (10, 100),                    # U/L (más amplio para incluir daño hepático)
    'ALT': (7, 100),                     # U/L (más amplio para incluir daño hepático)
    'Bilirrubina': (0.1, 2.0),           # mg/dL (más amplio para incluir ictericia)
    'pH': (7.20, 7.50),                  # pH (más amplio para incluir acidosis y alcalosis)
    'pCO2': (30, 50),                    # mmHg (más amplio para incluir hipocapnia e hipercapnia)
    'pO2': (60, 120),                    # mmHg (más amplio para incluir hipoxemia)
    'HCO3': (18, 32),                    # mmol/L (más amplio para incluir desequilibrios ácido-base)
    'Lactato': (0.5, 4.0)                # mmol/L (más amplio para incluir acidosis láctica)
}

# Función para verificar los valores
def verificar_rangos(df, rangos):
    resultados = {}
    for columna, (minimo, maximo, medida) in rangos.items():
        if columna in df.columns:
            valores_fuera_rango = df[(df[columna] < minimo) | (df[columna] > maximo)]
            if not valores_fuera_rango.empty:
                resultados[columna] = valores_fuera_rango[['PacienteID', 'Fecha', 'Hora', columna]]
    return resultados

# Verificar los rangos
valores_fuera_rango = verificar_rangos(df, rangos_normales)

# Mostrar resultados
# if valores_fuera_rango:
#     print("Valores fuera de los rangos normales:")
#     for columna, datos in valores_fuera_rango.items():
#         print(f"/nColumna: {columna}")
#         print(datos)
# else:
#     print("Todos los valores están dentro de los rangos normales.")

def graficar_funcion(min, max, valor, medida, titulo):
    interval = max - min
    if ((valor < min) | (valor > max)): 
            marker_style = dict(color='#233825', size=10, symbol="x", line=dict(color="black", width=2))
            if (valor < min) :
                yaxis_aux = dict(title=medida, range=[valor - interval, max + interval])
            else :
                yaxis_aux = dict(title=medida, range=[min - interval * (1/2), valor + interval])
    else:
            marker_style = dict(color='#233825', size=10, symbol="circle", line=dict(color="black", width=2))
            yaxis_aux = dict(title=medida, range=[min - interval * (1/2), max + interval])
    
    # Crear la figura
    fig = go.Figure()

    # Añadir la banda de rango normal
    fig.add_trace(go.Scatter(
        x=[None], y=[None],  # No se dibuja nada, solo para la leyenda
        mode="lines",
        line=dict(width=0),
        fill="toself",
        fillcolor="rgba(135, 206, 235, 0.3)",
        name=f"Rango normal ({min} - {max})"
    ))

    # Añadir la banda de rango normal (usando shapes)
    fig.add_shape(
        type="rect",
        x0=-1, y0=min, x1=1, y1=max,
        fillcolor="rgba (216, 243, 220, 0.5)",
        line=dict(width=0),
    )

    # Añadir el punto
    fig.add_trace(go.Scatter(
        x=[0], y=[valor],
        mode="markers",
        marker=marker_style,
        name="Valor actual",
        hovertemplate="Valor: %{y} <extra></extra>",  # Texto al hacer hover
    ))

    # Añadir la línea vertical al hacer hover
    fig.update_layout(
        hovermode="x",  # Muestra la línea vertical al hacer hover
        hoverlabel=dict(
            bgcolor="white",
            font_size=12
        ),
        # Añade esto para una línea más visible:
        xaxis=dict(
            showspikes=True,        # Activar línea de hover
            spikethickness=1,       # Grosor de la línea
            spikecolor="black",       # Color
            spikedash="solid",        # Estilo: solid, dot, dash
        ),
        yaxis=yaxis_aux,
        title=titulo,
        plot_bgcolor= '#edf6f9',  # Fondo del área del gráfico
        paper_bgcolor="lavender",              # Fondo exterior
    )


    # Mostrar la gráfica
    fig.show()

def graficar_funciones(fila, rangos):
    for columna, (minimo, maximo, medida) in rangos.items():
        if  columna in fila.index:
            graficar_funcion(minimo, maximo, fila[columna], medida, columna)

graficar_funciones(df.iloc[1], rangos_normales)
