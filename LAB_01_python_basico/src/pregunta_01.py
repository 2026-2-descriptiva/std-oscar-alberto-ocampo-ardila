import csv
import gzip 

def leer_registros():
    """
    Lee el archivo `data/data.csv.gz` y retorna un generador de registros.
    Cada registro es un diccionario con las claves `id` y `value`.
    """
    with gzip.open('data/data.csv.gz', mode='rt') as archivo:
        return list(csv.reader(archivo, delimiter='\t'))

def pregunta_01():
    """
    Calcule la suma de los valores de la segunda columna (`value`) del
    archivo `data/data.csv.gz` y retorne el resultado como un número entero.

    Ejemplo del formato de la respuesta:

        214
    """
    
    registros = leer_registros()
    return sum(int(fila[1]) for fila in registros)

    raise NotImplementedError
