
import sys
from time import sleep
from prettytable import PrettyTable
from bases import *

class AnalizadorSintactico:

    def __init__(self,tokens : list) -> None:
        self.errores = []
        self.tokens = tokens

    def agregarError(self,esperado,obtenido):
        self.errores.append(
            '''ERROR SINTÁCTICO: se obtuvo {} se esperaba {}'''.format(obtenido,esperado)
        )

    def sacarToken(self):
        ''' Saca el primer token y lo quita de la lista'''
        try:
            return self.tokens.pop(0)
        except:
            return None

    def observarToken(self):
        ''' Saca el primer token y lo mete de nuevo en de la lista'''
        try:
            return self.tokens[0]
        except:
            return None

    
    def analizar(self):
        self.S()

    def S(self):
        self.INICIO()

    def INICIO(self):
        # Observar el primer elemento para
        # decidir a donde ir
        temporal = self.observarToken()
        if temporal is None:
            self.agregarError('reservada_RESULTADO | reservada_JORNADA | reservada_GOLES | reservada_TABLA | reservada_PARTIDOS | reservada_TOP | reservada_ADIOS',"EOF")
        elif temporal.tipo == 'reservada_RESULTADO':
            self.resultadoDePartido()
        elif temporal.tipo == 'reservada_JORNADA':
            self.resultadoDeJornada()
        elif temporal.tipo == 'reservada_PARTIDOS':
            self.TEMPORADA_DE_UN_EQUIPO()
        elif temporal.tipo == 'reservada_TABLA':
            self.TABLA_GENERAL()
        elif temporal.tipo == 'reservada_TOP':
            self.TABLA_TOP()
        elif temporal.tipo == 'reservada_ADIOS':
            print('Nos vemos luego :D')
            sleep(5)
            sys.exit()
        else:
            self.agregarError('reservada_RESULTADO | reservada_JORNADA | reservada_GOLES | reservada_TABLA | reservada_PARTIDOS | reservada_TOP | reservada_ADIOS',temporal.tipo)

    def resultadoDePartido(self):
        # Comando para obtener resultado de un partido


        # Sacar token --- se espera reservada_RESULTADO
        token = self.sacarToken()
        if token.tipo == 'reservada_RESULTADO':
            # Sacar otro token --- se espera cadena
            token = self.sacarToken()
            if token is None:
                self.agregarError("cadena","EOF")
                return
            elif token.tipo == "cadena":
                # Se guarda el equipo
                equipo2 = token.lexema
                # Sacar otro token --- se espera reservada_VS
                token = self.sacarToken()
                if token is None:
                    self.agregarError("reservada_VS","EOF")
                    return
                elif token.tipo == "reservada_VS":
                    # Sacar otro token --- se espera cadena
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("cadena","EOF")
                        return
                    elif token.tipo == "cadena":
                        # Se guarda el equipo
                        equipo1 = token.lexema
                        # Sacar otro token --- se espera reservada_TEMPORADA
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("reservada_TEMPORADA","EOF")
                            return
                        elif token.tipo == "reservada_TEMPORADA":
                            # Sacar otro token --- se espera menorQue
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("menorQue","EOF")
                                return
                            elif token.tipo == "menorQue":
                                # Sacar otro token --- se espera año
                                token = self.sacarToken()
                                if token is None:
                                    self.agregarError("numero","EOF")
                                    return
                                elif token.tipo == "numero":
                                    # Se guarda el primer año
                                    fecha1 = token.lexema
                                    # Sacar otro token --- se espera guion
                                    token = self.sacarToken()
                                    if token is None:
                                        self.agregarError("guion","EOF")
                                        return
                                    elif token.tipo == "guion":
                                        # Sacar otro token --- se espera guion
                                        token = self.sacarToken()
                                        if token is None:
                                            self.agregarError("numero","EOF")
                                            return
                                        elif token.tipo == "numero":
                                            # Se guarda el primer año
                                            fecha2 = token.lexema
                                            # Sacar otro token --- se espera mayorQue
                                            token = self.sacarToken()
                                            if token is None:
                                                self.agregarError("mayorQue","EOF")
                                                return
                                            elif token.tipo == "mayorQue":
                                                #Llamo a mi funcionalidad
                                                obtenerResultadoDePartido(equipo2,equipo1,fecha1,fecha2)
                                                
                                            else:
                                                self.agregarError("mayorQue",token.tipo)
                                        else:
                                            self.agregarError("numero",token.tipo)
                                    else:
                                        self.agregarError("guion",token.tipo)
                                else:
                                    self.agregarError("numero",token.tipo)
                            else:
                                self.agregarError("menorQue",token.tipo)
                            
                        else:
                            self.agregarError("reservada_TEMPORADA",token.tipo)
                    else:
                        self.agregarError("cadena",token.tipo)
                    
                else:
                    self.agregarError("reservada_VS",token.tipo)
            else:
                self.agregarError("cadena",token.tipo)
        else:
            self.agregarError("reservada_RESULTADO","EOF")
        


    def resultadoDeJornada(self):
        # Comando para obtener resultado de jornada

        # Sacar token --- se espera reservada_JORNADA
        token = self.sacarToken()
        if token.tipo == 'reservada_JORNADA':
            # Sacar otro token --- se espera numero
            token = self.sacarToken()
            if token is None:
                self.agregarError("numero","EOF")
                return
            elif token.tipo == "numero":
                jornada = token.lexema
                # Sacar otro token --- se espera reservada_TEMPORADA
                token = self.sacarToken()
                if token is None:
                    self.agregarError("reservada_TEMPORADA","EOF")
                    return
                elif token.tipo == "reservada_TEMPORADA":
                    
                    # Sacar otro token --- se espera menorQue
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("menorQue","EOF")
                        return
                    elif token.tipo == "menorQue":
                        # Sacar otro token --- se espera numero
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("numero","EOF")
                            return
                        elif token.tipo == "numero":
                            fecha1 = token.lexema
                            # Sacar otro token --- se espera guion
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("guion","EOF")
                                return
                            elif token.tipo == "guion":
                                # Sacar otro token --- se espera numero
                                token = self.sacarToken()
                                if token is None:
                                    self.agregarError("numero","EOF")
                                    return
                                elif token.tipo == "numero":
                                    fecha2 = token.lexema
                                    # Sacar otro token --- se espera mayorQue
                                    token = self.sacarToken()
                                    if token is None:
                                        self.agregarError("mayorQue","EOF")
                                        return
                                    elif token.tipo == "mayorQue":
                                        # Sacar otro token --- se espera -f
                                        token = self.sacarToken()
                                        if token is None:
                                            obtenerResultadoDeJornada(jornada,fecha1,fecha2,'jornada')
                                            return
                                        elif token.tipo == "-f":
                                            
                                            # Sacar otro token --- se espera cadena
                                            token = self.sacarToken()
                                            if token is None:
                                                self.agregarError("cadena","EOF")
                                                return
                                            elif token.tipo == "cadena":
                                                archivo = token.lexema
                                                obtenerResultadoDeJornada(jornada,fecha1,fecha2,archivo)
                                            else:
                                                self.agregarError("cadena",token.tipo)
                                        else:
                                            self.agregarError("-f",token.tipo)
                                    else:
                                        self.agregarError("mayorQue",token.tipo)
                                else:
                                    self.agregarError("numero",token.tipo)
                            else:
                                self.agregarError("guion",token.tipo)
                        else:
                            self.agregarError("numero",token.tipo)   
                    else:
                        self.agregarError("menorQue",token.tipo)                    
                else:
                    self.agregarError("reservada_TEMPORADA",token.tipo)
            else:
                self.agregarError("numero",token.tipo)
        else:
            self.agregarError("reservada_JORNADA","EOF")        


    def TEMPORADA_DE_UN_EQUIPO(self):
        archivo = 'partidos'
        jorfin = 'No'
        jorIni = 'No'
        # Sacar token --- se espera reservada_PARTIDOS
        token = self.sacarToken()
        if token.tipo == 'reservada_PARTIDOS':
            # Sacar otro token --- se espera cadena
            token = self.sacarToken()
            if token is None:
                self.agregarError("reservada_EQUIPO","EOF")
                return
            elif token.tipo == "cadena" :
                equipo = token.lexema
                # Sacar otro token --- se espera reservada_TEMPORADA
                token = self.sacarToken()
                if token is None:
                    self.agregarError("reservada_TEMPORADA","EOF")
                    return
                elif token.tipo == "reservada_TEMPORADA":
                    # Sacar otro token --- se espera menorQue
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("menorQue","EOF")
                        return
                    elif token.tipo == "menorQue":
                        # Sacar otro token --- se espera numero
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("numero","EOF")
                            return
                        elif token.tipo == "numero":
                            fecha1 = token.lexema
                            # Sacar otro token --- se espera guion
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("guion","EOF")
                                return
                            elif token.tipo == "guion":
                                # Sacar otro token --- se espera numero
                                token = self.sacarToken()
                                if token is None:
                                    self.agregarError("numero","EOF")
                                    return
                                elif token.tipo == "numero":
                                    fecha2 = token.lexema
                                    # Sacar otro token --- se espera mayorQue
                                    token = self.sacarToken()
                                    if token is None:
                                        self.agregarError("mayorQue","EOF")
                                        return
                                    elif token.tipo == "mayorQue":
                                        # Sacar otro token --- se espera -f
                                        token = self.sacarToken()
                                        if token is None:
                                            obtenerResultadoDeEquipo(equipo,fecha1,fecha2,archivo,jorIni,jorfin)
                                            return
                                        elif token.tipo == "-f":
                                            # Sacar otro token --- se espera cadena
                                            token = self.sacarToken()
                                            if token is None:
                                                self.agregarError("cadena","EOF")
                                                return
                                            elif token.tipo == "cadena":
                                                archivo = token.lexema
                                                token = self.sacarToken()
                                                if token.tipo == "-ji":
                                                    # Sacar otro token --- se espera numero
                                                    token = self.sacarToken()
                                                    if token is None:
                                                        self.agregarError("cadena","EOF")
                                                        return
                                                    elif token.tipo == "numero":
                                                        jorIni = token.lexema
                                                        token = self.sacarToken()
                                                        if token.tipo == "-jf":
                                                            # Sacar otro token --- se espera numero
                                                            token = self.sacarToken()
                                                            if token is None:
                                                                self.agregarError("numero","EOF")
                                                                return
                                                            elif token.tipo == "numero":
                                                                jorfin = token.lexema
                                                                token = self.sacarToken()
                                                                obtenerResultadoDeEquipo(equipo,fecha1,fecha2,archivo,jorIni,jorfin)
                                                            else:
                                                                self.agregarError("cadena",token.tipo)
                                                    else:
                                                        self.agregarError("cadena",token.tipo)
                                                elif token.tipo == "-jf":
                                                    
                                                    # Sacar otro token --- se espera numero
                                                    token = self.sacarToken()
                                                    if token is None:
                                                        self.agregarError("cadena","EOF")
                                                        return
                                                    elif token.tipo == "numero":
                                                        jorfin = token.lexema
                                                        token = self.sacarToken()
                                                        if token.tipo == "-ji":
                                                    
                                                            # Sacar otro token --- se espera numero
                                                            token = self.sacarToken()
                                                            if token is None:
                                                                self.agregarError("numero","EOF")
                                                                return
                                                            elif token.tipo == "numero":
                                                                jorIni = token.lexema
                                                                obtenerResultadoDeEquipo(equipo,fecha1,fecha2,archivo,jorIni,jorfin)
                                                            else:
                                                                self.agregarError("numero",token.tipo)
                                                    else:
                                                        self.agregarError("cadena",token.tipo)
                                            else:
                                                self.agregarError("cadena",token.tipo)
                                        elif token.tipo == "-ji":
                                            # Sacar otro token --- se espera numero
                                            token = self.sacarToken()
                                            if token is None:
                                                self.agregarError("numero","EOF")
                                                return
                                            elif token.tipo == "numero":
                                                jorIni = token.lexema
                                                token = self.sacarToken()
                                                if token.tipo == "-f":
                                                    # Sacar otro token --- se espera cadena
                                                    token = self.sacarToken()
                                                    if token is None:
                                                        self.agregarError("cadena","EOF")
                                                        return
                                                    elif token.tipo == "cadena":
                                                        archivo = token.lexema
                                                        token = self.sacarToken()
                                                        if token.tipo == "-jf":
                                                            # Sacar otro token --- se espera numero
                                                            token = self.sacarToken()
                                                            if token is None:
                                                                self.agregarError("numero","EOF")
                                                                return
                                                            elif token.tipo == "numero":
                                                                jorfin = token.lexema
                                                                obtenerResultadoDeEquipo(equipo,fecha1,fecha2,archivo,jorIni,jorfin)
                                                            else:
                                                                self.agregarError("numero",token.tipo)
                                                    else:
                                                        self.agregarError("cadena",token.tipo)
                                                elif token.tipo == "-jf":
                                                    
                                                    # Sacar otro token --- se espera numero
                                                    token = self.sacarToken()
                                                    if token is None:
                                                        self.agregarError("numero","EOF")
                                                        return
                                                    elif token.tipo == "numero":
                                                        jorfin = token.lexema
                                                        token = self.sacarToken()
                                                        if token is None:
                                                            obtenerResultadoDeEquipo(equipo,fecha1,fecha2,archivo,jorIni,jorfin)
                                                            return
                                                        elif token.tipo == "-f":
                                                    
                                                            # Sacar otro token --- se espera cadena
                                                            token = self.sacarToken()
                                                            if token is None:
                                                                self.agregarError("cadena","EOF")
                                                                return
                                                            elif token.tipo == "cadena":
                                                                archivo = token.lexema
                                                                token = self.sacarToken()
                                                                obtenerResultadoDeEquipo(equipo,fecha1,fecha2,archivo,jorIni,jorfin)
                                                            else:
                                                                self.agregarError("cadena",token.tipo)
                                                    else:
                                                        self.agregarError("numero",token.tipo)
                                        elif token.tipo == "-jf":
                                            # Sacar otro token --- se espera numero
                                            token = self.sacarToken()
                                            if token is None:
                                                self.agregarError("numero","EOF")
                                                return
                                            elif token.tipo == "numero":
                                                archivo = token.lexema
                                                if token.tipo == "-f":
                                                    # Sacar otro token --- se espera cadena
                                                    token = self.sacarToken()
                                                    if token is None:
                                                        self.agregarError("cadena","EOF")
                                                        return
                                                    elif token.tipo == "cadena":
                                                        archivo = token.lexema
                                                        token = self.sacarToken()
                                                        if token.tipo == "-ji":
                                                            # Sacar otro token --- se espera numero
                                                            token = self.sacarToken()
                                                            if token is None:
                                                                self.agregarError("numero","EOF")
                                                                return
                                                            elif token.tipo == "numero":
                                                                jorIni = token.lexema
                                                                obtenerResultadoDeEquipo(equipo,fecha1,fecha2,archivo,jorIni,jorfin)
                                                            else:
                                                                self.agregarError("numero",token.tipo)
                                                    else:
                                                        self.agregarError("cadena",token.tipo)
                                                elif token.tipo == "-ji":
                                                    
                                                    # Sacar otro token --- se espera numero
                                                    token = self.sacarToken()
                                                    if token is None:
                                                        self.agregarError("numero","EOF")
                                                        return
                                                    elif token.tipo == "numero":
                                                        jorIni = token.lexema
                                                        token = self.sacarToken()
                                                        if token.tipo == "-f":
                                                    
                                                            # Sacar otro token --- se espera cadena
                                                            token = self.sacarToken()
                                                            if token is None:
                                                                self.agregarError("cadena","EOF")
                                                                return
                                                            elif token.tipo == "cadena":
                                                                archivo = token.lexema
                                                                obtenerResultadoDeEquipo(equipo,fecha1,fecha2,archivo,jorIni,jorfin)
                                                            else:
                                                                self.agregarError("cadena",token.tipo)
                                                    else:
                                                        self.agregarError("numero",token.tipo)
                                    else:
                                        self.agregarError("mayorQue",token.tipo) 
                                else:
                                    self.agregarError("numero",token.tipo)
                            else:
                                self.agregarError("guion",token.tipo)
                        else:
                            self.agregarError("numero",token.tipo)                             
                    else:
                        self.agregarError("menorQue",token.tipo)                     
                else:
                    self.agregarError("reservada_TEMPORADA",token.tipo)                         
            else:
                self.agregarError("cadena",token.tipo)          
        else:
            self.agregarError("cadena","EOF")                


    def LISTA(self):
        # Producción
        #            LISTA' ::= VALOR LISTA'
        #Valor es un str o un int
        valor = self.VALOR()
        if valor is None:
            return
        
        lista_ = self.LISTA_()
        if lista_ is None:
            return        
                  #[3]    + [1,3,4]
                  #[3,1,3,4]
        return [valor] + lista_

    def LISTA_(self):
        # Producción
        #            LISTA' ::= coma VALOR LISTA' | epsilon
        
        #Para no perder el token en caso de irnos por epsilon, solo lo observo
        token = self.observarToken()
        if token is None:
            return
        if token.tipo == 'coma':
            #Ya se que es una coma entonces si lo saco
            token = self.sacarToken()

            #Llamamos al no terminal VALOR
            # Valor retorna un numero o una cadena
            valor = self.VALOR()
            #Si el valor es None quiere decir que hubo un error sintactico en VALOR
            #Entonces seguimos 'subiendo' ese None
            if valor is None:
                return
            
            lista_prima = self.LISTA_()

            #Si el valor es None quiere decir que hubo un error sintactico en LISTA'    
            if lista_prima is None:
                return
                
            #Retornamos una lista con lo obtenido en VALOR Y LISTA'
            return [valor] + lista_prima
        else:
            # Como en está producción es posible esperar un epsilon
            # Voy a retornar una lista vacía en caso de que token.tipo
            # no     sea una coma, esto para simular el epsilon
            return []
    

    def VALOR(self):
        # Producción
        #            VALOR ::= cadena | numero
              
        token = self.sacarToken()
        # Si no viene un token retornamos None para
        # Causar que no se ejecute el comando
        if token is None:
            self.agregarError("cadena | entero","EOF") 
            return
        if token.tipo == 'cadena':
            return token.lexema
        elif token.tipo == 'entero':
            return int(token.lexema)
        else:
            self.agregarError("cadena | entero",token.tipo) 

    def TABLA_GENERAL(self):
        # Comando de impresión de tabla general
    
        archivo = 'temporada'
        # Sacar token --- se espera reservada_TABLA
        token = self.sacarToken()
        if token.tipo == 'reservada_TABLA':
            # Sacar otro token --- se espera reservada_TEMPORADA
            token = self.sacarToken()
            if token is None:
                self.agregarError("reservada_TEMPORADA","EOF")
                return
            elif token.tipo == "reservada_TEMPORADA":
                
                # Sacar otro token --- se espera menorQue
                token = self.sacarToken()
                if token is None:
                    self.agregarError("menorQue","EOF")
                    return
                elif token.tipo == "menorQue":
                    # Sacar otro token --- se espera numero
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("numero","EOF")
                        return
                    elif token.tipo == "numero":
                        fecha1 = token.lexema
                        # Sacar otro token --- se espera guion
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("guion","EOF")
                            return
                        elif token.tipo == "guion":
                            # Sacar otro token --- se espera numero
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("numero","EOF")
                                return
                            elif token.tipo == "numero":
                                fecha2 = token.lexema
                                # Sacar otro token --- se espera mayorQue
                                token = self.sacarToken()
                                if token is None:
                                    self.agregarError("mayorQue","EOF")
                                    return
                                elif token.tipo == "mayorQue":
                                    # Sacar otro token --- se espera -f
                                    token = self.sacarToken()
                                    if token is None:
                                        tablaGeneral(fecha1,fecha2,archivo)
                                        return
                                    elif token.tipo == "-f":
                                        # Sacar otro token --- se espera cadena
                                        token = self.sacarToken()
                                        if token is None:
                                            self.agregarError("cadena","EOF")
                                            return
                                        elif token.tipo == "cadena":
                                            archivo = token.lexema
                                            tablaGeneral(fecha1,fecha2,archivo)
                                        else:
                                            self.agregarError("cadena",token.tipo)
                                    else:
                                        self.agregarError("-f",token.tipo)
                                else:
                                    self.agregarError("mayorQue",token.tipo) 
                            else:
                                self.agregarError("numero",token.tipo) 
                        else:
                            self.agregarError("guion",token.tipo) 
                    else:
                        self.agregarError("numero",token.tipo)     
                else:
                    self.agregarError("menorQue",token.tipo)                  
            else:
                self.agregarError("reservada_TEMPORADA",token.tipo)           
        else:
            self.agregarError("reservada_TABLA","EOF")                

    def TABLA_TOP(self):
            # Comando de impresión de tabla general
        
            n = 5
            # Sacar token --- se espera reservada_TABLA
            token = self.sacarToken()
            if token.tipo == 'reservada_TOP':
                # Sacar otro token --- se espera reservada_SUPERIOR | reservada_INFERIOR
                token = self.sacarToken()
                if token is None:
                    self.agregarError("reservada_SUPERIOR | reservada_INFERIOR","EOF")
                    return
                elif token.tipo == "reservada_SUPERIOR" or token.tipo == "reservada_INFERIOR" :
                    condicion = token.tipo
                    # Sacar otro token --- se espera reservada_TEMPORADA
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("reservada_TEMPORADA","EOF")
                        return
                    elif token.tipo == "reservada_TEMPORADA":
                        # Sacar otro token --- se espera menorQue
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("menorQue","EOF")
                            return
                        elif token.tipo == "menorQue":
                            # Sacar otro token --- se espera numero
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("numero","EOF")
                                return
                            elif token.tipo == "numero":
                                # Sacar otro token --- se espera guion
                                fecha1 = token.lexema
                                token = self.sacarToken()
                                if token is None:
                                    self.agregarError("guion","EOF")
                                    return
                                elif token.tipo == "guion":
                                    
                                    # Sacar otro token --- se espera numero
                                    token = self.sacarToken()
                                    if token is None:
                                        self.agregarError("numero","EOF")
                                        return
                                    elif token.tipo == "numero":
                                        fecha2 = token.lexema
                                        # Sacar otro token --- se espera mayorQue
                                        token = self.sacarToken()
                                        if token is None:
                                            self.agregarError("mayorQue","EOF")
                                            return
                                        elif token.tipo == "mayorQue":
                                            # Sacar otro token --- se espera -n
                                            token = self.sacarToken()
                                            if token is None:
                                                tablaTop(fecha1,fecha2,n)
                                                return
                                            elif token.tipo == "-n":
                                                # Sacar otro token --- se espera numero
                                                token = self.sacarToken()
                                                if token is None:
                                                    self.agregarError("numero","EOF")
                                                    return
                                                elif token.tipo == "numero":
                                                    n = token.lexema
                                                    tablaTop(fecha1,fecha2,n)
                                                else:
                                                    self.agregarError("numero",token.tipo)
                                            else:
                                                self.agregarError("-n",token.tipo)
                                        else:
                                            self.agregarError("mayorQue",token.tipo)
                                    else:
                                        self.agregarError("numero",token.tipo) 
                                else:
                                    self.agregarError("guion",token.tipo) 
                            else:
                                self.agregarError("numero",token.tipo) 
                        else:
                            self.agregarError("menorQue",token.tipo)     
                    else:
                        self.agregarError("reservada_TEMPORADA",token.tipo)                  
                else:
                    self.agregarError("reservada_SUPERIOR | reservada_INFERIOR",token.tipo)           
            else:
                self.agregarError("reservada_TOP","EOF")       

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Descripcion"]
        for error_ in self.errores:
            x.add_row([error_])
        print(x)            