import pandas as pd

def process_excel_column(file_path, sheet_name, column_name, data_type):
    # Cargando el archivo Excel
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    except FileNotFoundError:
        return "Error: No se encontró el archivo."
    except Exception as e:
        return f"Error: {str(e)}"

    # Verificando si la columna existe
    if column_name not in df.columns:
        return f"Error: La columna '{column_name}' no existe en la hoja '{sheet_name}'."

    # Procesando la columna
    errors = []
    for idx, value in enumerate(df[column_name], start=2):  # Comenzamos desde la segunda fila considerando la cabecera
        try:
            # Intentar convertir el valor al tipo de dato especificado
            converted_value = data_type(value)
        except (ValueError, TypeError):
            # Si no se puede convertir, mantener el valor original y agregar a la lista de errores
            errors.append((idx, value))

    # Escribiendo los resultados en un archivo de texto
    output_file = "errores.log"
    with open(output_file, "w") as f:
        for error in errors:
            f.write(f"Fila {error[0]}: {error[1]}\n")

    if errors:
        return f"Se encontraron errores en los datos. Los detalles se han guardado en '{output_file}'."
    else:
        return "No se encontraron errores en los datos."

# Ejemplo de uso
file_path = "sctr_sanitas.xlsx"  # Cambia esto al path de tu archivo Excel
sheet_name = "Afiliados"         # Cambia esto al nombre de tu hoja específica
column_name = "Remuneracion*"     # Cambia esto al nombre de la columna que quieres procesar
data_type = float            # Cambia esto al tipo de dato que deseas (int, float, datetime, etc)

print(process_excel_column(file_path, sheet_name, column_name, data_type))
