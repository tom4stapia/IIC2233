from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_VENTANA_POST_RONDA)


class VentanaPostJuego(window_name, base_class):

    senal_pasar_ronda = pyqtSignal(bool)
    senal_pasar = pyqtSignal()
    senal_salir = pyqtSignal()
    senal_agregar_ranking = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_seguir.clicked.connect(self.verificar_ronda)

    def actualizar_datos(self, datos, bool):
        # COMO MANTENER FORMATO
        self.label_ronda.setText(datos["Nivel"])
        self.label_soles.setText(datos["Soles"])
        self.label_puntaje.setText(datos["Puntaje"])
        self.label_puntaje_total.setText(str(int(float(datos["Puntaje total"]))))
        self.label_zombies.setText(datos["Zombies destruidos"])
        self.continuar = bool
        self.datos = datos
        if bool:
            self.label_gano.show()
            self.label_perdio.hide()
        else:
            self.label_perdio.show()
            self.label_gano.hide()

    def mostrar_datos(self):
        self.show()

    def verificar_ronda(self):
        self.senal_pasar_ronda.emit(self.continuar)

    def recibir_validacion(self, bool):
        if bool:
            self.hide()
            self.senal_pasar.emit()

    def salir(self):
        self.hide()
        self.senal_agregar_ranking.emit(int(float(self.datos["Puntaje total"])))
        self.senal_salir.emit()
