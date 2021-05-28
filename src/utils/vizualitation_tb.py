import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.series import Series
import seaborn as sns


def crear_boxplot(df: pd.DataFrame):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    newdf = df.select_dtypes(include=numerics)
    for colum in newdf.colum:
        fig, ax = plt.subplots()
        sns.boxplot(ax=ax, data=df[colum])
        ax.set_title(colum)
        return fig

def bins_freedman(serie: pd.Series):
    # Calcula el numero de bins de un histograma segun la regla de Freedman–Diaconis
    iqr = serie.quantile(0.75) - serie.quantile(0.25)
    numero_datos = serie.count()
    h = 2 * iqr / (numero_datos ** (1/3))
    numero_bins = (serie.max() - serie.min()) / h
    return int(numero_bins)

def outliers(df: pd.DataFrame):
    for column in df.columns:
        third_cuartil = df[column].quantile(0.75)
        first_cuartil = df[column].quantile(0.25)
        iqr = third_cuartil - first_cuartil
        maximo = third_cuartil + (iqr * 1.5)
        minimo = maximo = first_cuartil - (iqr * 1.5)
        df = df[(df[column] > maximo) | (df[column] < minimo)]
        crear_boxplot(df)