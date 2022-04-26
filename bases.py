from ast import Pass
import json
import pandas as pd
from prettytable import PrettyTable

datosPartidos = pd.read_csv('C:/Users/Angel/Desktop/VSCode/Carpeta para Github/[LFP]Proyecto2_202012039/LFP_PY2_202012039/LaLigaBot-LFP.csv')
def RESULTADO(equipo1,equipo2,fecha1,fecha2):
    datos = (datosPartidos[(datosPartidos['Equipo1'] == equipo1) & (datosPartidos['Equipo2'] == equipo2) & (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2)))])
    tmpEquipo1 = datos.iloc[0,3]
    tmpEquipo2 = datos.iloc[0,4]
    tmpGol1 = datos.iloc[0,5]
    tmpGol2 = datos.iloc[0,6]
    print('El resultado de este partido fue: {} {} - {} {}'.format(tmpEquipo1,tmpGol1,tmpEquipo2,tmpGol2))


def createTable(nombre,base):
    cadena = ''
    with open("bases.txt",'r+') as file:
        diccionario = json.loads(file.read())
        diccionario["bases"][base][nombre] = []
        cadena = json.dumps(diccionario)
    escribir(cadena)
    print("Se creó en la base de datos",base,"la tabla",nombre)

def insertar(tabla,base,registro):
    cadena = ''
    with open("bases.txt",'r+') as file:
        diccionario = json.loads(file.read())
        diccionario["bases"][base][tabla].append(list(registro))
        cadena = json.dumps(diccionario)
    escribir(cadena)
    print("Se insertó en la tabla",tabla,"de la base",base,"un registro")

def escribir(cadena):
    with open("bases.txt",'w') as file:
        file.write(cadena)

def imprimir(tabla,base):
    print("Imprimiendo tabla",tabla,"de la base",base)
    lista = []
    with open("bases.txt",'r') as file:
        lista = json.loads(file.read())["bases"][base][tabla]
    x = PrettyTable()
    for registro in lista:
        x.add_row(registro)
    print(x) 