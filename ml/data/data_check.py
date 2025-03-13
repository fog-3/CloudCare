import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('c:/Users/alcaz/Git/CloudCare/ml/data/resumen_evolucion_Limpio.csv')
df = df.ffill()
#df = df.fillna(method='ffill')
#df.to_csv('c:/Users/alcaz/Git/CloudCare/ml/data/resumen_evolucion_limpioProp.csv', index=False)

# Convertir columnas a valores numéricos
for columna in df.columns:
    df[columna] = pd.to_numeric(df[columna], errors='coerce')


# Definir los rangos normales para cada columna
rangos_normales = {
    'PresionSistolica': (90, 140),       # mmHg
    'PresionDiastolica': (60, 90),       # mmHg
    'FrecuenciaCardiaca': (60, 100),     # lpm
    'Temperatura': (36.5, 39.2),         # °C
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
    for columna, (minimo, maximo) in rangos.items():
        if columna in df.columns:
            valores_fuera_rango = df[(df[columna] < minimo) | (df[columna] > maximo)]
            if not valores_fuera_rango.empty:
                resultados[columna] = valores_fuera_rango[['PacienteID', 'Fecha', 'Hora', columna]]
    return resultados

# Verificar los rangos
valores_fuera_rango = verificar_rangos(df, rangos_normales)

# Mostrar resultados
if valores_fuera_rango:
    print("Valores fuera de los rangos normales:")
    for columna, datos in valores_fuera_rango.items():
        print(f"/nColumna: {columna}")
        print(datos)
else:
    print("Todos los valores están dentro de los rangos normales.")