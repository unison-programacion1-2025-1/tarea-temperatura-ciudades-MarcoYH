import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Ver tipos de datos de las columnas
print(df.dtypes)

# Convertir la columna 'Datetime' a tipo datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])
# Establecer la columna 'Date' como índice del DataFrame
df.set_index('Datetime', inplace=True)

# TODO: Crear funcion para convertir de grados Kelvin a Celsius
def kelvin_to_celsius(kelvin):
    C=kelvin-273.15
    return C
    

# TODO: Copiar el DataFrame original y nombralo df_celsius...

df_celsius=df.copy()

# TODO: Convertir las temperaturas de cada ciudad de Kelvin a Celsius usando la funcion creada...
for ciudad in df_celsius.columns:
    df_celsius[ciudad]=df_celsius[ciudad].apply(kelvin_to_celsius)
# Analisis!

# TODO: Imprime que día y hora se registró la temperatura mínima en Phoenix con el siguiente mensaje: "El día con la temperatura mínima en Phoenix fue: {fecha}"
fecha_minima=df_celsius['Phoenix'].idxmin()
print(f"El día con la temperatura mínima en Phoenix fue: {fecha_minima}")
# TODO: Imprime la temperatura mínima en Phoenix con el siguiente mensaje: "La temperatura mínima registrada en Phoenix fue de: ", temperatura, " °C""
temperatura_minima = df_celsius['Phoenix'].min()
temperatura_minima = round(temperatura_minima, 2)
print(f"La temperatura mínima registrada en Phoenix fue de: {temperatura_minima} °C")
# TODO: Imprime que día y hora se registró la temperatura máxima en Phoenix con el siguiente mensaje: "El día con la temperatura máxima en Phoenix fue: {fecha}"
fecha_maxima=df_celsius["Phoenix"].idxmax()
print(f"El día con la temperatura máxima en Phoenix fue: {fecha_maxima}")
# TODO: Imprime la temperatura máxima en Phoenix con el siguiente mensaje: "La temperatura máxima registrada en Phoenix fue de: ", temperatura, " °C""
temperatura_max=df_celsius["Phoenix"].max()
print(f"La temperatura máxima registrada en Phoenix fue de: {temperatura_max:.2f} °C")
# TODO: Imprime la temperatura promedio en Phoenix durante el año 2016 con el siguiente mensaje: "La temperatura promedio durante 2016 en Phoenix fue de: ", temperatura, " °C""
promedio=df_celsius["Phoenix"].mean()
print(f"La temperatura promedio durante 2016 en Phoenix fue de: {promedio:.1f} °C")
# Graficar la temperatura de Phoenix durante el año 2016
plt.figure(figsize=(20, 10))
plt.scatter(df_celsius.index, df_celsius['Phoenix'], label='Phoenix')
plt.title('Temperatura en Phoenix durante 2016')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.savefig("temperatura_phoenix_2016.png")
plt.show()

# Exportar el DataFrame modificado a un nuevo archivo CSV
df_celsius.to_csv("temperatura_celsius.csv")
