import numpy as np
import pandas as pd
import streamlit as st
import os
import plotly.express as px

def dataframe():
    '''Función que devuelve el json de exoplanetas a streamlit'''    
    st.write('Dataframe de exoplanetas')
    st.table(pd.read_json('http://localhost:5000/?tokenize_id=B49078469'))

def bienvenida():
    st.title('Proyecto EDA: Exoplanetas')
    st.write('En 2009 la NASA lanzó el telescopio Kepler, el mayor proyecto hasta la fecha para el descubrimiento de exoplanetas. Despues de 10 años, unos 4.000 planetas han sido confirmados, y una pregunta frecuente en la ciencia ficción empezo a tener sus primeras evidencias')
    st.write('¿Habra planetas con condiciones similares a la tierra para ser colonozidas?')

def grafico_ESI():
    df = pd.read_csv(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + os.sep + 'data' + os.sep + 'phl_exoplanet_catalog_cleaned.csv')
    fig = px.scatter(df.query("Indice_similitud_tierra > 0.75"), x="Distancia_estrella", y='Distancia_tierra', size="Radio_estrella",hover_name="Nombre", size_max=30, color='Indice_similitud_tierra', title='Planetas potencialmente habitables')
    st.plotly_chart(fig)