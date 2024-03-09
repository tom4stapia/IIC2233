from PyQt5.QtCore import QObject, pyqtSignal

class LogicaRanking(QObject):

    senal_abrir_ranking = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def ordenar_ranking(self, puntajes):
        ranking_desorden = []
        with open(puntajes, "r") as archivo:
            for linea in archivo:
                ranking_desorden.append(linea.strip("\n").split(","))
        for i in range(len(ranking_desorden)):
            ranking_desorden[i][1] = int(ranking_desorden[i][1])
        ranking_oficial = sorted(ranking_desorden, key=self.orden, reverse=True)
        self.senal_abrir_ranking.emit(ranking_oficial[:5])
        

    def orden(self, lista):
        return lista[1]