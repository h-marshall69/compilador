import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

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
        self.EventoAbrirLocal = QAction(QtGui.QIcon("img/open.png"), 'Abrir un archivo', self)
        self.EventoAbrirLocal.setShortcut("Ctrl+O")
        self.EventoAbrirLocal.triggered.connect(self.abrirArchivo)

        # Evento Salir
        self.EventoSalir = QAction(QtGui.QIcon("img/salir.png"), "Salir del Programa", self)

    '''
    Metodo para abrir el archivo fuente
    mediante el dialogo de python
    '''
    def abrirArchivo(self):
            
        urlActual = self.fuenteUrl

        # Direccion del archivo SElecionado en el Dialogo de python
        self.fuenteUrl = QFileDialog.getOpenFileName(self, 'Open File', filter='*.ql')

        # Si se selecciono algun archivo en el dialogo
        # se imprime el contenido en la caja de texto
        # del archivo fuente
        if self.fuenteUrl:
            archivo = open(self.fuenteUrl, 'r')
            self.txtAreaFuente.setText(archivo.read())
            archivo.close()
        else:
            self.fuenteUrl = urlActual



        

