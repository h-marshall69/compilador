import sys
from PyQt5.QtWidgets import QApplication, QWidget
from presentacion.marshall import Ventana

# Comandos para iniciar la Ventana
if __name__ == '__main__':
    # Creamos una instancia de QApplication
    app = QApplication(sys.argv)

    # Creamos una instancia de nuestra ventana
    ventana = Ventana()

    # Mostramos la ventana
    ventana.show()

    # Iniciamos el ciclo de eventos de la aplicación
    sys.exit(app.exec_())