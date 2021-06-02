import matplotlib.pyplot as plt
from astropy.timeseries import TimeSeries
import os, sys
import pandas as pd

def dataframe_astropy():
    data = TimeSeries.read('../documentation/kplr010666592-2013131215648_slc.fits', format='kepler.fits')
    kepler_df = data.to_pandas()
    return kepler_df, data

def cargar_df():    
    sep = os.sep
    df = pd.read_csv(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + sep + 'data' + sep + 'phl_exoplanet_catalog.csv')
    print(f'{df.shape[0]} filas y {df.shape[1]} columnas')
    return df