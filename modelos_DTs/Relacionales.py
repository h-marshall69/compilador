'''
Metodo para reconocer si un caracter es Relacional
    @param: caracter a evaluar
    @Return: True si es relacional, False si no
'''
def dt_esRelacional( self, caracter ):
    
    operadores = [ "=", "<", ">", "!" ]
    return self.perteneceLista( caracter, operadores )

'''
Diagrama de Transicion Relacionales
    @Return: diccionario con  token y lexema
            acorde a la respuesta
'''
def dt_relacionales( self, lexema ):

        cont = self.marshall.contador
        
        # Caso ==
        if lexema == '=':

            lexema = lexema + self.marshall.leerCaracter()

            if lexema[ 1 ] == '=' and cont == self.marshall.contador:

                pos = self.marshall.uami.tabla.findSymbol( lexema )

                if pos == -1:
                    pos = self.marshall.uami.tabla.addItem( lexema, self.pr.RELOP)

                return  pos
                        
        
        # Caso !=
        if lexema == '!':

            lexema = lexema + self.marshall.leerCaracter()

            if lexema[ 1 ] == '=' and cont == self.marshall.contador:

                pos = self.marshall.uami.tabla.findSymbol( lexema )

                if pos == -1:
                    pos = self.marshall.uami.tabla.addItem( lexema, self.pr.RELOP)

                return pos
                        
            else: 
                # print "entro del otro lado y voy para alla con el lexema", lexema[0]
                self.marshall.desleer()
                return self.logicos( lexema[0] )

        # Caso >= y >
        elif lexema == '>':

            lexema = lexema + self.marshall.leerCaracter()

            if lexema[ 1 ] == '=' and cont == self.marshall.contador:

                pos = self.marshall.uami.tabla.findSymbol( lexema )

                if pos == -1:
                    pos = self.marshall.uami.tabla.addItem( lexema, self.pr.RELOP)

                return pos
                        

            else:

                pos = self.marshall.uami.tabla.findSymbol( lexema[0] )

                if pos == -1:
                    pos = self.marshall.uami.tabla.addItem( lexema[0], self.pr.RELOP)

                self.marshall.desleer()
                return  pos
                        
        
        # Caso <= y <
        elif lexema == '<':

            lexema = lexema + self.marshall.leerCaracter()

            if lexema[ 1 ] == '=' and cont == self.marshall.contador:

                pos = self.marshall.uami.tabla.findSymbol( lexema )

                if pos == -1:
                    pos = self.marshall.uami.tabla.addItem( lexema, self.pr.RELOP)

                return pos
                        

            else:

                pos = self.marshall.uami.tabla.findSymbol( lexema[0] )

                if pos == -1:
                    pos = self.marshall.uami.tabla.addItem( lexema[0], self.pr.RELOP)

                self.marshall.desleer()
                return  pos
                        