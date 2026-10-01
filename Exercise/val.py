import pandas as pd


def filas_con_campos_vacios(df):
    # Detecta celdas vacías (NaN o strings vacíos)
    vacio = df.isna() | (df == '')
    
    # Filtra las filas que tienen al menos un valor vacío
    filas_vacias = df[vacio.any(axis=1)]
    
    print(f"🔎 Se encontraron {len(filas_vacias)} filas con al menos un campo vacío.")
    return filas_vacias


def filas_con_mas_de_tres_vacios(df):
    # Detectar celdas vacías (NaN o strings vacíos)
    vacio = df.isna() | (df == '')
    
    # Contar cuántos campos vacíos hay en cada fila
    conteo_vacios = vacio.sum(axis=1)
    
    # Filtrar filas con más de 3 vacíos
    filas_filtradas = df[conteo_vacios > 3]
    
    print(f"🔎 Se encontraron {len(filas_filtradas)} filas con más de 3 campos vacíos.")
    return filas_filtradas

df = pd.read_csv("C:/Users/Pipicano/Downloads/COSTOS_20250630_36.csv", sep='|', dtype=str)

print(df)

# Llamar a la función
filas_vacias = filas_con_mas_de_tres_vacios(df)

# Mostrar las primeras 5 filas vacías (opcional)
print(filas_vacias.head())

