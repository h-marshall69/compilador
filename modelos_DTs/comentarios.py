'''
Metodo para reconocer si un caracter puede ser cadena
    @param: caracter a evaluar
    @Return: True si es una letra, False si no
'''
def dt_esComentario( self, caracter ):
    if caracter == "{":
        return True
    return False

def dt_comentarios( self, lexema ):

    cont = self.marshall.contador

    if lexema == "{":

        caracter = ""
        resto = ""

        while caracter != "}" and cont == self.marshall.contador:
            resto += caracter
            caracter = self.marshall.leerCaracter()

        if cont != self.marshall.contador:

            lexema = lexema + resto
            self.marshall.desleer()

            return {
                        "token": self.pr.ERROR,
                        "lexema": "falto cerrar llave " + lexema
                   }
        else:
            
            # Lexema del comentario
            lexema = lexema + resto + caracter