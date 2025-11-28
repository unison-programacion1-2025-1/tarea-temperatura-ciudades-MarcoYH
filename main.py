import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('data.csv')

# 1. CONVERSIÓN DE UNIDADES

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

df_celsius = df.copy()

# Aplicar conversión a las columnas de ciudades
ciudades = ['San Diego', 'Phoenix', 'Toronto']
for ciudad in ciudades:
    df_celsius[ciudad] = df_celsius[ciudad].apply(kelvin_to_celsius)

# 2. ANÁLISIS DE DATOS (PHOENIX)

# Encontrar temperatura mínima y máxima
temp_min_idx = df_celsius['Phoenix'].idxmin()
temp_max_idx = df_celsius['Phoenix'].idxmax()

# Obtener las fechas y temperaturas
fecha_hora_min = df_celsius.loc[temp_min_idx, 'Date Time']
temp_min = round(df_celsius.loc[temp_min_idx, 'Phoenix'], 2)

fecha_hora_max = df_celsius.loc[temp_max_idx, 'Date Time']
temp_max = round(df_celsius.loc[temp_max_idx, 'Phoenix'], 2)

# Calcular temperatura promedio
temp_promedio = round(df_celsius['Phoenix'].mean(), 2)

# TODO: Imprimir resultados en el formato EXACTO que esperan los tests
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

# Generar gráfico de dispersión
plt.figure(figsize=(12, 6))
plt.scatter(df_celsius.index, df_celsius['Phoenix'], alpha=0.6, s=10)
plt.title('Variación de Temperatura en Phoenix durante 2016')
plt.xlabel('Registro (tiempo)')
plt.ylabel('Temperatura (°C)')
plt.grid(True, alpha=0.3)

# Guardar la gráfica
plt.savefig('temperatura_phoenix_2016.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. EXPORTACIÓN

# Exportar DataFrame a CSV
df_celsius.to_csv('data_celsius.csv', index=False)

print("\n Proceso completado exitosamente!")
print(f" Gráfica guardada como: temperatura_phoenix_2016.png")
print(f" Datos exportados como: data_celsius.csv")
