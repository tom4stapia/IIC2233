import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
import parametros as p


window_name, base_class = uic.loadUiType(p.RUTA_VENTANA_INICIO)


class VentanaInicio(window_name, base_class):

    senal_enviar_login = pyqtSignal(str)
    senal_ordenar_ranking = pyqtSignal(str)
    senal_abrir_ventanap = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.usuario.setText("")
        self.usuario.setPlaceholderText("Introduzca usuario")
        self.boton_jugar.clicked.connect(self.verificar_login)
        self.boton_ranking.clicked.connect(self.ver_ranking)
        self.boton_salir.clicked.connect(self.salir)
    
    def verificar_login(self):
        self.senal_enviar_login.emit(self.usuario.text())
    
    def recibir_validacion(self, valid, error):
        if valid is True:
            self.hide()
            self.senal_abrir_ventanap.emit()
            self.usuario.setText("")
            self.usuario.setPlaceholderText("Introduzca usuario")
        else:
            self.usuario.setText("")
            self.usuario.setPlaceholderText(f"Introduzca usuario válido. Error: {error}")

    def mostrar_ventana(self):
        self.show()

    def ver_ranking(self):
        self.hide()
        self.senal_ordenar_ranking.emit(p.RUTA_PUNTAJES)

    def salir(self):
        sys.exit()
    