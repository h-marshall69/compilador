'''
Metodo para reconocer si un caracter es Logico
    @param: caracter a evaluar
    @Return: True si es logico, False si no
'''
def dt_esLogico( self, caracter ):
    
    operadores = [ "&", "|", "!" ]
    return self.perteneceLista( caracter, operadores )


'''
Diagrama de Transicion Logicos
    @Return: diccionario con  token y lexema
            acorde a la respuesta
'''
def dt_logicos( self, lexema ):

        cont = self.marshall.contador

        # Negacion
        if lexema == '!':

            if self.marshall.leerCaracter() != "=" or self.marshall.contador == cont:

                pos = self.marshall.uami.tabla.findSymbol( lexema )

                if pos == -1:
                    pos = self.marshall.uami.tabla.addItem( lexema, self.pr.LOGOP)

                self.marshall.desleer()
                
                return pos
                    
                    
        
        # Caso And 
        elif lexema == '&':

            lexema = lexema + self.marshall.leerCaracter()

            if lexema[ 1 ] == '&':

                # misma linea
                if cont == self.marshall.contador:
                    
                    pos = self.marshall.uami.tabla.findSymbol( lexema )

                    if pos == -1:
                        pos = self.marshall.uami.tabla.addItem( lexema, self.pr.LOGOP)

                    return pos
                        

                else:
                    self.marshall.desleer()
                    return {
                            "token": self.pr.ERROR,
                            "lexema": lexema[0]
                        }

            else:
                self.marshall.desleer()
                return {
                            "token": self.pr.ERROR,
                            "lexema": lexema[0]
                        }
        
        # Caso Or 
        elif lexema == '|':

            lexema = lexema + self.marshall.leerCaracter()

            if lexema[ 1 ] == '|':

                # misma linea
                if cont == self.marshall.contador:

                    pos = self.marshall.uami.tabla.findSymbol( lexema )

                    if pos == -1:
                        pos = self.marshall.uami.tabla.addItem( lexema, self.pr.LOGOP)

                    return pos
                        

                else:
                    self.marshall.desleer()
                    return {
                            "token": self.pr.ERROR,
                            "lexema": lexema[0]
                        }
                          
            else:
                self.marshall.desleer()
                return {
                            "token": self.pr.ERROR,
                            "lexema": lexema[0]
                        }