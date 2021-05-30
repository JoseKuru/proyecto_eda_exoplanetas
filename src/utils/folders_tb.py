import matplotlib.pyplot as plt
import os, sys

def guardar_visualizacion(nombre_archivo: str):
    ruta_reports = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    plt.savefig(ruta_reports + os.sep + 'reports' + os.sep + nombre_archivo)
    return ruta_reports

