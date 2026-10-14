import pandas as pd

def pregunta_01():
    """
    ¿Cuántos registros tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
    como un número entero.

    Ejemplo del formato de la respuesta:

        40
    """
    return numero_registros_tabla()
    
    raise NotImplementedError

def numero_registros_tabla():
    df = pd.read_csv('data/tbl0.tsv', sep='\t')
    
    suma_registros = len(df)
    
    return int(suma_registros)
