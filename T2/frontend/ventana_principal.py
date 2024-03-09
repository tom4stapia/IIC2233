import parametros as p
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType(p.RUTA_VENTANA_PRINCIPAL)


class VentanaPrincipal(window_name, base_class):
    senal_ventana_juego = pyqtSignal(str)
    senal_datos = pyqtSignal(int, str, int, bool)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_error.hide()
        self.boton.clicked.connect(self.apreto)

    def apreto(self):
        if self.boton_salida.isChecked():
            self.hide()
            self.senal_ventana_juego.emit(p.IMG_OSCURO)
            self.senal_datos.emit(p.SOLES_POR_RECOLECCION, str(p.PONDERADOR_NOCTURNO), 
                                  p.PUNTAJE_ZOMBIE_NOCTURNO, False)
            self.label_error.hide()
   
        elif self.boton_jardin.isChecked():
            self.hide()
            self.senal_ventana_juego.emit(p.IMG_JARDIN)
            self.senal_datos.emit(p.SOLES_POR_RECOLECCION*2, str(p.PONDERADOR_DIURNO),
                                  p.PUNTAJE_ZOMBIE_DIURNO, True)
            self.label_error.hide()
        else:
            self.label_error.show()

    def mostrar_ventana(self):
        self.show()
