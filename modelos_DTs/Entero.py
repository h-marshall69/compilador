'''
Metodo para reconocer si un caracter es un digito
    @param: caracter a evaluar
    @Return: True si es digito, False si no
'''
def dt_esDigito( self, caracter ):

    digitos = list( range(0,10) )
    return self.perteneceLista(caracter, digitos)


'''
Diagrama de Transicion Entero
    @Return: diccionario con  token y lexema
                acorde a la respuesta
'''
def dt_Entero(self, lexema):

        cont = self.marshall.contador

        if self.esDigito( lexema ):
            # Empieza en cero
            if lexema == "0":
                lexema += self.marshall.leerCaracter()
                # Segundo caracter es "otro"
                # Return entero cero
                if self.esDigito( lexema[1] ) == False:

                    pos = self.marshall.uami.tabla.findSymbol( lexema[0] )
                    if pos == -1:
                        pos = self.marshall.uami.tabla.addItem( lexema, self.pr.NUM_ENT)

                    self.marshall.desleer()
                    return pos
                        
                # Segundo caracter es un digito
                else:
                    # Se lee todo el numero entero para regresarlo como error y lexema
                    digito = self.marshall.leerCaracter()
                    while self.esDigito( digito ) and cont == self.marshall.contador:
                        lexema += digito
                        digito = self.marshall.leerCaracter()
                        
                    self.marshall.desleer()
                    return {
                            "token": self.pr.ERROR,
                            "lexema": lexema
                        }
            # No empieza en cero
            else:
                # lee todo el numero y lo regresa como entero
                digito = lexema
                lexema = ""
                while self.esDigito( digito ) and cont == self.marshall.contador:
                    lexema += digito
                    digito = self.marshall.leerCaracter()

                pos = self.marshall.uami.tabla.findSymbol( lexema )

                if pos == -1:
                    pos = self.marshall.uami.tabla.addItem( lexema, self.pr.NUM_ENT)

                self.marshall.desleer()
                return pos
                        