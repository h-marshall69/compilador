import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QFileDialog, QMessageBox, QTextEdit, QLabel, QApplication
from PyQt5 import QtGui
from presentacion.Uami import Uami

class Ventana(QMainWindow):

    # Creamos una subclase de QWidget para nuestra ventana
    def __init__(self):
        super().__init__()

        # Direccion Url del archivo fuente
        self.fuenteUrl = ""

        # Configuracion de la ventana
        self.setWindowTitle('Mi Ventana')  # Establecemos el título de la ventana
        self.setGeometry(250, 50, 880, 670)  # Establecemos la posición y el tamaño de la ventana
        self.setWindowTitle("Marshall") # Titulo de La ventana
        self.setWindowIcon(QtGui.QIcon("img/logo.png"))

        # Evento para abrir los archivos
        self.EventoAbrirLocal = QAction(QtGui.QIcon("img/logo.png"), 'Abrir un archivo', self)
        self.EventoAbrirLocal.setShortcut("Ctrl+O")
        self.EventoAbrirLocal.triggered.connect(self.abrirArchivo)

        # Evento Salir
        self.EventoSalir = QAction(QtGui.QIcon("img/salir.png"), "Salir del Programa", self)
        self.EventoSalir.setShortcut("Ctrl+Q")
        self.EventoSalir.setStatusTip('Salir de la aplicaion')
        self.EventoSalir.triggered.connect(self.cierraAplicacion)

        # Evento Save
        self.EventoSave = QAction(QtGui.QIcon("img/save.png"), "Guardar", self);
        self.EventoSave.setShortcut("Ctrl+g")
        self.EventoSave.setStatusTip('Guardar archivo fuente')
        self.EventoSave.triggered.connect(self.guardarArchivo)

        # Evento SaveAs
        self.EventoSaveAs = QAction(QtGui.QIcon("img/saveAs.png"), "Guardar como", self);
        self.EventoSaveAs.setShortcut("Ctrl+s")
        self.EventoSaveAs.setStatusTip('Guardar como el archivo fuente')
        self.EventoSaveAs.triggered.connect(self.guardarArchivoAs)

        # Evento para compilar
        self.EventoCompilar = QAction(QtGui.QIcon("img/comp.png"), 'compilar', self)
        self.EventoCompilar.setShortcut("Ctrl+R")
        self.EventoCompilar.setStatusTip('Iniciar la compilacion')
        self.EventoCompilar.triggered.connect(self.iniciarCompilacion)

        # Configuracion del Menu Principal
        self.MenuPrincipal = self.menuBar()

        # Se crea el menu archivo y se agregan los eventos
        self.MenuArchivo = self.MenuPrincipal.addMenu('&Archivo')
        self.MenuArchivo.addAction(self.EventoSalir)
        self.MenuArchivo.addAction(self.EventoCompilar)
        self.MenuArchivo.addAction(self.EventoAbrirLocal)
        self.MenuArchivo.addAction(self.EventoSave)
        self.MenuArchivo.addAction(self.EventoSaveAs)

        # Se crea el Toolbar y se agregan los eventos
        self.ToolBar = self.addToolBar("Archivo")
        self.ToolBar.addAction(self.EventoAbrirLocal)
        self.ToolBar.addAction(self.EventoSalir)
        self.ToolBar.addAction(self.EventoCompilar)
        self.ToolBar.addAction(self.EventoSave)
        self.ToolBar.addAction(self.EventoSaveAs)
        self.ToolBar.addAction(self.EventoAbrirLocal)

        self.diseno()

    '''
    LLenado y ubicaion de los componentes
    en la ventana
    '''
    def diseno(self):

        # Caja de texto (text Areas)
        self.txtAreaFuente = QTextEdit(self)
        self.txtAreaFuente.setGeometry(10, 85, 425, 270)

        self.txtAreaObjeto = QTextEdit(self)
        self.txtAreaObjeto.setGeometry(880, 85, 390, 565)

        self.txtAreaFileError = QTextEdit(self)
        self.txtAreaFileError.setGeometry(10, 380, 425, 270)

        self.txtAreaResultado = QTextEdit(self)
        self.txtAreaResultado.setGeometry(445, 380, 425, 270)

        self.txtAreaFileTupla = QTextEdit(self)
        self.txtAreaFileTupla.setGeometry(445, 85, 425, 270)

        # Etiquetas (Labels)
        self.lbl_Fuente = QLabel("CONTENIDO DEL ARCHIVO FUENTE: ", self)
        self.lbl_Fuente.setGeometry(80, 40, 300, 60)
        self.lbl_Fuente.setFont(QtGui.QFont('SansSerif', 11))

        self.lbl_Objeto = QLabel("CONTENIDO DEL ARCHIVO OBJETO: ", self)
        self.lbl_Objeto.setGeometry(970, 40, 300, 60)
        self.lbl_Objeto.setFont(QtGui.QFont('SansSerif', 11))

        self.lbl_fileError = QLabel("CONTENIDO DEL ARCHIVO ERROR: ", self)
        self.lbl_fileError.setGeometry(80, 335, 300, 60)
        self.lbl_fileError.setFont(QtGui.QFont('SansSerif', 11))

        self.lbl_compilacion = QLabel("RESULTADO DE LA COMPILACION: ", self)
        self.lbl_compilacion.setGeometry(550, 335, 300, 60)
        self.lbl_compilacion.setFont(QtGui.QFont('SansSerif', 11))

        self.lbl_fileTupla = QLabel("CONTENIDO DEL ARCHIVO TUPLA: ", self)
        self.lbl_fileTupla.setGeometry(550, 40, 300, 60)
        self.lbl_fileTupla.setFont(QtGui.QFont('SansSerif', 11))
        self.show()

    '''
    Mtodo para salir de la aplicaion
    ya sea por el toolbar, menu o shortcut
    '''
    def cierraAplicacion(self):
        opcion = QMessageBox.question(self, 'Salir de la Aplicaion', 'Estas seguro de salir', QMessageBox.Yes | QMessageBox.No)
        if opcion == QMessageBox.Yes:
            sys.exit()
        else:
            pass
    
    '''
    Metodo para abrir el archivo fuente
    mediante el dialogo de python
    '''
    def abrirArchivo(self):
            
        urlActual = self.fuenteUrl

        # Direccion del archivo SElecionado en el Dialogo de python
        self.fuenteUrl = QFileDialog.getOpenFileName(self, 'Open File', filter='*.fte')

        # Si se selecciono algun archivo en el dialogo
        # se imprime el contenido en la caja de texto
        # del archivo fuente
        if self.fuenteUrl:
            archivo = open(self.fuenteUrl[0], "r")
            self.txtAreaFuente.setText(archivo.read())
            archivo.close()
        else:
            self.fuenteUrl = urlActual

    '''
    Metodo para guardar el archivo fuente
    ya sea por el toolbar, menu o shortcut
    '''
    def guardarArchivo(self):

        # Guarda archivos ya existe
        if self.fuenteUrl:
            archivo = open(self.fuenteUrl[0], "w")
            texto = self.txtAreaFuente.toPlainText()
            archivo.write(texto)
            archivo.close()

        # Guardar como si no existe el archivo
        else:
            url = str(QFileDialog.getSaveFileName(self, 'Save As File', filter="*.fte"))

            if url:
                # Si no termina en .fte
                if url.endswith(".fte") == False:
                    pos_ini = url.find(".")
                    pos_final = len(url)
                    url = url.replace(url[pos_ini:pos_final], ".fte")

                archivo = open(url, "w")
                texto = self.txtAreaFuente.toPlainText()
                archivo.write(texto)
                archivo.close()
                self.fuenteUrl = url

    '''
    Metodo para guardar el archivo fuente
    ya sea por el toolbar, menu o shortcut
    '''
    def guardarArchivoAs(self):

        # urlActual = self.fuenteUrl
        url, _ = QFileDialog.getSaveFileName(self, 'Save As File', filter="*.fte")
        if url:
            # Si no termina en .fte
            if url.endswith(".fte") == False:
                pos_ini = url.find(".")
                pos_final = len(url)
                url = url.replace(url[pos_ini:pos_final], ".fte")
            
            archivo = open(url, 'w')
            texto = self.txtAreaFuente.toPlainText()
            archivo.write(texto)
            archivo.close()

            self.fuenteUrl = url

            # if urlActual:
            #     self.fuenteUrl = urlActual
            # else:
            #     self.fuenteUrl = url
    
    def escribirAreaFuente(self, texto):
        self.txtAreaFuente.setText(texto)

    def getTextAreaFuente( self ):
        return self.txtAreaFuente.toPlainText()
    
    def escribirAreaResultado( self, texto ):
        self.txtAreaResultado.setText( texto )
    
    def getTextAreaResultado( self ):
        return self.txtAreaResultado.toPlainText()


    def escribirAreaErrores( self, texto ):
        self.txtAreaFileError.setText( texto )
    
    def getTextAreaErrores( self ):
        return self.txtAreaFileError.toPlainText()
        
    
    def escribirAreaTupla( self, texto ):
        self.txtAreaFileTupla.setText( texto )
    
    def getTextAreaTupla( self ):
        return self.txtAreaFileTupla.toPlainText()

    def escribirAreaObjeto( self, texto ):
        self.txtAreaObjeto.setText( texto )

    def getTextAreaObjeto( self ):
        return self.txtAreaObjeto.toPlainText()

    '''
    Metodo que inicia la compilacion
    en la ventana
    '''
    def iniciarCompilacion(self):
        uami = Uami(self)
        uami.iniciaCompilacion()