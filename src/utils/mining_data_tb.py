import numpy as np
import pandas as pd


def numero_nan(df : pd.DataFrame):
    '''
    Retorna el numero de elementos NaN por cada columna
    '''
    return df.isna().sum()

def columnas_porcentaje_nan(df: pd.DataFrame, porcentaje_minimo: int):
    '''
    Retorna una lista con las columnas con un porcentaje de valores NaN superiores
    al pasado por parametro
    '''
    lista_columnas = []
    for colum in df.columns:
        if df[colum].isna().sum() / df.shape[0] > porcentaje_minimo:
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
