from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
import parametros as p
from random import randint


class Girasol():

    def __init__(self):
        self.vida = p.VIDA_PLANTA
        self.soles = p.CANTIDAD_SOLES
        self.posicion = None
        self.tipo = "girasol"
        self.label = None
        self.soles_creados = []
        self.timer_crear_soles = QTimer()
        self.timer_animacion = QTimer()
        self.imagenes = [p.IMG_GIRASOL_1, p.IMG_GIRASOL_2]
        self.n_imagen = 0
        self.crear_timers()

    def crear_timers(self):
        self.timer_crear_soles.setInterval(p.INTERVALO_SOLES_GIRASOL)
        self.timer_crear_soles.timeout.connect(self.crear_soles)
        self.timer_animacion.setInterval(p.INTERVALO_APARICION_SOLES)
        self.timer_animacion.timeout.connect(self.animacion)
    
    def correr_timers(self):
        self.timer_crear_soles.start()
        self.timer_animacion.start()
    
    def crear_soles(self):
        for _ in range(self.soles):
            x = randint(self.posicion[0][0], self.posicion[0][1] - p.ANCHO_SOL)
            y = randint(self.posicion[1][0], self.posicion[1][1] - p.LARGO_SOL)
            self.soles_creados.append((x, y))

    def animacion(self):
        if self.n_imagen % 2 == 0:
            self.label.setPixmap(QPixmap(self.imagenes[0]))
        else:
            self.label.setPixmap(QPixmap(self.imagenes[1]))
        self.n_imagen += 1

    def muere(self):
        self.label.hide()
        self.parar_timers()
    
    def parar_timers(self):
        self.timer_animacion.stop()
        self.timer_crear_soles.stop()


class PlantaClasica():
    def __init__(self):
        self.vida = p.VIDA_PLANTA
        self.tipo = "planta clasica"
        self.imagenes = [p.IMG_PC_1, p.IMG_PC_2, p.IMG_PC_3]
        self.label = None
        self.posicion = None
        self.balas = []
        self.imagenes_balas = [p.IMG_BALA_C_1, p.IMG_BALA_C_2, p.IMG_BALA_C_3]
        self.timer_disparar = QTimer()
        self.timer_animacion = QTimer()
        self.n_imagen = 0
        self.crear_timers()

    def crear_timers(self):
        self.timer_disparar.setInterval(p.INTERVALO_DISPARO)
        self.timer_disparar.timeout.connect(self.disparar)
        self.timer_animacion.setInterval(int(p.INTERVALO_DISPARO/3))
        self.timer_animacion.timeout.connect(self.animacion)
    
    def correr_timers(self):
        self.timer_disparar.start()
        self.timer_animacion.start()

    def disparar(self):
        if (self.posicion[1][0] <= p.Y_FILA_1 < self.posicion[1][1]):
            y = p.Y_FILA_1
        else:
            y = p.Y_FILA_2
        x = int((self.posicion[0][0] + self.posicion[0][1])/2)
        bala = Bala(self.imagenes_balas, x, y)
        bala.timer_mov_bala.start()
        self.balas.append(bala)

    def animacion(self):
        if self.n_imagen == 0:
            self.label.setPixmap(QPixmap(self.imagenes[0]))
            self.n_imagen = 1
        elif self.n_imagen == 1:
            self.label.setPixmap(QPixmap(self.imagenes[1]))
            self.n_imagen = 2
        else:
            self.label.setPixmap(QPixmap(self.imagenes[2]))
            self.n_imagen = 0
            
    def muere(self):
        self.label.hide()
        self.parar_timers()
    
    def parar_timers(self):
        self.timer_animacion.stop()
        self.timer_disparar.stop()


class PlantaAzul(PlantaClasica):
    def __init__(self):
        super().__init__()
        self.tipo = "planta azul"
        self.ralentizar = p.RALENTIZAR_ZOMBIE
        self.imagenes = [p.IMG_PA_1, p.IMG_PA_2, p.IMG_PA_3]
        self.imagenes_balas = [p.IMG_BALA_A_1, p.IMG_BALA_A_2, p.IMG_BALA_A_3]
        

class PlantaPatata():
    def __init__(self):
        super().__init__()
        self.vida = 2*(p.VIDA_PLANTA)
        self.imagenes = [p.IMG_PAPA_1, p.IMG_PAPA_2, p.IMG_PAPA_3]
        self.timer_animacion = QTimer()
        self.tipo = "papa"
        self.crear_timers()

    def crear_timers(self):
        self.timer_animacion.setInterval(p.INTERVALO_ACTUALIZAR_JUEGO)
        self.timer_animacion.timeout.connect(self.animacion)
    
    def correr_timers(self):
        self.timer_animacion.start()

    def animacion(self):
        if self.vida > 120:
            self.label.setPixmap(QPixmap(self.imagenes[0]))
        elif 60 < self.vida <= 120:
            self.label.setPixmap(QPixmap(self.imagenes[1]))
        else:
            self.label.setPixmap(QPixmap(self.imagenes[2])) 
    
    def muere(self):
        self.label.hide()
        self.parar_timers()
    
    def parar_timers(self):
        self.timer_animacion.stop()


