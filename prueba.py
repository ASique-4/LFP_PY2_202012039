import pandas as pd

datosPartidos = pd.read_csv('C:/Users/Angel/Desktop/VSCode/Carpeta para Github/[LFP]Proyecto2_202012039/LFP_PY2_202012039/LaLigaBot-LFP.csv')

def RESULTADO(equipo1,equipo2,fecha1,fecha2):
    print(datosPartidos[(datosPartidos['Equipo1'] == equipo1) & (datosPartidos['Equipo2'] == equipo2) & (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2)))].iloc[0,6])

def RESULTADO2(equipo1,equipo2,fecha1,fecha2):
    datos = (datosPartidos[(datosPartidos['Equipo1'] == equipo1) & (datosPartidos['Equipo2'] == equipo2) & (datosPartidos['Temporada'] == (str(fecha1)+'-'+str(fecha2)))])
    tmpEquipo1 = datos.iloc[0,3]
    tmpEquipo2 = datos.iloc[0,4]
    tmpGol1 = datos.iloc[0,5]
    tmpGol2 = datos.iloc[0,6]
    print('El resultado de este partido fue: {} {} - {} {}'.format(tmpEquipo1,tmpGol1,tmpEquipo2,tmpGol2))

             #RESULTADO "Levante" VS "Español" TEMPORADA <2017-2018>
             #RESULTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>
#RESULTADO('Real Madrid','Villarreal','2019','2020')
RESULTADO2('Real Madrid','Villarreal','2019','2020')