from flask import render_template, request, redirect, url_for
from src import app
from src.models.enlaces import EnlacesModel
import webbrowser
from werkzeug.exceptions import abort
import random  # Para importar la biblioteca random al completo
from random import randrange, choice # Para importar sólo determinadas funciones (randrange y choice)

@app.route('/')
def acortador():
    return render_template('enlaces/acortador.html', enlaces=enlaces)

@app.route('/enlaces')
def enlaces():
    enlacesModel = EnlacesModel()
    enlaces = enlacesModel.traerTodos()
    return render_template('enlaces/vista_enlaces.html', enlaces=enlaces)

@app.route('/enlaces/crear', methods=['GET', 'POST'])
def crear_enlaces():
    if request.method == 'GET':       
        return render_template('enlaces/acortador.html')# mostramos el formulario de cracion
    enlaces = request.form.get('enlaces')  # PRIMERA variable par BD (En caso de no ser GET (else))
    n_caracteres = 4
    alfanumericos = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cortos = ""
    cortos = cortos.join([choice(alfanumericos) for i in range(n_caracteres)])  # SEGUNDA variable para BD
    enlacesModel = EnlacesModel()  # creamos la variable de tipo EnlacesModel
    raiz = 'localhost:5000/'
    cortos = raiz+cortos
    enlacesModel.insertar_enlaces(enlaces, cortos)# creamos el enlace    
    variableReenviar = cortos
    return render_template('enlaces/acortador.html', mostrar_en_vista=variableReenviar)

@app.route('/<cadena>', methods=['GET', 'POST'])
def ver_enlaces(cadena):
    raiz = 'localhost:5000/'
    consultor=raiz+cadena
    enlacesModel = EnlacesModel()
    encontrado=enlacesModel.traer_un_enlaces(consultor)
    for i in encontrado:
        encontrado=i[0]
    return redirect(encontrado)
    #return 'Esta es la url ' + str(encontrado)