class Bala():
    def __init__(self, imagenes, x, y):
        self.x = x
        self.y = y
        self.n_imagen = 0
        self.ancho = p.ANCHO_BALA
        self.largo = p.LARGO_BALA
        self.llego = False
        self.aparecio = False
        self.label = None
        self.dano = p.DANO_PROYECTIL
        self.imagenes = imagenes
        self.timer_mov_bala = QTimer()
        self.timer_animacion = QTimer()
        self.configurar_timer()
    
    def configurar_timer(self):
        self.timer_mov_bala.setInterval(p.INTERVALO_ACTUALIZAR_JUEGO)
        self.timer_mov_bala.timeout.connect(self.mover_bala)
        self.timer_animacion.setInterval(p.INTERVALO_ACTUALIZAR_JUEGO)
        self.timer_animacion.timeout.connect(self.animacion)
    
    def correr_timers(self):
        self.timer_mov_bala.start()
    
    def parar_timers(self):
        self.timer_mov_bala.stop()
    
    def mover_bala(self):
        self.x += p.VELOCIDAD_BALA
        self.label.move(int(self.x), int(self.y))
        if self.llego is True:
            self.n_imagen += 1
            self.timer_mov_bala.stop()
            self.timer_animacion.start()
    
    def animacion(self):
        if self.n_imagen == 1:
            self.label.setPixmap(QPixmap(self.imagenes[1]))
            self.n_imagen += 1
        elif self.n_imagen == 2:
            self.n_imagen += 1
            self.label.setPixmap(QPixmap(self.imagenes[2]))
        else:
            self.label.hide()
            self.timer_animacion.stop()

    def parar_timers(self):
        self.timer_mov_bala.stop()


class ZombieClasico():
    def __init__(self, pos_y):
        super().__init__()
        self.timer_mover = QTimer()
        self.timer_comer = QTimer()
        self.timer_animacion_comer = QTimer()
        self.frenado = False
        self.llego = False
        self.vida = p.VIDA_ZOMBIE
        self.dano = p.DANO_MORDIDA
        self._x = p.X_LIM_SUPERIOR
        self.y = pos_y
        self.velocidad = p.VELOCIDAD_ZOMBIE_X
        self.ancho = p.ANCHO_ZOMBIE
        self.largo = p.LARGO_ZOMBIE
        self.pasos = 0
        self.vivo = True
        self.label = None
        self.bloque = None
        self.aparecio = False
        self.comiendo = 0
        self.imagenes_caminando = [p.IMG_Z_W_W1, p.IMG_Z_W_W2]
        self.imagenes_comiendo = [p.IMG_Z_W_C1, p.IMG_Z_W_C2, p.IMG_Z_W_C3]
        self.configurar_timer()
    
    def configurar_timer(self):
        self.timer_mover.setInterval(p.VELOCIDAD_ZOMBIE)
        self.timer_mover.timeout.connect(self.mover)
        self.timer_comer.setInterval(p.INTERVALO_TIEMPO_MORDIDA)
        self.timer_comer.timeout.connect(self.comer)
        self.timer_animacion_comer.setInterval(p.ANIMACION_ZOMBIE)
        self.timer_animacion_comer.timeout.connect(self.animacion_comer)

    def parar_timers(self):
        self.timer_animacion_comer.stop()
        self.timer_comer.stop()
        self.timer_mover.stop()
    
    def correr_timers(self):
        self.timer_mover.start()
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        if valor >= p.X_LIM_PIERDE:
            self._x = valor
        elif valor < p.X_LIM_PIERDE:
            self._x = p.X_LIM_PIERDE
            self.llego = True
            self.parar_timers()
            
    
    def mover(self):
        if self.vida > 0 and self.label != None:
            self.x -= self.velocidad 
            if self.pasos % 2 == 0:
                self.label.setPixmap(QPixmap(self.imagenes_caminando[0]))
            else:
                self.label.setPixmap(QPixmap(self.imagenes_caminando[1]))
            self.label.move(int(self.x), int(self.y))
            self.pasos += 1
            self.aparecio=True
    
    def animacion_comer(self):
        if self.vida > 0 and self.label != None:
            if self.comiendo == 0:
                self.label.setPixmap(QPixmap(self.imagenes_comiendo[0]))
                self.comiendo = 1
            elif self.comiendo == 1:
                self.label.setPixmap(QPixmap(self.imagenes_comiendo[1]))
                self.comiendo = 2
            else:
                self.label.setPixmap(QPixmap(self.imagenes_comiendo[2]))
                self.comiendo = 0

    def comer(self):
        if self.vida > 0:
            if self.bloque.planta != None:
                self.bloque.planta.vida -= self.dano
                if self.bloque.planta.vida <= 0:
                    self.timer_animacion_comer.stop()
                    self.label.setPixmap(QPixmap(self.imagenes_caminando[0]))
                    self.bloque.planta.muere()
                    self.bloque.ocupado = False
                    self.bloque.planta = None
    
    def muere(self):
        self.label.hide()
        self.parar_timers()


class ZombieRapido(ZombieClasico):
    def __init__(self, pos_y):
        super().__init__(pos_y)
        self.velocidad = 1.5 * p.VELOCIDAD_ZOMBIE_X
        self.imagenes_caminando = [p.IMG_Z_R_W1, p.IMG_Z_R_W2]
        self.imagenes_comiendo = [p.IMG_Z_R_C1, p.IMG_Z_R_C2, p.IMG_Z_R_C3]


class Bloque():
    def __init__(self, posicion):
        super().__init__()
        self.posicion = posicion
        self.planta = None
        self.ocupado = False
        