import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('data.csv')

# TODO 1: Conversión de Unidades
def kelvin_to_celsius(kelvin):
    """
    Convierte temperatura de Kelvin a Celsius
    """
    return kelvin - 273.15

# Crear nuevo DataFrame con las temperaturas convertidas
df_celsius = df.copy()

# Identificar columnas automáticamente
# Buscar columnas que parezcan ser de temperatura (nombres de ciudades)
temperature_columns = []
date_column = None

for col in df.columns:
    col_lower = col.lower()
    # Buscar columnas de temperatura
    if any(city in col_lower for city in ['san diego', 'phoenix', 'toronto', 'temp']):
        temperature_columns.append(col)
        df_celsius[col] = df_celsius[col].apply(kelvin_to_celsius)
    # Buscar columna de fecha/hora
    elif any(time_keyword in col_lower for time_keyword in ['date', 'time', 'timestamp']):
        date_column = col

# Si no encontramos columna de fecha, usar el índice
if date_column is None:
    date_column = df.columns[0]  # Usar primera columna como fallback

# Asegurarnos de que Phoenix esté en las columnas de temperatura
phoenix_col = None
for col in temperature_columns:
    if 'phoenix' in col.lower():
        phoenix_col = col
        break

if phoenix_col is None:
    # Si no encontramos Phoenix, usar la segunda columna (asumiendo estructura)
    phoenix_col = df.columns[1] if len(df.columns) > 1 else df.columns[0]

# TODO 2: Análisis de Datos (Phoenix)
# Encontrar temperatura mínima y su fecha/hora
min_temp_idx = df_celsius[phoenix_col].idxmin()
min_temp_date = df_celsius.loc[min_temp_idx, date_column]
min_temp_value = round(df_celsius.loc[min_temp_idx, phoenix_col], 2)

# Encontrar temperatura máxima y su fecha/hora
max_temp_idx = df_celsius[phoenix_col].idxmax()
max_temp_date = df_celsius.loc[max_temp_idx, date_column]
max_temp_value = round(df_celsius.loc[max_temp_idx, phoenix_col], 2)

# Calcular temperatura promedio
avg_temp = round(df_celsius[phoenix_col].mean(), 2)

# Imprimir resultados
print(f"¿Qué día y a que hora se registró la temperatura mínima en Phoenix durante 2016?")
print(f"El día con la temperatura mínima en Phoenix fue: {min_temp_date}")

print(f"\n¿Cuál fue la temperatura mínima registrada en Phoenix durante 2016?")
print(f"La temperatura mínima registrada en Phoenix fue de: {min_temp_value} °C")

print(f"\n¿Qué día y a que hora se registró la temperatura máxima en Phoenix durante 2016?")
print(f"El día con la temperatura máxima en Phoenix fue: {max_temp_date}")

print(f"\n¿Cuál fue la temperatura máxima registrada en Phoenix durante 2016?")
print(f"La temperatura máxima registrada en Phoenix fue de: {max_temp_value} °C")

print(f"\n⁠Temperatura promedio del año en Phoenix")
print(f"La temperatura promedio durante 2016 en Phoenix fue de: {avg_temp} °C")

# TODO 3: Visualización
plt.figure(figsize=(12, 6))
plt.scatter(df_celsius.index, df_celsius[phoenix_col], alpha=0.6, s=10)
plt.title('Variación de Temperatura en Phoenix durante 2016')
plt.xlabel('Registros (tiempo)')
plt.ylabel('Temperatura (°C)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('temperatura_phoenix_2016.png', dpi=300)
plt.close()

# TODO 4: Exportación
df_celsius.to_csv('data_celsius.csv', index=False)

print("\nProceso completado exitosamente!")
print("Gráfico guardado como: temperatura_phoenix_2016.png")
print("Datos exportados como: data_celsius.csv")
