import flask
import pandas as pd
import os

def comprobacion_token():
    '''Comprueba que el token es correcto y, en ese caso, devuelve el dataframe
    de exoplanetas convertidos a json'''
    token = flask.request.args.get('tokenize_id')
    if token == 'B49078469':
        return pd.read_csv(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
                + os.sep + 'data' + os.sep + 'phl_exoplanet_catalog_cleaned.csv').to_json()
    return 'Token incorrecto'