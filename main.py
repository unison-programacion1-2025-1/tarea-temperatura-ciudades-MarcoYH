import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('data.csv')

# 1. CONVERSIÓN DE UNIDADES

# TODO: Crear función kelvin_to_celsius
def kelvin_to_celsius(kelvin):
    """
    Convierte temperatura de Kelvin a Celsius
    
    Args:
        kelvin (float): Temperatura en grados Kelvin
    
    Returns:
        float: Temperatura en grados Celsius
    """
    return kelvin - 273.15

# TODO: Aplicar la función a las columnas de las ciudades
df_celsius = df.copy()
df_celsius['San Diego'] = df_celsius['San Diego'].apply(kelvin_to_celsius)
df_celsius['Phoenix'] = df_celsius['Phoenix'].apply(kelvin_to_celsius)
df_celsius['Toronto'] = df_celsius['Toronto'].apply(kelvin_to_celsius)

# 2. ANÁLISIS DE DATOS (PHOENIX)

# TODO: Encontrar temperatura mínima y máxima
temp_min_idx = df_celsius['Phoenix'].idxmin()
temp_max_idx = df_celsius['Phoenix'].idxmax()

fecha_hora_min = df_celsius.loc[temp_min_idx, 'Date Time']
temp_min = round(df_celsius.loc[temp_min_idx, 'Phoenix'], 2)

fecha_hora_max = df_celsius.loc[temp_max_idx, 'Date Time']
temp_max = round(df_celsius.loc[temp_max_idx, 'Phoenix'], 2)

# TODO: Calcular temperatura promedio
temp_promedio = round(df_celsius['Phoenix'].mean(), 2)

# TODO: Imprimir resultados
print(f"¿Qué día y a que hora se registró la temperatura mínima en Phoenix durante 2016?")
print(f"El día con la temperatura mínima en Phoenix fue: {fecha_hora_min}")

print(f"\n¿Cuál fue la temperatura mínima registrada en Phoenix durante 2016?")
print(f"La temperatura mínima registrada en Phoenix fue de: {temp_min} °C")

print(f"\n¿Qué día y a que hora se registró la temperatura máxima en Phoenix durante 2016?")
print(f"El día con la temperatura máxima en Phoenix fue: {fecha_hora_max}")

print(f"\n¿Cuál fue la temperatura máxima registrada en Phoenix durante 2016?")
print(f"La temperatura máxima registrada en Phoenix fue de: {temp_max} °C")

print(f"\n⁠Temperatura promedio del año en Phoenix")
print(f"La temperatura promedio durante 2016 en Phoenix fue de: {temp_promedio} °C")

# 3. VISUALIZACIÓN

# TODO: Generar gráfico de dispersión
plt.figure(figsize=(12, 6))
plt.scatter(df_celsius.index, df_celsius['Phoenix'], alpha=0.6, s=10)
plt.title('Variación de Temperatura en Phoenix durante 2016')
plt.xlabel('Registro (tiempo)')
plt.ylabel('Temperatura (°C)')
plt.grid(True, alpha=0.3)

# TODO: Guardar la gráfica
plt.savefig('temperatura_phoenix_2016.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. EXPORTACIÓN

# TODO: Exportar DataFrame a CSV
df_celsius.to_csv('data_celsius.csv', index=False)

print("\n Proceso completado exitosamente!")
print(f"Gráfica guardada como: temperatura_phoenix_2016.png")
print(f"Datos exportados como: data_celsius.csv")

