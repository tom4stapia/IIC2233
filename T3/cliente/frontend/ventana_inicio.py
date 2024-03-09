import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from cripto import data_json
import os


ruta = os.path.join(data_json("RUTA_VENTANA_INICIO")[0],
data_json("RUTA_VENTANA_INICIO")[1], data_json("RUTA_VENTANA_INICIO")[2])

window_name, base_class = uic.loadUiType(ruta)

class VentanaInicio(window_name, base_class):
    senal_enviar_login = pyqtSignal(dict)
    senal_pasar_ventana = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.usuario.setText("")
        self.usuario.setPlaceholderText("Ingresa tu nombre...")
        self.boton_usuario.clicked.connect(self.enviar_login)
    
    def enviar_login(self):
        """Cuando se apreta el botón de enviar o se apreta enter"""
        nombre_usuario = self.usuario.text()
        diccionario = {
            "comando": "validar_login",
            "nombre usuario": nombre_usuario,
        }
        self.senal_enviar_login.emit(diccionario)
        self.pasar_ventana()
    
    def pasar_ventana(self):
        self.hide()
        self.senal_pasar_ventana.emit()
    
    def recibir_validacion(self, valid):
        pass

    def mostrar_ventana(self):
        self.show()

    def ver_ranking(self):
        pass

    def salir(self):
        sys.exit()