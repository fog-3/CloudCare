import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('ml/data/resumen_evolucion_Limpio.csv')
df = df.ffill()
#df = df.fillna(method='ffill')
#df.to_csv('c:/Users/alcaz/Git/CloudCare/ml/data/resumen_evolucion_limpioProp.csv', index=False)

# Convertir columnas a valores numéricos
for columna in df.columns:
    if columna not in ['Fecha', 'Hora']:
        df[columna] = pd.to_numeric(df[columna], errors='coerce')

# Definir los rangos normales para cada columna
rangos_normales = {
    'PresionSistolica': (90, 140),       # mmHg
    'PresionDiastolica': (60, 90),       # mmHg
    'FrecuenciaCardiaca': (60, 100),     # lpm
    'Temperatura': (36.0, 39.2),         # °C
    'SaturacionOxigeno': (89, 98),       # %
    'Glucosa': (70, 180),                # mg/dL
    'Leucocitos': (4000, 11000),         # células/μL
    'Hemoglobina': (12, 16),             # g/dL (ajusta según sexo)
    'Plaquetas': (150000, 450000),       # plaquetas/μL
    'Colesterol': (0, 200),              # mg/dL
    'HDL': (40, 60),                     # mg/dL
    'LDL': (0, 130),                     # mg/dL
    'Trigliceridos': (0, 150),           # mg/dL
    'Sodio': (135, 145),                 # mmol/L
    'Potasio': (3.5, 5.1),               # mmol/L
    'Cloro': (98, 107),                  # mmol/L
    'Creatinina': (0.6, 1.2),            # mg/dL
    'Urea': (7, 20),                     # mg/dL
    'AST': (10, 40),                     # U/L
    'ALT': (7, 56),                      # U/L
    'Bilirrubina': (0.1, 1.2),           # mg/dL
    'pH': (7.35, 7.45),                  # pH
    'pCO2': (35, 45),                    # mmHg
    'pO2': (75, 100),                    # mmHg
    'HCO3': (22, 28),                    # mmol/L
    'Lactato': (0.5, 2.2)                # mmol/L
}

# Función para verificar los valores
def verificar_rangos(df, rangos):
    resultados = {}
    for columna, (minimo, maximo) in rangos.items():
        if columna in df.columns:
            valores_fuera_rango = df[(df[columna] < minimo) | (df[columna] > maximo)]
            if not valores_fuera_rango.empty:
                valores_fuera_rango['Diferencia'] = valores_fuera_rango[columna].apply(
                    lambda x: x - maximo if x > maximo else x - minimo
                )
                resultados[columna] = valores_fuera_rango[['PacienteID', 'Fecha', 'Hora', columna, 'Diferencia']]
    return resultados

# Verificar los rangos
valores_fuera_rango = verificar_rangos(df, rangos_normales)

# Mostrar resultados
if valores_fuera_rango:
    print("Valores fuera de los rangos normales:")
    for columna, datos in valores_fuera_rango.items():
        print(f"\nColumna: {columna}")
        print(datos)
else:
    print("Todos los valores están dentro de los rangos normales.")