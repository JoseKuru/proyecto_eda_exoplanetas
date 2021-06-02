import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


def numero_nan(df : pd.DataFrame):
    '''
    Retorna el porcentaje de elementos NaN por cada columna
    '''
    return (df.isna().mean()) * 100

def columnas_porcentaje_nan(df: pd.DataFrame, porcentaje_minimo: int):
    '''
    Retorna una lista con las columnas con un porcentaje de valores NaN superiores
    al pasado por parametro
    '''
    lista_columnas = []
    for colum in df.columns:
        if df[colum].isna().mean() > porcentaje_minimo:
            lista_columnas.append(colum)
    return lista_columnas

def eliminar_columnas_nan(df: pd.DataFrame, porcentaje_minimo: int):
    '''
    Elimina las columnas con un porcentaje de NaN superiores al porcentaje pasado
    '''
    columnas = columnas_porcentaje_nan(df, porcentaje_minimo)
    for columna in columnas:
        del df[columna]
        print(f'Eliminada columna {columna}')

def convertir_a_grados_decimales(datos: str):
    '''
    Transforma datos en formato string '{grados} {horas} {minutos}' en grados decimales
    '''
    grados_decimales = 0
    grados_horas_minutos = datos.split(' ')
    grados_decimales += int(grados_horas_minutos[0])
    grados_decimales += int(grados_horas_minutos[1])/60
    grados_decimales += float(grados_horas_minutos[2])/3600
    return grados_decimales

def rellenar_nan(df: pd.DataFrame):
    # Creamos una instancia de la clase SimpleImputer que nos permitira cambiar los tipos NaN por el dato que queramos
    # En nuestro caso sera la mediana
    imp = SimpleImputer(missing_values = np.nan, strategy='median')
    # Como las primeras dos columnas de nuestro dataset son categoricas, no permiten el uso de la mediana, por eso transformaremos el resto de columnas y despues lo concatenaremos todo 
    transform = imp.fit_transform(df.iloc[:, 2:].values)
    df = pd.concat([df.iloc[:, :2], pd.DataFrame(transform, columns=df.columns[2:])], axis=1)
    return df
    
def modificar_columnas(df):
    columnas_escogidas = ['P_NAME', 'P_DETECTION', 'P_MASS', 'P_RADIUS_EST', 'P_PERIOD', 'P_ESI', 'P_GRAVITY', 'P_DENSITY', 'P_DISTANCE', 'S_DISTANCE', 'S_RADIUS_EST', 'S_TYPE', 'S_RA_H', 'S_DEC_T']
    df = df[columnas_escogidas]
    df.rename({'P_NAME': 'Nombre', 'P_DETECTION': 'Metodo_deteccion', 'P_MASS': 'Masa', 'P_RADIUS_EST': 'Radio', 'P_PERIOD': 'Periodo_orbital', 'P_ESI': 'Indice_similitud_tierra', 'P_GRAVITY': 'Gravedad', 'P_DENSITY': 'Densidad', 'P_DISTANCE': 'Distancia_estrella', 'S_DISTANCE': 'Distancia_tierra', 'S_RADIUS_EST': 'Radio_estrella', 'S_TYPE': 'Tipo_estrella', 'S_RA_H': 'Ascension_recta', 'S_DEC_T': 'Declinacion'}, axis=1, inplace=True)
    return df