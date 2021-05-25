import os
import numpy as np
import pandas as pd
import streamlit as st
import os, sys
import seaborn as sns
import matplotlib.pyplot as plt
path = __file__
for i in range(2):
    path = os.path.dirname(path)
sys.path.append(path)

from utils.dashboard_tb import *

df = pd.read_csv('df_limpio.csv')
add_selectbox = st.sidebar.selectbox('Menu', options=['Técnicas', 'Distribución y clasificación de estrellas'])

# Add a slider to the sidebar:
if add_selectbox == 'Distribución y clasificación de estrellas':
    fig, ax = plt.subplots()
    sns.countplot(ax=ax, data=df, x='P_DETECTION')
    ax.set_xticklabels(labels=df['P_DETECTION'].unique(), rotation=90)
    st.pyplot(figure=fig)