import parametros as p
from PyQt5 import uic
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, QTimer, Qt
from PyQt5.QtGui import QPixmap
from backend.elementos_juego import Bloque

window_name, base_class = uic.loadUiType(p.RUTA_VENTANA_JUEGO)


class VentanaJuego(window_name, base_class):

    senal_compra_girasol = pyqtSignal(object)
    senal_compra_plantac = pyqtSignal(object)
    senal_compra_plantaa = pyqtSignal(object)
    senal_compra_papa = pyqtSignal(object)
    senal_empezar = pyqtSignal()
    senal_crear_zombies = pyqtSignal()
    senal_sumar_soles = pyqtSignal()
    senal_mover_bala = pyqtSignal(object)
    senal_empezar_planta = pyqtSignal(object)
    senal_pausar = pyqtSignal()
    senal_reanudar = pyqtSignal()
    senal_reiniciar = pyqtSignal()
    senal_abrir_ventana_post = pyqtSignal()
    senal_creacion_zombies = pyqtSignal()
    senal_salir_juego = pyqtSignal()
    senal_avanzar_ronda = pyqtSignal()
    senal_tecla = pyqtSignal(str)
    senal_empezar_ronda = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_apretado = False
        self.bloque_seleccionado = None
        self.pausa = False
        self.empezo = False
        self.termino = False
        self.soles = []
        self.labels_creados = []
        self.crear_bloques()
        self.label_pierde.hide()
        self.label_ruz_ganador.hide()
        self.label_ganador.hide()
        self.label_error.hide()
        self.boton_girasol.clicked.connect(self.comprar_girasol)
        self.boton_planta_clasica.clicked.connect(self.comprar_planta_clasica)
        self.boton_planta_azul.clicked.connect(self.comprar_planta_azul)
        self.boton_patata.clicked.connect(self.comprar_papa)
        self.boton_inicio.clicked.connect(self.empezar_timers)
        self.boton_pausa.clicked.connect(self.pausar_juego)
        self.boton_avanzar.clicked.connect(self.avanzar_ronda)
        self.boton_salir.clicked.connect(self.salir)
        self.timer_fin_ronda = QTimer()
        self.timer_error_compra = QTimer()
        self.configurar_timer()
    
    def configurar_timer(self):
        self.timer_fin_ronda.setInterval(p.INTERVALO_FIN_RONDA)
        self.timer_fin_ronda.timeout.connect(self.cerrar_ventana)
        self.timer_fin_ronda.setSingleShot(True)
        self.timer_error_compra.setInterval(p.INTERVALO_FIN_RONDA)
        self.timer_error_compra.timeout.connect(self.mensaje_error)
        self.timer_error_compra.setSingleShot(True)
    
    def mostrar_ventana(self, fondo):
        self.label_fondo.setPixmap(QPixmap(fondo))
        self.show()
    
    def paso_de_ronda(self):
        self.senal_empezar_ronda.emit()
        self.show()

    def gana_ronda(self):
        self.termino = True
        self.label_ruz.hide()
        self.label_ruz_ganador.raise_()
        self.label_ganador.raise_()
        self.label_ruz_ganador.show()
        self.label_ganador.show()
        self.timer_fin_ronda.start()
    
    def pierde_ronda(self):
        self.termino = True
        self.label_pierde.raise_()
        self.label_pierde.show()
        self.timer_fin_ronda.start()
    
    def cerrar_ventana(self):
        self.hide()
        self.senal_abrir_ventana_post.emit()
        for i in range(len(self.labels_creados)):
            self.labels_creados[i].hide()
        self.label_ruz_ganador.hide()
        self.label_ganador.hide()
        self.label_pierde.hide()
        self.labels_creados = []
        self.senal_reiniciar.emit()
        self.empezo = False
        self.termino = False

    def salir(self):
        self.senal_salir_juego.emit()

    def avanzar_ronda(self):
        self.senal_avanzar_ronda.emit()

    def pausar_juego(self):
        if self.empezo:
            if self.pausa:
                self.senal_reanudar.emit()
                self.pausa = False
            else:
                self.pausa = True
                self.senal_pausar.emit()

    def setear_datos(self, datos: dict):
        self.label_soles.setText(datos['Soles'])
        self.label_puntaje.setText(datos['Puntaje'])
        self.label_nivel.setText(datos['Nivel'])
        self.label_zombies_r.setText(datos['Zombies restantes'])
        self.label_zombies_d.setText(datos['Zombies destruidos'])

    def mousePressEvent(self, event):
        if self.pausa is False and self.termino is False:
            if event.button() == Qt.LeftButton:
                for bloque in self.bloques:
                    if self.bloques[bloque].posicion[0][0] <= event.x() <= \
                        self.bloques[bloque].posicion[0][1]:
                        if self.bloques[bloque].posicion[1][0] <= event.y() <= \
                            self.bloques[bloque].posicion[1][1]:
                            if self.boton_apretado is not False:
                                self.bloque_seleccionado = self.bloques[bloque]
                                if self.boton_apretado == "girasol":
                                    self.senal_compra_girasol.emit(self.bloque_seleccionado)
                                elif self.boton_apretado == "planta clasica":
                                    self.senal_compra_plantac.emit(self.bloque_seleccionado)
                                elif self.boton_apretado == "planta azul":
                                    self.senal_compra_plantaa.emit(self.bloque_seleccionado)
                                else:
                                    self.senal_compra_papa.emit(self.bloque_seleccionado)
                            self.boton_apretado = False
        if event.button() == Qt.RightButton:
            for sol in self.soles:
                if sol[0] <= event.x() <= (sol[0] + p.ANCHO_SOL) and \
                    sol[1] <= event.y() <= (sol[1] + p.LARGO_SOL):
                    sol[2].hide()
                    self.soles.remove(sol)
                    self.senal_sumar_soles.emit()

    def empezar_timers(self):
        if self.pausa is False and self.empezo is False:
            self.senal_empezar.emit()
            self.senal_creacion_zombies.emit()
            self.empezo = True

    def crear_bloques(self):
        self.bloques = {
            1: Bloque([(352, 407), (125, 218)]),
            2: Bloque([(407, 467), (125, 218)]),
            3: Bloque([(467, 525), (125, 218)]),
            4: Bloque([(525, 584), (125, 218)]),
            5: Bloque([(584, 642), (125, 218)]),
            6: Bloque([(642, 701), (125, 218)]),
            7: Bloque([(701, 760), (125, 218)]),
            8: Bloque([(760, 818), (125, 218)]),
            9: Bloque([(818, 877), (125, 218)]),
            10: Bloque([(877, 934), (125, 218)]),
            11: Bloque([(352, 407), (218, 310)]),
            12: Bloque([(407, 467), (218, 310)]),
            13: Bloque([(467, 525), (218, 310)]),
            14: Bloque([(525, 584), (218, 310)]),
            15: Bloque([(584, 642), (218, 310)]),
            16: Bloque([(642, 701), (218, 310)]),
            17: Bloque([(701, 760), (218, 310)]),
            18: Bloque([(760, 818), (218, 310)]),
            19: Bloque([(818, 877), (218, 310)]),
            20: Bloque([(877, 934), (218, 310)])
        }

    def comprar_girasol(self):
        self.boton_apretado = "girasol"

    def comprar_planta_clasica(self):
        self.boton_apretado = "planta clasica"

    def comprar_planta_azul(self):
        self.boton_apretado = "planta azul"
    
    def comprar_papa(self):
        self.boton_apretado = "papa"
    
    def compra_exitosa(self, exito, bloque, error):
        if exito is True:
            self.planta = QLabel(self)
            bloque.planta.label = self.planta
            self.labels_creados.append(self.planta)
            self.planta.setPixmap(QPixmap(bloque.planta.imagenes[0]))
            self.planta.setScaledContents(True)
            self.planta.setGeometry(bloque.posicion[0][0]+p.DESPLAZAMIENTO_PLANTA,
                                    bloque.posicion[1][0]+p.DESPLAZAMIENTO_PLANTA,
                                    p.ANCHO_PLANTA, p.LARGO_PLANTA)
            self.planta.show()
            if self.empezo is True and self.pausa is False:
                self.senal_empezar_planta.emit(bloque.planta)
        else:
            self.label_error.setText(error)
            self.label_error.show()
            self.timer_error_compra.start()
    
    def mensaje_error(self):
        self.label_error.hide()

    def aparece_bala(self, bala):
        self.b = QLabel(self)
        self.b.setScaledContents(True)
        bala.label = self.b
        self.labels_creados.append(self.b)
        self.b.setPixmap(QPixmap(bala.imagenes[0]))
        self.b.setGeometry(bala.x, bala.y, bala.ancho, bala.largo)
        self.b.show()
        bala.aparecio = True    

    def aparece_zombie(self, zombie):
        self.z = QLabel(self)
        self.z.setScaledContents(True)
        self.labels_creados.append(self.z)
        zombie.label = self.z
        self.z.setGeometry(zombie.x, zombie.y, zombie.ancho, zombie.largo)
        zombie.timer_mover.start()
        self.z.show()
  
    def aparece_sol(self, x, y, imagen):
        self.sol = QLabel(self)
        self.soles.append((x, y, self.sol))
        self.labels_creados.append(self.sol)
        self.sol.setScaledContents(True)
        self.sol.setGeometry(x, y, p.ANCHO_SOL, p.LARGO_SOL)
        self.sol.setPixmap(imagen)
        self.sol.show()

    def keyPressEvent(self, event):
        self.senal_tecla.emit(event.text().lower())
        if event.text().lower() == "p":
            self.pausar_juego()