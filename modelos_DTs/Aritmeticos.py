'''
Metodo para reconocer si un caracter es Aritmetico
   @param: caracter a evaluar
   @Return: True si es aritmetico, False si no
'''
def dt_esAritmetico( self, caracter ):
    operadores = [ "=", "-", "+", "/", "*", "%" ]
    return self.perteneceLista( caracter, operadores )

'''
Diagrama de Transicion Aritmeticos
    @Return: diccionario con  token y lexema
                acorde a la respuesta
'''
def dt_aritmeticos(self, lexema):

        cont = self.marshall.contador
        pos = self.marshall.uami.tabla.findSymbol(lexema)
    
        # Asignacion
        if lexema  == "=":
            if self.marshall.leerCaracter() != "=" or self.marshall.contador != cont:
                if pos == -1:
                    pos = self.marshall.uami.tabla.addItem(lexema, self.pr.ASIGNACION)

                self.marshall.desleer()
                
                return pos
                        
            else:
                self.marshall.desleer()
                return self.relacionales( lexema )

        # Suma
        elif lexema == '+':
            if pos == -1:
                pos = self.marshall.uami.tabla.addItem(lexema, self.pr.ADDOP)
            return pos
                    
        # Resta
        elif lexema == '-':
            if pos == -1:
                pos = self.marshall.uami.tabla.addItem(lexema, self.pr.ADDOP)
            return pos
                    
        # DIVISION
        elif lexema == '/':
            if pos == -1:
                pos = self.marshall.uami.tabla.addItem(lexema, self.pr.MULOP)
            return pos
                    
        # Multiplicacion
        elif lexema == '*':
            if pos == -1:
                pos = self.marshall.uami.tabla.addItem(lexema, self.pr.MULOP)
            return pos
                    
        # MODULO
        elif lexema == '%':
            if pos == -1:
                pos = self.marshall.uami.tabla.addItem(lexema, self.pr.MODULO)
            return pos
                    