from flask import Flask, request, jsonify
from flask_cors import CORS
from Singleton import *
from Algoritmo import *

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return 'hola'

@app.route('/load', methods=['POST'])
def load():
    #recuperar json
    data = request.json

    #recuperar notas
    notas = data['notas']

    #nueva entrada
    entrada = []

    #recorrer notas
    for n in notas:
        nota = [n['proyecto1'], n['proyecto2'], n['proyecto3'], n['proyecto4'], n['final'], 0]
        entrada.append(nota)

    #guardar entrada
    Singleton.getInstance().entrada = entrada

    #respuesta
    return jsonify({'status': '200'})

@app.route('/generar', methods=['POST'])
def generar():
    #verificar entrada
    if len(Singleton.getInstance().entrada) == 0:
        return jsonify({'status': '500'})
    else:
        #recuperar json
        data = request.json
        
        #cargar singleton
        Singleton.getInstance().criterioFin = int(data['fin'])
        Singleton.getInstance().criterioSeleccion = int(data['sel'])

        #obtener datos
        tp = Singleton.getInstance().tamPoblacion
        e = Singleton.getInstance().entrada
        cf = Singleton.getInstance().criterioFin
        ef = Singleton.getInstance().entradaFin
        cs = Singleton.getInstance().criterioSeleccion
        es = Singleton.getInstance().entradaSeleccion

        #ejecutar algoritmo
        algoritmo = Algoritmo(tp, e, cf, ef, cs, es)
        algoritmo.ejecutar()

        return jsonify({'status': '200'})

@app.route('/calcular', methods=['POST'])
def calcular():
    return 'calcular'

if __name__ == "__main__":
    app.run(debug=True)
