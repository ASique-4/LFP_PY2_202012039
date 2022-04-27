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
             #RESULTADO "Levante" VS "Español" TEMPORADA <2017-2018>
             #RESULTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>
#RESULTADO('Real Madrid','Villarreal','2019','2020')
#RESULTADO2('12','2019','2020','jornada')
obtenerResultadoDeEquipo('Real Madrid','1999','2000','prueba3','1','18')