from soupsieve import select
from Token import Token
from Error import Error
from prettytable import PrettyTable

class AnalizadorLexico:

    
    def __init__(self) -> None:
        self.listaTokens  = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.estado = 0
        self.simbolo = ''
        self.i = 0
    
    def limpiartokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema","Linea","Columna","Tipo"]
        

    def limpiarErrores(self):
        x1 = PrettyTable()
        x1.field_names = ["Descripcion"]

    def agregar_token(self,caracter,linea,columna,token):
        self.listaTokens.append(Token(caracter,linea,columna,token))
        self.buffer = ''


    def agregar_error(self,caracter,linea,columna):
        self.listaErrores.append(Error('ERROR LEXICO: Lexema ' + caracter + ' no reconocido en el lenguaje.', linea, columna))
        self.buffer = ''

    #JORNADA 1 TEMPORADA <1996-1997> -f jornada1 Reporte
    def s0(self,caracter : str,cadena):
        '''Estado S0'''
        if caracter.isalpha() or (caracter.isdigit() and cadena[self.i + 1] != None and cadena[self.i + 1] != ' ' and cadena[self.i + 1] != '\n' 
        and cadena[self.i - 1] != None and cadena[self.i - 1].isalpha()) or (caracter.isdigit() and cadena[self.i - 1] != None and cadena[self.i - 1].isalpha()):
            self.estado = 1
            self.buffer += caracter
            self.columna += 1     
        elif caracter.isdigit() :
            self.estado = 4
            self.buffer += caracter
            self.columna += 1               
        elif caracter == '"':
            self.estado = 2
            self.columna += 1     
        elif caracter == '<':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
            self.simbolo = 'menorQue'
        elif caracter == '>':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
            self.simbolo = 'mayorQue'      
        elif caracter == '-' and cadena[self.i + 1] != None and cadena[self.i + 1] == 'n':
            self.estado = 6
            self.buffer += caracter + cadena[self.i + 1]
            self.columna += 1
            self.i += 1
            self.simbolo = '-n'
        elif caracter == '-' and cadena[self.i + 1] != None and cadena[self.i + 1] == 'f':
            self.estado = 6
            self.buffer += caracter + cadena[self.i + 1]
            self.columna += 1
            self.i += 1
            self.simbolo = '-f'
        elif caracter == '-' and cadena[self.i + 1] != None and cadena[self.i + 1] == 'j' and cadena[self.i + 2] != None and cadena[self.i + 2] == 'f':
            self.estado = 6
            self.buffer += caracter + cadena[self.i + 1] + cadena[self.i + 2]
            self.columna += 1
            self.i += 2
            self.simbolo = '-jf'
        elif caracter == '-' and cadena[self.i + 1] != None and cadena[self.i + 1] == 'j' and cadena[self.i + 2] != None and cadena[self.i + 2] == 'i':
            self.estado = 6
            self.buffer += caracter + cadena[self.i + 1] + cadena[self.i + 2]
            self.columna += 1
            self.i += 2
            self.simbolo = '-ji'    
        elif caracter == '-':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
            self.simbolo = 'guion'
        elif caracter== '\n':
            self.linea += 1
            self.columna = 0
        elif caracter in ['\t',' ']:
            self.columna += 1
        elif caracter == '$':
            pass
        else:
            self.agregar_error(caracter,self.linea,self.columna)
            self.columna += 1
            self.estado = 0

    def s1(self,caracter : str, cadena):
        '''Estado S1'''
        if caracter.isalpha() or (caracter.isdigit() and cadena[self.i + 1] != None and cadena[self.i + 1] != ' ' and cadena[self.i + 1] != '\n' 
        and cadena[self.i - 1] != None and cadena[self.i - 1].isalpha()) or (caracter.isdigit() and cadena[self.i - 1] != None and cadena[self.i - 1].isalpha()):
            self.estado = 1
            self.buffer += caracter
            self.columna += 1                                               
        else: 
            if self.buffer in ['RESULTADO','VS','TEMPORADA','JORNADA','GOLES','LOCAL','VISITANTE','TOTAL',
                                'TABLA','PARTIDOS','TOP','ADIOS','-f','-ji','-jf','SUPERIOR','INFERIOR','-n']:
                self.agregar_token(self.buffer,self.linea,self.columna,'reservada_'+self.buffer)    
                self.estado = 0
                self.i -= 1
            else:
                self.agregar_token(self.buffer,self.linea,self.columna,'cadena')
                self.columna += 1
                self.estado = 0
                self.i -= 1

             #RESULTADO "Levante" VS "Español" TEMPORADA <2017-2018>
             #RESULTADO "Real Madrid" VS "Villarreal" TEMPORADA <2019-2020>

    def s2(self,cadena : str):
        '''Estado S2'''
        tmp = int(self.i)
        if cadena[self.i-1] == '"':
            while cadena[tmp] != '"':
                if cadena[tmp] == '\n':
                    self.agregar_error('"'+self.buffer,self.linea,self.columna)
                    self.estado = 0        
                    self.i += tmp-self.i
                    break
                self.buffer += cadena[tmp]
                if tmp+1 < len(cadena):
                    tmp += 1
                    self.columna += 1
                else:
                    continue
        elif cadena[self.i-1] == "'":
            while cadena[tmp] != "'": 
                self.buffer += cadena[tmp]
                if cadena[tmp] == '\n':
                    self.agregar_error("'"+self.buffer,self.linea,self.columna)
                    self.estado = 0        
                    self.i += tmp-self.i
                    break
                if tmp+1 < len(cadena):
                    tmp += 1
                    self.columna += 1
                else:
                    continue
        self.agregar_token(self.buffer,self.linea,self.columna,'cadena')
        self.estado = 0        
        self.i += tmp-self.i



    def s4(self,cadena : str):
        '''Estado S4'''
        tmp = int(self.i)
        if cadena[self.i-1] == '<' or cadena[self.i-1] == '-' or cadena[self.i-1].isdigit():
            while cadena[tmp] != '>' and cadena[tmp] != '-' and cadena[tmp] != ' ' and cadena[tmp] != '\n' and cadena[tmp] != '$':
                if cadena[tmp] == '\n':
                    self.agregar_error('> | -'+self.buffer,self.linea,self.columna)
                    self.estado = 0        
                    self.i += tmp-self.i
                    break
                self.buffer += cadena[tmp]
                if tmp+1 < len(cadena):
                    tmp += 1
                    self.columna += 1
                else:
                    continue
        self.agregar_token(self.buffer,self.linea,self.columna,'numero')
        self.estado = 0        
        self.i += tmp-self.i-1

    def s6(self,cadena : str):
        '''Estado S6'''
        self.agregar_token(self.buffer,self.linea,self.columna,self.simbolo)
        self.estado = 0
        self.i -= 1
        if self.buffer == '<' or self.buffer == '-':
            self.estado = 4

    def analizar(self, cadena):
        cadena = cadena + '$'
        self.listaErrores = []
        self.listaTokens = []
        self.i = 0
        while self.i < len(cadena):
            if self.estado == 0:
                self.s0(cadena[self.i],cadena)
            elif self.estado == 1:
                self.s1(cadena[self.i],cadena)
            elif self.estado == 2:
                self.s2(cadena)
            elif self.estado == 4:
                self.s4(cadena)                   
            elif self.estado == 6:
                self.s6(cadena[self.i])            

            self.i += 1    

    def imprimirTokens(self):
        '''Imprime una tabla con los tokens'''
        x = PrettyTable()
        x.field_names = ["Lexema","Linea","Columna","Tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema, token.linea, token.columna,token.tipo])
        return x.get_html_string()

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x1 = PrettyTable()
        x1.field_names = ["Descripción"]
        for error_ in self.listaErrores:
            x1.add_row([error_.descripcion])
        return x1.get_html_string()