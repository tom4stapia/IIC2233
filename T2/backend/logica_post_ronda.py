from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p

class LogicaPostRonda(QObject):

    senal_continuar_juego = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def comprobar_ronda(self, bool):
        if bool:
            self.senal_continuar_juego.emit(True)
        else:
            self.senal_continuar_juego.emit(False)
    
    def recibir_usuario(self, usuario):
        self.usuario = usuario
        
    def agregar_ranking(self, puntaje_total):
        with open(p.RUTA_PUNTAJES, "a") as archivo:
            archivo.write(self.usuario+","+str(puntaje_total)+"\n")   

