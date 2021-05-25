import flask, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-x', '--X', type=int, help='Introduce el DNI del estudiante')
args = parser.parse_args()
if args.prueba == 8642:
    print('Iniciando conexión')
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    @app.route('/', methods=['GET'])
    def home():
        pass