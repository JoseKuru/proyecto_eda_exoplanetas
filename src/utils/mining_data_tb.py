import numpy as np
import pandas as pd


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
    grados_decimales = 0
    grados_horas_minutos = datos.split(' ')
    grados_decimales += int(grados_horas_minutos[0])
    grados_decimales += int(grados_horas_minutos[1])/60
    grados_decimales += float(grados_horas_minutos[2])/3600
    return grados_decimales
