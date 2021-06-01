import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.series import Series
import seaborn as sns


def crear_boxplot(df: pd.DataFrame):
    '''
    Función que crea un boxplot por cada columna numérica del dataframe
    '''
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    newdf = df.select_dtypes(include=numerics)
    for colum in newdf.colum:
        fig, ax = plt.subplots()
        sns.boxplot(ax=ax, data=df[colum])
        ax.set_title(colum)
        return fig

def bins_freedman(serie: pd.Series):
    '''
    Calcula el número de bins de un histograma segun la regla de Freedman–Diaconis
    '''
    iqr = serie.quantile(0.75) - serie.quantile(0.25)
    numero_datos = serie.count()
    h = 2 * iqr / (numero_datos ** (1/3))
    numero_bins = (serie.max() - serie.min()) / h
    return int(numero_bins)

def outliers(df: pd.DataFrame):
    '''
    Crea un boxplot con un dataframe que solo contiene los outliers del dataframe original
    '''
    for column in df.columns:
        third_cuartil = df[column].quantile(0.75)
        first_cuartil = df[column].quantile(0.25)
        iqr = third_cuartil - first_cuartil
        maximo = third_cuartil + (iqr * 1.5)
        minimo = maximo = first_cuartil - (iqr * 1.5)
        df = df[(df[column] > maximo) | (df[column] < minimo)]
        crear_boxplot(df)

def mostrar_porcentaje(df, ax):
    '''
    Muestra los porcentajes en un diagrama de barras
    '''
    length = df.shape[0]
    for p in ax.patches:
        percentage =f'{round((p.get_width()/length) * 100, 2)} %'
        width, height =p.get_width(),p.get_height()
        x=p.get_x()+width+0.02
        y=p.get_y()+height/2
        ax.annotate(percentage,(x,y))