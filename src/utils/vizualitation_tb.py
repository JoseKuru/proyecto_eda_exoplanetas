import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.series import Series
import seaborn as sns


def crear_boxplot(df: pd.DataFrame):
    for colum in df.columns:
        sns.boxplot(df[colum])

def bins_freedman(serie: pd.Series):
    iqr = serie.quantile(0.75) - serie.quantile(0.25)
    print(iqr)
    numero_datos = serie.count()
    print(numero_datos)
    h = 2 * iqr / (numero_datos ** (1/3))
    print(h)
    numero_bins = (serie.max() - serie.min()) / h
    print(numero_bins)
    return int(numero_bins)