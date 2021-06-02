import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.series import Series
import seaborn as sns
import sys, os
import plotly.express as px
import astropy.timeseries as TimeSeries


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

def guardar_visualizacion(nombre_archivo: str):
    ruta_reports = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    plt.savefig(ruta_reports + os.sep + 'reports' + os.sep + nombre_archivo, bbox_inches="tight")
    return ruta_reports

def boxplot_radio(df):
    fig, ax = plt.subplots(ncols=2, figsize=(20,10))
    ax[0].set_title("Boxplot de la variable 'Radio'")
    ax[0].axhline(y=30)
    sns.boxplot(ax=ax[0], data=df, y='Radio')
    ax[1].set_title("Distribución de la variable 'Radio'")
    sns.violinplot(ax=ax[1], data=df, x='Radio')
    guardar_visualizacion('outliers.png')

def boxplot_distancia_estrella(df):
    fig, ax = plt.subplots(ncols=2, figsize=(20,10))
    ax[0].set_title("Boxplot de la variable 'Distancia_estrella'")
    sns.boxplot(ax=ax[0], data=df, y='Distancia_estrella')
    ax[1].set_title("Distribución de la variable ''Distancia_estrella''")
    sns.violinplot(ax=ax[1], data=df, x='Distancia_estrella')
    guardar_visualizacion('outliers2.png')

def histograma_metodos(df):
    fig, ax = plt.subplots()
    sns.countplot(data=df, y='Metodo_deteccion', order=df['Metodo_deteccion'].value_counts().sort_values(ascending=False).index)
    ax.set_xlabel('Métodos')
    ax.set_ylabel('Frecuencia')
    ax.set_xlim(0, 4000)
    mostrar_porcentaje(df, ax)
    guardar_visualizacion('Metodos.png')

def curva_luz(kepler_df, data):
    plt.plot(data.time.jd, kepler_df["sap_flux"], "k.", markersize=1)
    plt.xlabel('Tiempo')
    plt.ylabel('Intensidad lumínica')
    guardar_visualizacion('curva_luz.png')

def histograma_radio_distancia(df):
    fig, ax = plt.subplots(ncols=2, figsize=(18, 5))
    sns.histplot(ax=ax[0], data=df[df['Radio'] < 20], x='Radio', bins=bins_freedman(df['Radio']))
    ax[0].axvline(x= 1, c='green', label='La Tierra')
    ax[0].axvline(x= 11.21, c='purple', label='Júpiter')
    ax[0].legend()
    sns.histplot(ax=ax[1], data=df[df['Distancia_estrella'] < 1], x='Distancia_estrella', bins=bins_freedman(df[df['Distancia_estrella'] < 1]['Distancia_estrella']))
    ax[1].axvline(x= 1, c='green', label='La Tierra')
    ax[1].legend()
    guardar_visualizacion('histogramas.png')

def grafica_esi(df):
    graph = px.scatter(df.query("Indice_similitud_tierra > 0.75"), x="Distancia_estrella", 
    y='Radio', size="Radio_estrella",hover_name="Nombre", size_max=30, 
    color='Indice_similitud_tierra', title='Planetas potencialmente habitables')
    return graph

def heatmap(df):
    fig, ax = plt.subplots(figsize=(15,9))
    sns.heatmap(data=df.corr(), annot=True)
    guardar_visualizacion('Heatmap')

def pairplot(df):
    sns.pairplot(df, diag_kws={'bins': 5})
    guardar_visualizacion('pairplot.png')

def graficos_conclusiones(df):
    fig, ax = plt.subplots(ncols=2, figsize=(18, 5))
    sns.scatterplot(ax=ax[0], data=df, x='Ascension_recta', y='Declinacion')
    sns.histplot(ax=ax[1], data=df[df['Distancia_tierra'] < 2000], x='Distancia_tierra', bins=bins_freedman(df[df['Distancia_tierra'] < 2000]['Distancia_tierra']))
    guardar_visualizacion('conclusion.png')

def pie_chart():
    dict_tiempo = {'Elección tema': 2,
    'Data wrangling': 7,
    'Visualización': 4,
    'Api': 1,
    'BBDD': 1,
    'Streamlit': 1,
    'Presentación': 1
    }
    plt.pie(x=dict_tiempo.values(), labels=dict_tiempo.keys())
    plt.title('Tiempo invertido en cada proceso')
    guardar_visualizacion('tiempo.png')

def diagrama_gantt():
    df = pd.DataFrame([
        dict(Task="Elección tema", Start='2021-05-18', Finish='2021-05-20'),
        dict(Task="Data wrangling", Start='2021-05-22', Finish='2021-05-28'),
        dict(Task="Visualización", Start='2021-05-28', Finish='2021-06-02'),
        dict(Task="Api", Start='2021-05-29', Finish='2021-05-30'),
        dict(Task="BBDD", Start='2021-06-01', Finish='2021-06-02'),
        dict(Task="Streamlit", Start='2021-06-01', Finish='2021-06-02'),
        dict(Task="Presentación", Start='2021-06-02', Finish='2021-06-03')
    ])
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
    fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
    return fig