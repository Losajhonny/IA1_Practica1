from flask import Flask, request, jsonify
from flask_cors import CORS
from Singleton import *
from Algoritmo import *
import time
import os

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
    Singleton.getInstance().nombre = data['nombre']

    #respuesta
    return jsonify({ 'status' : '200' })

@app.route('/generar', methods=['POST'])
def generar():
    #verificar entrada
    if len(Singleton.getInstance().entrada) == 0:
        return jsonify({ 'status' : '500' })
    else:
        #recuperar json
        data = request.json
        
        #cargar singleton
        Singleton.getInstance().criterioFin = int(data['fin'])
        Singleton.getInstance().criterioSeleccion = int(data['sel'])

        #obtener datos
        e = Singleton.getInstance().entrada
        cf = Singleton.getInstance().criterioFin
        cs = Singleton.getInstance().criterioSeleccion

        #ejecutar algoritmo
        algoritmo = Algoritmo()
        algoritmo.entrada = e
        algoritmo.criterioFin = cf
        algoritmo.criterioSel = cs
        algoritmo.ejecutar()

        #generar bitacora
        fecha = time.strftime("%x")
        hora  = time.strftime("%X")
        nombre = Singleton.getInstance().nombre
        criterioFin = Singleton.getInstance().getCriterioFin()
        criterioSel = Singleton.getInstance().getCriterioSel()
        generacion = Singleton.getInstance().generacion
        modelo = Singleton.getInstance().modelo

        mejorModelo = ""
        for w in range(len(modelo)):
            mejorModelo += " w" + str(w + 1) + ": " + str(modelo[w]) + ", "

        file = open("bitacora.txt", "a")
        file.write("#####################################################\n")
        file.write("Fecha: " + fecha + "\n")
        file.write("Hora: " + hora + "\n")
        file.write("Nombre: " + nombre + "\n")
        file.write("Criterio Finalizacion: " + criterioFin + "\n")
        file.write("Criterio Seleccion: " + criterioSel + "\n")
        file.write("No Generaciones: " + str(generacion) + "\n")
        file.write("Modelo: " + mejorModelo + "\n")
        file.write("#####################################################\n\n")
        file.close()

        return jsonify({ 'status' : '200' })

@app.route('/calcular', methods=['POST'])
def calcular():
    #recuperar json
    data = request.json

    #verificar entrada
    if len(Singleton.getInstance().modelo) == 0:
        return jsonify({ 'status' : '500', 'nota': 0.0 })
    else:
        modelo = Singleton.getInstance().modelo
        
        p1 = data['proyecto1']
        p2 = data['proyecto2']
        p3 = data['proyecto3']
        p4 = data['proyecto4']

        w1 = modelo[0]
        w2 = modelo[1]
        w3 = modelo[2]
        w4 = modelo[3]

        notaFinal = w1 * p1 + w2 * p2 + w3 * p3 + w4 * p4
        return jsonify({ 'status' : '200', 'nota':  notaFinal })

if __name__ == "__main__":
    app.run(debug=True)
