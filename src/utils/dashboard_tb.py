import numpy as np
import pandas as pd
import streamlit as st

def filtrar_estrella(df: pd.DataFrame):
    st.sidebar.selectbox('Filtra por el tipo de estrella', options=df.S_TYPE.unique().tolist())

def dataframe():    
    st.write('Dataframe de exoplanetas')
    st.table(pd.read_json('http://localhost:5000/?tokenize_id=B49078469'))
