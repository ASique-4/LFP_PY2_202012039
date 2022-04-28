
import webbrowser
import pandas as pd
from prettytable import *


datosPartidos = pd.read_csv('C:/Users/Angel/Desktop/VSCode/Carpeta para Github/[LFP]Proyecto2_202012039/LFP_PY2_202012039/LaLigaBot-LFP.csv')
def obtenerResultadoDePartido(equipo1,equipo2,fecha1,fecha2):
    datos = (datosPartidos[(datosPartidos['Equipo1'] == equipo1) & (datosPartidos['Equipo2'] == equipo2) & (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2)))])
    tmpEquipo1 = datos.iloc[0,3]
    tmpEquipo2 = datos.iloc[0,4]
    tmpGol1 = datos.iloc[0,5]
    tmpGol2 = datos.iloc[0,6]
    print('El resultado de este partido fue: {} {} - {} {}'.format(tmpEquipo1,tmpGol1,tmpEquipo2,tmpGol2))


def obtenerResultadoDeJornada(jornada,fecha1,fecha2,archivo):
    datos = (datosPartidos[(datosPartidos['Jornada'] == int(jornada)) & (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2)))])
    columnas = []
    x = PrettyTable()
    filas = []

    for j in datos.columns:
        filastxt = ''
        columnas.append(j)
        for i in datos[j]:
            filastxt += "'"+str(i)+"'" + ','

        filastxt[:-1]
        filastxt = "["+filastxt+"]"
        tmpfilas = eval(filastxt)
        filas.append(tmpfilas)
    index = 0
    for i in columnas:
        x.add_column(i,filas[index])
        index += 1

    print('Generando archivo de resultados jornada {} temporada {}-{}\n'.format(jornada,fecha1,fecha2))
    imprimir(archivo,x.get_html_string())

def obtenerResultadoDeEquipo(equipo,fecha1,fecha2,archivo,jorIni,jorFin):
    
    if jorIni != 'No' and jorFin == 'No':
        datos = (datosPartidos[((datosPartidos['Equipo1'] == str(equipo)) |  (datosPartidos['Equipo2'] == str(equipo)))  & (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2))) & (datosPartidos['Jornada'] >= int(jorIni))])
    elif jorFin != 'No' and jorIni == 'No':
        datos = (datosPartidos[((datosPartidos['Equipo1'] == str(equipo)) |  (datosPartidos['Equipo2'] == str(equipo))) & (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2))) & (datosPartidos['Jornada'] <= int(jorFin))])
    elif jorFin != 'No' and jorIni != 'No':
        datos = (datosPartidos[((datosPartidos['Equipo1'] == str(equipo)) |  (datosPartidos['Equipo2'] == str(equipo)))  & (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2))) & (datosPartidos['Jornada'] >= int(jorIni)) & (datosPartidos['Jornada'] <= int(jorFin))])
    else:
        datos = (datosPartidos[((datosPartidos['Equipo1'] == str(equipo)) |  (datosPartidos['Equipo2'] == str(equipo)))  & (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2)))])
    columnas = []
    x = PrettyTable()
    filas = []

    for j in datos.columns:
        filastxt = ''
        columnas.append(j)
        for i in datos[j]:
            filastxt += "'"+str(i)+"'" + ','

        filastxt[:-1]
        filastxt = "["+filastxt+"]"
        tmpfilas = eval(filastxt)
        filas.append(tmpfilas)
    index = 0
    for i in columnas:
        x.add_column(i,filas[index])
        index += 1
    #print(x)
    print('Generando archivo de resultados de temporada {}-{} del {}\n'.format(fecha1,fecha2,equipo))
    imprimir(archivo,x.get_html_string())

def tablaGeneral(fecha1,fecha2,archivo):
    datos = (datosPartidos[ (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2)))])
    x = PrettyTable()

    index = 0
    strE1 = ''
    strE2 = ''
    for i in datos['Equipo1']:
        if datos.iloc[index,5] > datos.iloc[index,6]:
            strE1 += "['{}',{}],".format(i,int(3))
        elif datos.iloc[index,5] == datos.iloc[index,6]:
            strE1 += "['{}',{}],".format(i,int(1))
        elif datos.iloc[index,5] < datos.iloc[index,6]:
            strE1 += "['{}',{}],".format(i,int(0))
        index += 1
            
    index = 0
    for i in datos['Equipo2']:
        if datos.iloc[index,5] > datos.iloc[index,6]:
            strE2 += "['{}',{}],".format(i,int(0))
        elif datos.iloc[index,5] == datos.iloc[index,6]:
            strE2 += "['{}',{}],".format(i,int(1))
        elif datos.iloc[index,5] < datos.iloc[index,6]:
            strE2 += "['{}',{}],".format(i,int(3))
        index += 1
    E1 = eval('['+strE1[:-1]+']')
    E2 = eval('['+strE2[:-1]+']')

    indexj = 0
    for i in E1:
        indexj = 0
        for j in E2:
            if i[0] == j[0]:
                i[1] += j[1] 
                E2.pop(indexj)
            indexj += 1
    

    for i in E1:
        indexj = 0
        for j in E1:
            if str(i[0]).lower() == str(j[0]).lower() and i != j:
                i[1] += j[1]
                E1.pop(indexj)
            indexj +=1

    x.field_names = ['Equipo','Puntos']
    x.add_rows(E1)
    print('Generando archivo de clasificación de temporada {}-{}\n'.format(fecha1,fecha2))
    imprimir(archivo,x.get_html_string())

