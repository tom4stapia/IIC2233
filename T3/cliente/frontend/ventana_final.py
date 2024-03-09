import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from cripto import data_json
import os


ruta = os.path.join(data_json("RUTA_VENTANA_FINAL")[0],
data_json("RUTA_VENTANA_FINAL")[1], data_json("RUTA_VENTANA_FINAL")[2])

window_name, base_class = uic.loadUiType(ruta)

class VentanaFinal(window_name, base_class):
    senal_cerrar_ventana = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton.clicked.connect(self.pasar_ventana)
    
    def pasar_ventana(self):
        self.hide()
        self.senal_cerrar_ventana.emit()
    
    def mostrar_ventana(self):
        self.show()

    def salir(self):
        sys.exit()