from Lexico import AnalizadorLexico
from Sintactico import AnalizadorSintactico
import PySimpleGUI as sg
from bases import imprimir

sg.theme('DarkBlue2')

layout = [
        [sg.Output(size=(110, 20), font=('Helvetica 10'),text_color='white'),[sg.Button('REPORTE DE \nERRORES', button_color=('DarkTurquoise', 'Black'))
        ,sg.Button('LIMPIAR LOG\n DE ERRORES', button_color=('DarkTurquoise', 'Black')),sg.Button('REPORTE DE \nTOKENS', button_color=('DarkTurquoise', 'Black'))
        ,sg.Button('LIMPIAR LOG\n DE TOKENS', button_color=('DarkTurquoise', 'Black')),sg.Button('MANUAL DE\n USUARIO', button_color=('DarkTurquoise', 'Black'))
        ,sg.Button('MANUAL TECNICO', button_color=('DarkTurquoise', 'Black'))]],
        [sg.Multiline(size=(70, 5), enter_submits=False, key='-QUERY-', do_not_clear=False,text_color='white'),
        sg.Button('ENVIAR', button_color=('DarkTurquoise', 'Black'), bind_return_key=True),
        sg.Button('SALIR', button_color=('DarkTurquoise', 'Black'))]]

window = sg.Window('La Liga Bot', layout, font=('Helvetica', ' 13'), default_button_element_size=(8,2), use_default_focus=False)
#PARTIDOS "Real Madrid" TEMPORADA <1999-2000> -ji 1 -jf 18
while True:    
    
    event, value = window.read()
    if event in (sg.WIN_CLOSED, 'SALIR'): 
        break
    
    if event == 'ENVIAR':
        query = value['-QUERY-'].rstrip()
        print(query + '\n')
        lexico = AnalizadorLexico()
        

        cadena = query


        lexico.analizar(cadena)
        #lexico.imprimirTokens()
        #lexico.imprimirErrores()
        global tokens 
        tokens = lexico.imprimirTokens()
        #Guardar lista de tokens
        listaTokens = lexico.listaTokens


        #Análisis sintáctico
        sintactico = AnalizadorSintactico(listaTokens)
        sintactico.analizar()
        #sintactico.imprimirErrores()

    if event == ('REPORTE DE \nERRORES'): 
        l = lexico.imprimirErrores()
        s = sintactico.imprimirErrores()
        imprimir('Reporte de errores',l+'\n'+s)
    if event == ( 'LIMPIAR LOG\n DE ERRORES'): 
        lexico.listaErrores = []
        sintactico.errores = []
    if event == ( 'REPORTE DE \nTOKENS'): 
        t = tokens
        imprimir('Reporte de tokens',t)
    if event == ('MANUAL TECNICO'): 
        pass
    if event == ('LIMPIAR LOG\n DE TOKENS'): 
        lexico.listaTokens = []
        tokens = lexico.imprimirTokens()
    if event == ('MANUAL DE\n USUARIO'): 
        pass
        

window.close()
    




