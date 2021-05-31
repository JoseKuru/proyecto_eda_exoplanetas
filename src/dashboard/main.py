import os
import numpy as np
import pandas as pd
import streamlit as st
import os, sys, requests
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
path = __file__
for i in range(2):
    path = os.path.dirname(path)
sys.path.append(path)

from utils.dashboard_tb import *

add_selectbox = st.sidebar.selectbox('Menu', options=['Bienvenida', 'Distribución y clasificación de estrellas', 'Flask'])

# Add a slider to the sidebar:
if add_selectbox == 'Distribución y clasificación de estrellas':
    df = pd.read_csv(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + os.sep + 'data' + os.sep + 'phl_exoplanet_catalog_cleaned.csv')
    st.plotly_chart(px.scatter(df.query("Indice_similitud_tierra > 0.75"), x="Distancia_estrella", y='Distancia_tierra', size="Radio_estrella",hover_name="Nombre", size_max=30, color='Indice_similitud_tierra'))

if add_selectbox == 'Flask':
    dataframe()
