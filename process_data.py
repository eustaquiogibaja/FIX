import pandas as pd

# Leer el archivo de Excel
datos = pd.read_excel('hotel_bookings.csv')

# Realizar algún procesamiento de datos (ejemplo: calcular la suma de una columna)
suma_columna = datos['personas'].sum()

# Generar un informe en formato CSV
informe = pd.DataFrame({'Suma': [suma_columna]})
informe.to_csv('report.csv', index=False)

print(f"Informe generado: {suma_columna}")