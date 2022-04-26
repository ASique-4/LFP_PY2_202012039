from Lexico import AnalizadorLexico
from Sintactico import AnalizadorSintactico
import PySimpleGUI as sg

sg.theme('DarkBlue')

layout = [[sg.Text('Your output will go here', size=(40, 1))],
        [sg.Output(size=(110, 20), font=('Helvetica 10'))],
        [sg.Multiline(size=(70, 5), enter_submits=False, key='-QUERY-', do_not_clear=False),
        sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
        sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

window = sg.Window('Chat window', layout, font=('Helvetica', ' 13'), default_button_element_size=(8,2), use_default_focus=False)

while True:     
    event, value = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'): 
        break
    if event == 'SEND':
        query = value['-QUERY-'].rstrip()
        print(query + '\n')
        lexico = AnalizadorLexico()

        cadena = query


        lexico.analizar(cadena)
        #lexico.imprimirTokens()

        #Guardar lista de tokens
        listaTokens = lexico.listaTokens


        #Análisis sintáctico
        sintactico = AnalizadorSintactico(listaTokens)
        sintactico.analizar()
        #sintactico.imprimirErrores()

        

window.close()
    




