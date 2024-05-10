import pandas as pd

# Ruta del archivo Excel
file_path = 'archivo_excel.xlsx'
sheet = 'Hoja1'

try:
    df = pd.read_excel(file_path, sheet_name=sheet)

    # Convertir la columna 'Remuneracion*' a tipo de datos de cadena (str)
    df['Remuneracion*'] = df['Remuneracion*'].astype(str)

    # Reemplazar comas con puntos en la columna 'Remuneracion*'
    df['Remuneracion*'] = df['Remuneracion*'].str.replace(',', '.')

    # Imprimir la columna 'Remuneracion*' para verificar si se ha reemplazado correctamente
    print(df['Remuneracion*'])

    # Convertir la columna Remuneracion* a tipo float
    df['FecNacimiento*'] = df['FecNacimiento*'].astype('datetime64[ns]')

    # Guardar las primeras 100 filas en un archivo CSV
    df.head(100).to_csv('primeras_100_filas.csv', index=False)
except ValueError as e:
    # Capturar el error de conversión
    print("Error de conversión encontrado:")
    print(e)

    # Obtener la posición de la celda con el error
    # Esto solo funciona si sabes cuál es la última operación que causó el error
    fila = int(str(e).split('occurred at index ')[1])
    columna = str(e).split('for ')[1].split(' ')[0]
    
    print("Posición de la celda con error:")
    print("Fila:", fila)
    print("Columna:", columna)
