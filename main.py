# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from ventana import *
import sys, var, events


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        var.ui=Ui_VenPrincipal()
        var.ui.setupUi(self)

        '''
        CONEXIÓN CON LOS EVENTOS
        '''

        #CODIGO DE CONEXIÓN DE LOS EVENTOS
        '''
        BOTONES
        '''
        #var.ui.btnAceptar.clicked.connect(events.Eventos.Saludo)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.btnSalir.clicked.connect(events.eventos.Salir)

        '''
        CONTROLES DEL MENUBAR
        '''
if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    window=Main()
    window.show()
    sys.exit(app.exec())