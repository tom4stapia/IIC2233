from PyQt5.QtCore import pyqtSignal, QTimer
from cripto import data_json
import os
import sys
from PyQt5 import uic

ruta = os.path.join(data_json("RUTA_VENTANA_ESPERA")[0],
data_json("RUTA_VENTANA_ESPERA")[1], data_json("RUTA_VENTANA_ESPERA")[2])

window_name, base_class = uic.loadUiType(ruta)


class VentanaEspera(window_name, base_class):
    senal_volver_inicio = pyqtSignal()
    senal_pasar = pyqtSignal()


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.volver.clicked.connect(self.volver_ventana)
        self.tiempo.setText(str(data_json("CUENTA_REGRESIVA_INICIO")))
        self.cuenta = int(data_json("CUENTA_REGRESIVA_INICIO"))
        self.timer = QTimer()
        self.configurar_timer()

    def configurar_timer(self):
        self.timer.setInterval(data_json("UN SEGUNDO"))
        self.timer.timeout.connect(self.actualizar_labels)

    def actualizar_labels(self):
        if self.cuenta > 0:
            self.cuenta -= 1
            self.tiempo.setText(str(self.cuenta))
        else:
            self.hide()
            self.timer.stop()
            self.tiempo.setText(str(data_json("CUENTA_REGRESIVA_INICIO")))
            self.cuenta = int(data_json("CUENTA_REGRESIVA_INICIO"))
            self.senal_pasar.emit()

    def volver_ventana(self):
        self.hide()
        self.tiempo.setText(str(data_json("CUENTA_REGRESIVA_INICIO")))
        self.cuenta = int(data_json("CUENTA_REGRESIVA_INICIO"))
        self.timer.stop()
        self.senal_volver_inicio.emit()
    
    def mostrar_ventana(self):
        self.show()
        self.timer.start()