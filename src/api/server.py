import flask, argparse, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(__file__)
print(sys.path)
from utils.apis_tb import *

parser = argparse.ArgumentParser()
parser.add_argument('-x', '--X', type=int, help='Introduce el DNI del estudiante')
args = parser.parse_args()
if args.X == 8642:
    print('Iniciando conexión')
    app = flask.Flask(__name__)

    @app.route('/', methods=['GET'])
    def home():
        
        return comprobacion_token()

    app.run(host= '127.0.0.1', port=5000, debug=True)

else:
    print('Contraseña incorrecta')
