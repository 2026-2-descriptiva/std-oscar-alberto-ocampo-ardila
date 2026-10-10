def pregunta_01():
    
    import pandas as pd
    import numpy as np
    
    df = pd.read_csv('../data/data.csv.gz',compression='gzip')
    
    sum_value = df['value'].sum()
    
    print(sum_value)
    """
    Calcule la suma de los valores de la segunda columna (`value`) del
    archivo `data/data.csv.gz` y retorne el resultado como un número entero.

    Ejemplo del formato de la respuesta:

        214
    """
    raise NotImplementedError
