import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('data.csv')

# Verificar los nombres reales de las columnas
print("Nombres de columnas en el archivo:")
print(df.columns.tolist())

# 1. CONVERSIÓN DE UNIDADES

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

df_celsius = df.copy()

# Identificar automáticamente las columnas de ciudades y fecha
ciudad_columns = []
fecha_col = None

for col in df.columns:
    if 'phoenix' in col.lower() or 'san diego' in col.lower() or 'toronto' in col.lower():
        ciudad_columns.append(col)
        # Aplicar conversión
        df_celsius[col] = df_celsius[col].apply(kelvin_to_celsius)
    elif 'date' in col.lower() or 'time' in col.lower():
        fecha_col = col

# Si no encontramos fecha_col, usar la primera columna que no sea de ciudad
if fecha_col is None:
    for col in df.columns:
        if col not in ciudad_columns:
            fecha_col = col
            break

print(f"Columna de fecha identificada: '{fecha_col}'")
print(f"Columnas de ciudades identificadas: {ciudad_columns}")

# 2. ANÁLISIS DE DATOS (PHOENIX)

# Identificar la columna de Phoenix
phoenix_col = None
for col in ciudad_columns:
    if 'phoenix' in col.lower():
        phoenix_col = col
        break

if phoenix_col is None and len(ciudad_columns) >= 2:
    # Asumir que Phoenix es la segunda columna si no la encontramos por nombre
    phoenix_col = ciudad_columns[1]

print(f"Usando columna para Phoenix: '{phoenix_col}'")

# Encontrar temperatura mínima y máxima
temp_min_idx = df_celsius[phoenix_col].idxmin()
temp_max_idx = df_celsius[phoenix_col].idxmax()

# Obtener las fechas y temperaturas usando la columna correcta
fecha_hora_min = df_celsius.loc[temp_min_idx, fecha_col]
temp_min = round(df_celsius.loc[temp_min_idx, phoenix_col], 2)

fecha_hora_max = df_celsius.loc[temp_max_idx, fecha_col]
temp_max = round(df_celsius.loc[temp_max_idx, phoenix_col], 2)

# Calcular temperatura promedio
temp_promedio = round(df_celsius[phoenix_col].mean(), 2)

# Imprimir resultados
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

print("\n Proceso completado exitosamente!")
