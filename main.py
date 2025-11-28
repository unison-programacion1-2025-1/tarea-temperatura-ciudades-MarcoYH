import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('data.csv')

# Mostrar información del dataset para debugging
print("Información del dataset:")
print("Columnas:", df.columns.tolist())
print("Primeras filas:")
print(df.head())

# 1. CONVERSIÓN DE UNIDADES

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

df_celsius = df.copy()

# Intentar con diferentes nombres posibles para las columnas
nombres_fecha_posibles = ['Date Time', 'DateTime', 'date time', 'datetime', 'Date', 'date', 'Time', 'time']
nombres_phoenix_posibles = ['Phoenix', 'phoenix']

# Encontrar columna de fecha
fecha_col = None
for nombre in nombres_fecha_posibles:
    if nombre in df.columns:
        fecha_col = nombre
        break

# Encontrar columna de Phoenix
phoenix_col = None
for nombre in nombres_phoenix_posibles:
    if nombre in df.columns:
        phoenix_col = nombre
        break

# Si no encontramos, usar las columnas por posición
if fecha_col is None:
    fecha_col = df.columns[0]  # Primera columna
    
if phoenix_col is None:
    # Buscar columnas que contengan nombres de ciudades
    for col in df.columns:
        if col != fecha_col and ('san' in col.lower() or 'phoenix' in col.lower() or 'toronto' in col.lower()):
            if 'phoenix' in col.lower():
                phoenix_col = col
                break
    # Si aún no encontramos, usar la segunda columna
    if phoenix_col is None and len(df.columns) > 1:
        phoenix_col = df.columns[1]

print(f"Usando columna de fecha: '{fecha_col}'")
print(f"Usando columna de Phoenix: '{phoenix_col}'")

# Aplicar conversión a todas las columnas que parezcan ser temperaturas
for col in df.columns:
    if col != fecha_col:
        df_celsius[col] = df_celsius[col].apply(kelvin_to_celsius)

# 2. ANÁLISIS DE DATOS (PHOENIX)

temp_min_idx = df_celsius[phoenix_col].idxmin()
temp_max_idx = df_celsius[phoenix_col].idxmax()

fecha_hora_min = df_celsius.loc[temp_min_idx, fecha_col]
temp_min = round(df_celsius.loc[temp_min_idx, phoenix_col], 2)

fecha_hora_max = df_celsius.loc[temp_max_idx, fecha_col]
temp_max = round(df_celsius.loc[temp_max_idx, phoenix_col], 2)

temp_promedio = round(df_celsius[phoenix_col].mean(), 2)

print("¿Qué día y a que hora se registró la temperatura mínima en Phoenix durante 2016?")
print(f"El día con la temperatura mínima en Phoenix fue: {fecha_hora_min}")

print("¿Cuál fue la temperatura mínima registrada en Phoenix durante 2016?")
print(f"La temperatura mínima registrada en Phoenix fue de: {temp_min} °C")

print("¿Qué día y a que hora se registró la temperatura máxima en Phoenix durante 2016?")
print(f"El día con la temperatura máxima en Phoenix fue: {fecha_hora_max}")

print("¿Cuál fue la temperatura máxima registrada en Phoenix durante 2016?")
print(f"La temperatura máxima registrada en Phoenix fue de: {temp_max} °C")

print("⁠Temperatura promedio del año en Phoenix")
print(f"La temperatura promedio durante 2016 en Phoenix fue de: {temp_promedio} °C")

# 3. VISUALIZACIÓN
plt.figure(figsize=(12, 6))
plt.scatter(df_celsius.index, df_celsius[phoenix_col], alpha=0.6, s=10)
plt.title('Variación de Temperatura en Phoenix durante 2016')
plt.xlabel('Registro (tiempo)')
plt.ylabel('Temperatura (°C)')
plt.grid(True, alpha=0.3)
plt.savefig('temperatura_phoenix_2016.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. EXPORTACIÓN
df_celsius.to_csv('data_celsius.csv', index=False)

print("\n Proceso completado exitosamente")
