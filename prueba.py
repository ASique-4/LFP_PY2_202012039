import pandas as pd
from prettytable import PrettyTable

datosPartidos = pd.read_csv('C:/Users/Angel/Desktop/VSCode/Carpeta para Github/[LFP]Proyecto2_202012039/LFP_PY2_202012039/LaLigaBot-LFP.csv')


def RESULTADO2(jornada,fecha1,fecha2,archivo):
    print(jornada,(str(fecha1)+'-'+str(fecha2)))
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
        print(filastxt)
        tmpfilas = eval(filastxt)
        filas.append(tmpfilas)
    print(filas)
    index = 0
    for i in columnas:
        x.add_column(i,filas[index])
        index += 1

    print(x)


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
    print(x)
    print('Generando archivo de resultados de temporada {}-{} del {}'.format(fecha1,fecha2,equipo))

def tablaGeneral(fecha1,fecha2,archivo):
    datos = (datosPartidos[ (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2)))])
    #print(datos)
    columnas = []
    x = PrettyTable()
    filas = []
    equipo1 = []
    equipo2 = []
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
        #filastxt += "['"+str(i)+"'" + ','
    E1 = eval('['+strE1[:-1]+']')
    E2 = eval('['+strE2[:-1]+']')
    #print(strE1)
    #print('----------------------------------------------------------------------------------')
    #print(strE2)
    strResultado = ''
    indexj = 0
    for i in E1:
        indexj = 0
        for j in E2:
            if i[0] == j[0]:
                #strResultado += "['{}',{}],".format(i[0],int(i[1])+int(j[1]))
                i[1] += j[1] 
                E2.pop(indexj)
            indexj += 1
    

    for i in E1:
        indexj = 0
        for j in E1:
            if i[0] == j[0] and i != j:
                i[1] += j[1]
                E1.pop(indexj)
            indexj +=1

    x.field_names = ['Equipo','Puntos']
    x.add_rows(E1)
    print(x)
    #filastxt[:-1]
    #filastxt = "["+filastxt+"]"
    #tmpfilas = eval(filastxt)
    #filas.append(tmpfilas)

    #index = 0
    #for i in columnas:
    #   x.add_column(i,filas[index])
    #    index += 1
def tablaTop(condicion,fecha1,fecha2,n):
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
    
    if condicion == 'reservada_INFERIOR':
        E1 = sorted(E1, key=lambda E1: E1[1])
    if condicion == 'reservada_SUPERIOR':
        E1 = sorted(E1, key=lambda E1: E1[1], reverse=True)

    x.field_names = ['Posicion','Equipo','Puntos']
    filas = ''
    i = 1
    while n >= i:
        filas += "[{},'{}',{}],".format(i,E1[i][0],E1[i][1])
        i += 1
    filas = eval('['+filas[:-1]+']')
    x.add_rows(filas)
    print(x)
    #print('Generando archivo de clasificación de temporada {}-{}'.format(fecha1,fecha2))             
             #RESULTADO "Levante" VS "Español" TEMPORADA <2017-2018>
             #RESULTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>
#RESULTADO('Real Madrid','Villarreal','2019','2020')
#RESULTADO2('12','2019','2020','jornada')
#obtenerResultadoDeEquipo('Real Madrid','1999','2000','prueba3','No','No')
#tablaGeneral('1996','1997','Prueba4')
tablaTop('reservada_INFERIOR','2000','2001',6)