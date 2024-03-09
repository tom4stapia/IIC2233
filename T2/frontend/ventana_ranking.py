from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_VENTANA_RANKING)


class Ranking(window_name, base_class):

    senal_ranking_revisado = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.boton_volver.clicked.connect(self.volver)

    def actualizar_ranking(self, puntajes):
        # COMO MANTENER FORMATO
        self.posicion1.setText(puntajes[0][0])
        self.posicion2.setText(puntajes[1][0])
        self.posicion3.setText(puntajes[2][0])
        self.posicion4.setText(puntajes[3][0])
        self.posicion5.setText(puntajes[4][0])
        self.puntaje1.setText(str(puntajes[0][1]))
        self.puntaje2.setText(str(puntajes[1][1]))
        self.puntaje3.setText(str(puntajes[2][1]))
        self.puntaje4.setText(str(puntajes[3][1]))
        self.puntaje5.setText(str(puntajes[4][1]))
        self.mostrar_ranking()

    def mostrar_ranking(self):
        self.show()

    def volver(self):
        self.senal_ranking_revisado.emit()
        self.hide()