def tablaTop(condicion,fecha1,fecha2,n):
    datos = (datosPartidos[ (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2)))])
    x = PrettyTable()

    index = 0
    strE1 = ''
    strE2 = ''
    filas = ''
    for i in datos['Equipo1']:
        if datos.iloc[index,5] > datos.iloc[index,6]:
            strE1 += "['{}',{}],".format(i,int(3))
        elif datos.iloc[index,5] == datos.iloc[index,6]:
            strE1 += "['{}',{}],".format(i,int(1))
        elif datos.iloc[index,5] < datos.iloc[index,6]:
            strE1 += "['{}',{}],".format(i,int(0))
        index += 1
            
    index = 0
    for i in datos['Equipo2']:
        if datos.iloc[index,5] > datos.iloc[index,6]:
            strE2 += "['{}',{}],".format(i,int(0))
        elif datos.iloc[index,5] == datos.iloc[index,6]:
            strE2 += "['{}',{}],".format(i,int(1))
        elif datos.iloc[index,5] < datos.iloc[index,6]:
            strE2 += "['{}',{}],".format(i,int(3))
        index += 1
    E1 = eval('['+strE1[:-1]+']')
    E2 = eval('['+strE2[:-1]+']')

    indexj = 0
    for i in E1:
        indexj = 0
        for j in E2:
            if str(i[0]).lower() == str(j[0]).lower():
                i[1] += j[1] 
                E2.pop(indexj)
            indexj += 1
    

    for i in E1:
        indexj = 0
        for j in E1:
            if str(i[0]).lower() == str(j[0]).lower() and i != j:
                i[1] += j[1]
                E1.pop(indexj)
            indexj +=1
    
    if condicion == 'reservada_INFERIOR':
        E1 = sorted(E1, key=lambda E1: E1[1])
    elif condicion == 'reservada_SUPERIOR':
        E1 = sorted(E1, key=lambda E1: E1[1], reverse=True)

    x.field_names = ['Posicion','Equipo','Puntos']
    i = 1
    while int(n) >= i:
        filas += "[{},'{}',{}],".format(i,E1[i][0],E1[i][1])
        i += 1
    filas = eval('['+filas[:-1]+']')
    x.add_rows(filas)
    x.set_style(MSWORD_FRIENDLY)
    if condicion == 'reservada_INFERIOR':
        print('El top inferior de la temporada {}-{} fue: '.format(fecha1,fecha2))
        print(x)
        print('\n')
    elif condicion == 'reservada_SUPERIOR':
        print('El top superior de la temporada {}-{} fue: '.format(fecha1,fecha2))
        print(x)
        print('\n')
        
def CantidadDeGoles(condicion,equipo,fecha1,fecha2):
    datos = (datosPartidos[ (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2)))])

    index = 0
    strE1 = ''
    strE2 = ''
    if condicion == 'reservada_LOCAL':
        for i in datos['Equipo1']:
            if str(i) == str(equipo):
                strE1 += "['{}',{}],".format(i,int(datos.iloc[index,5]))
            index += 1
        index = 0
        E1 = eval('['+strE1[:-1]+']')
        for i in E1:
            indexj = 0
            for j in E1:
                if str(i[0]).lower() == str(j[0]).lower() and i != j:
                    i[1] += j[1]
                    E1.pop(indexj)
                indexj +=1

    elif condicion == 'reservada_VISITANTE':
        for i in datos['Equipo2']:
            if str(i) == str(equipo):
                strE1 += "['{}',{}],".format(i,int(datos.iloc[index,6]))
            index += 1
        index = 0
        E1 = eval('['+strE1[:-1]+']')
        for i in E1:
            indexj = 0
            for j in E1:
                if str(i[0]).lower() == str(j[0]).lower() and i != j:
                    i[1] += j[1]
                    E1.pop(indexj)
                indexj +=1

    elif condicion == 'reservada_TOTAL':
        for i in datos['Equipo1']:
            if str(i) == str(equipo):
                strE1 += "['{}',{}],".format(i,int(datos.iloc[index,5]))
            index += 1
        index = 0
        for i in datos['Equipo2']:
            if str(i) == str(equipo):
                strE2 += "['{}',{}],".format(i,int(datos.iloc[index,6]))
            index += 1

        E1 = eval('['+strE1[:-1]+']')
        E2 = eval('['+strE2[:-1]+']')

        indexj = 0
        for i in E1:
            indexj = 0
            for j in E2:
                if i[0] == j[0]:
                    i[1] += j[1] 
                    E2.pop(indexj)
                indexj += 1
        
        for i in E1:
            indexj = 0
            for j in E1:
                if str(i[0]).lower() == str(j[0]).lower() and i != j:
                    i[1] += j[1]
                    E1.pop(indexj)
                indexj +=1

    if E1 != [] and E1 != None and E1[1] != None and E1[1][1] != None:
        print('Los goles anotados por el {} en total en la temporada {}-{} fueron {} \n'.format(equipo,fecha1,fecha2,E1[1][1]))
    else:
        print('Algo salio mal :(\n')



def imprimir(archivo,tabla):
    '''Imprime una tabla en HTML'''
    strARCHIVO = open(archivo+'.html','w')
    strHTML = '''<!DOCTYPE html>
                <html>
                
                    <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>'''+archivo+'''</title>
                    </head>
                    <style>
                    table, th, td {
                    border: 1px solid rgb(31, 31, 31);
                    border-collapse: collapse;
                    background-color: #000000;
                    color: #00CED1;
                    }

                    th:nth-child(even),td:nth-child(even) {
                    background-color: #494949;
                    }
                    </style>
                    <body bgcolor="DarkSlateGray">
                        <center>
                            '''

    strHTML += tabla
    strHTML += '''      </center>
                    </body>
                </html>'''
    strARCHIVO.write(strHTML)
    strARCHIVO.close()
    webbrowser.open(archivo+'.html')