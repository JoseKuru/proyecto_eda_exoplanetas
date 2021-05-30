import flask, argparse, sys, os
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-x', '--X', type=int, help='Introduce el DNI del estudiante')
args = parser.parse_args()
if args.X == 8642:
    print('Iniciando conexión')
    app = flask.Flask(__name__)

    @app.route('/', methods=['GET'])
    def home():
        token = flask.request.args.get('tokenize_id')
        if token == 'B49078469':
            return pd.read_csv(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
                    + os.sep + 'data' + os.sep + 'phl_exoplanet_catalog_cleaned.csv').to_json()
        return 'Token incorrecto'

    app.run(host= '127.0.0.1', port=5000, debug=True)