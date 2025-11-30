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
df_celsius['San Diego'] = df_celsius['San Diego'].apply(kelvin_to_celsius)
df_celsius['Phoenix'] = df_celsius['Phoenix'].apply(kelvin_to_celsius)
df_celsius['Toronto'] = df_celsius['Toronto'].apply(kelvin_to_celsius)

# TODO 2: Análisis de Datos (Phoenix)
# Encontrar temperatura mínima y su fecha/hora
min_temp_idx = df_celsius['Phoenix'].idxmin()
min_temp_date = df_celsius.loc[min_temp_idx, 'Date Time']
min_temp_value = round(df_celsius.loc[min_temp_idx, 'Phoenix'], 2)

# Encontrar temperatura máxima y su fecha/hora
max_temp_idx = df_celsius['Phoenix'].idxmax()
max_temp_date = df_celsius.loc[max_temp_idx, 'Date Time']
max_temp_value = round(df_celsius.loc[max_temp_idx, 'Phoenix'], 2)

# Calcular temperatura promedio
avg_temp = round(df_celsius['Phoenix'].mean(), 2)

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
plt.scatter(df_celsius.index, df_celsius['Phoenix'], alpha=0.6, s=10)
plt.title('Variación de Temperatura en Phoenix durante 2016')
plt.xlabel('Registros (tiempo)')
plt.ylabel('Temperatura (°C)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('temperatura_phoenix_2016.png', dpi=300)
plt.close()

# TODO 4: Exportación
df_celsius.to_csv('data_celsius.csv', index=False)

print("\n Proceso completado exitosamente!")
print("Gráfico guardado como: temperatura_phoenix_2016.png")
print("Datos exportados como: data_celsius.csv")
