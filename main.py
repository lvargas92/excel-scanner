import pandas as pd

# Leer el archivo Excel y cargar los datos en un DataFrame
df = pd.read_excel('archivo_excel.xlsx')

# Obtener el tamaño máximo en caracteres de cada columna, ignorando NaN, NaT o None
tamanos_maximos = df.apply(lambda columna: columna.dropna().astype(str).str.len().max())

# Reemplazar NaN con 0 y convertir a entero
tamanos_maximos.fillna(0, inplace=True)
tamanos_maximos = tamanos_maximos.astype(int)

# Obtener el total de filas
total_filas = df.shape[0]

# Exportar la información a un archivo de texto con codificación UTF-8
with open('resultado.log', 'w', encoding='utf-8') as file:
    for columna, tamano_maximo in tamanos_maximos.items():
        file.write(f"Tamaño de la columna '{columna}': {tamano_maximo}\n")
    file.write(f"Total de filas en el archivo Excel: {total_filas}\n")
