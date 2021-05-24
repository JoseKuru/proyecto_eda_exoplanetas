import flask, argparse

parser = argparse.ArgumentParser()
parser.add_argument('prueba', type=str, help='Introduce el DNI del estudiante')
args = parser.parse_args()
if args.prueba == 'B4907846':
    print('Iniciando conexión')
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    @app.route('/', methods=['GET'])
    def home():
        return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

    app.run()