import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def crear_boxplot(df: pd.DataFrame):
    for colum in df.columns:
        sns.boxplot(df[colum])
