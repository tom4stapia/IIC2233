from random import randint
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from backend.elementos_juego import Girasol, PlantaAzul
from backend.elementos_juego import PlantaClasica, PlantaPatata
from backend.elementos_juego import ZombieClasico, ZombieRapido
import parametros as p
import backend.aparicion_zombies as a
from PyQt5.QtGui import QPixmap


class LogicaVentanaJuego(QObject):

    senal_compra_valida = pyqtSignal(bool, object, str)
    senal_cargar_datos_iniciales = pyqtSignal(dict)
    senal_enviar_zombie = pyqtSignal(object)
    senal_mover_zombie = pyqtSignal(object)
    senal_mandar_soles = pyqtSignal(int, int, object)
    senal_crear_bala = pyqtSignal(object)
    senal_gana_ronda = pyqtSignal()
    senal_pierde = pyqtSignal()
    senal_datos = pyqtSignal(dict, bool)

    def __init__(self, bloques):
        super().__init__()
        self.soles = p.SOLES_INICIALES
        self.bloques = bloques
        self.nivel = 1
        self.zombies_totales = 2*p.N_ZOMBIES
        self.zombies_destruidos = 0
        self.puntaje_total = 0
        self.puntaje = 0
        self.frase = ""
        self.plantas = []
        self.girasoles = []
        self.papas = []
        self.zombie_aparecio = []
        self.zombies_fila_1 = []
        self.zombies_fila_2 = []
        self.soles_avanzar = p.COSTO_AVANZAR
        self.timer_actualizar_juego = QTimer()
        self.timer_aparicion_zombies = QTimer()
        self.timer_movimiento_zombies = QTimer()
        self.timer_aparicion_soles = QTimer()
        self.timer_crear_balas = QTimer()
        self.timer_revisar_colision = QTimer()
        self.configurar_timers()
        
        
    def configurar_timers(self):
        self.timer_actualizar_juego.setInterval(p.INTERVALO_ACTUALIZAR_JUEGO)
        self.timer_actualizar_juego.timeout.connect(self.actualizar_labels)
        self.timer_actualizar_juego.start()
        self.timer_movimiento_zombies.setInterval(p.INTERVALO_ACTUALIZAR_JUEGO)
        self.timer_movimiento_zombies.timeout.connect(self.mover_zombies)
        self.timer_crear_balas.setInterval(p.INTERVALO_ACTUALIZAR_JUEGO)
        self.timer_crear_balas.timeout.connect(self.crear_balas)
        self.timer_revisar_colision.timeout.connect(self.revisar_colision)
    
    def recibir_datos(self, soles, ponderador, puntaje, bool):
        self.agregar_soles = soles
        self.ponderador = float(ponderador)
        self.agregar_puntaje = puntaje
        self.soles_random = bool
        if self.soles_random:
            self.timer_aparicion_soles.setInterval(p.INTERVALO_APARICION_SOLES)
            self.timer_aparicion_soles.timeout.connect(self.generar_soles)

    def correr_timers(self):
        for i in range(len(self.plantas)):
            self.plantas[i].correr_timers()
            for j in range(len(self.plantas[i].balas)):
                self.plantas[i].balas[j].correr_timers()
        for i in range(len(self.girasoles)):
            if self.girasoles[i].planta is not None:
                self.girasoles[i].planta.correr_timers()
        for i in range(len(self.papas)):
            self.papas[i].correr_timers()
        self.timer_actualizar_juego.start()
        if len(self.zombie_aparecio) < 2*p.N_ZOMBIES:
            self.timer_aparicion_zombies.start()
        self.timer_crear_balas.start()
        self.timer_revisar_colision.start()
        if self.soles_random:
            self.timer_aparicion_soles.start()
        if len(self.zombie_aparecio) > 0:
            self.timer_movimiento_zombies.start()
        for i in range(len(self.zombie_aparecio)):
            self.zombie_aparecio[i].correr_timers()
        
    def parar_timers(self):
        for i in range(len(self.plantas)):
            self.plantas[i].parar_timers()
            for j in range(len(self.plantas[i].balas)):
                self.plantas[i].balas[j].parar_timers()
        for i in range(len(self.girasoles)):
            if self.girasoles[i].planta is not None:
                self.girasoles[i].planta.parar_timers()
        for i in range(len(self.papas)):
            self.papas[i].parar_timers()
        for i in range(len(self.zombie_aparecio)):
            self.zombie_aparecio[i].parar_timers()
        self.timer_aparicion_zombies.stop()
        self.timer_movimiento_zombies.stop()
        if self.soles_random:
            self.timer_aparicion_soles.stop()
        self.timer_crear_balas.stop()
        self.timer_revisar_colision.stop()    
    
    def empezar_timer_planta(self, planta):
        planta.correr_timers()

    def revisar_colision(self):
        for planta in self.plantas:
            for zombie in self.zombie_aparecio:
                if zombie.vida > 0 and planta.vida > 0 and zombie.aparecio is True:
                    for i in range(len(planta.balas)):
                        if ((zombie.x <= planta.balas[i].x <= p.X_LIM_SUPERIOR + p.ANCHO_ZOMBIE)
                            and planta.balas[i].y == zombie.y) and planta.balas[i].llego is False\
                            and planta.balas[i].aparecio is True:
                            planta.balas[i].llego = True
                            zombie.vida -= planta.balas[i].dano
                            if planta.tipo == "planta azul":
                                if zombie.frenado is False:
                                    disminuye = (1-p.RALENTIZAR_ZOMBIE)
                                    zombie.velocidad = int(disminuye*zombie.velocidad)
                                    zombie.frenado = True
                            if zombie.vida <= 0 and zombie.vivo is True:
                                zombie.vivo = False
                                self.puntaje += self.agregar_puntaje
                                self.zombies_destruidos += 1
                                self.zombies_totales -= 1
                                zombie.muere()
                                if self.zombies_destruidos == 2*p.N_ZOMBIES:
                                    self.gano_ronda()
                                       
    def gano_ronda(self):
        self.timer_actualizar_juego.stop()
        self.puntaje_total += self.puntaje
        if self.zombies_destruidos == 2*p.N_ZOMBIES:
            self.puntaje_total += self.puntaje*self.ponderador
        self.senal_cargar_datos_iniciales.emit({
            'Soles': str(self.soles),
            'Puntaje': str(self.puntaje),
            'Nivel': str(self.nivel),
            'Zombies restantes': str(self.zombies_totales),
            'Zombies destruidos': str(self.zombies_destruidos)
        })
        self.senal_datos.emit({
            'Soles': str(self.soles),
            'Puntaje': str(self.puntaje),
            'Nivel': str(self.nivel),
            'Puntaje total': str(self.puntaje_total),
            'Zombies destruidos': str(self.zombies_destruidos)
            }, True)
        self.parar_timers()
        self.senal_gana_ronda.emit()
        self.nivel += 1

    def perdio(self):
        self.timer_actualizar_juego.stop()
        self.puntaje_total += self.puntaje
        self.senal_cargar_datos_iniciales.emit({
            'Soles': str(self.soles),
            'Puntaje': str(self.puntaje),
            'Nivel': str(self.nivel),
            'Zombies restantes': str(self.zombies_totales),
            'Zombies destruidos': str(self.zombies_destruidos)
        })
        self.senal_datos.emit({
            'Soles': str(self.soles),
            'Puntaje': str(self.puntaje),
            'Nivel': str(self.nivel),
            'Puntaje total': str(self.puntaje_total),
            'Zombies destruidos': str(self.zombies_destruidos)
            }, False)
        self.parar_timers()
        self.senal_pierde.emit()
        self.nivel = 1
        self.puntaje_total = 0
        
    def crear_zombies(self):
        for _ in range(int(self.zombies_totales/2)):
            f_1 = randint(1, 2)
            if f_1 == 1:
                self.zombies_fila_1.append(ZombieClasico(p.Y_FILA_1))
            else:
                self.zombies_fila_1.append(ZombieRapido(p.Y_FILA_1))
            f_2 = randint(1, 2)
            if f_2 == 1:
                self.zombies_fila_2.append(ZombieClasico(p.Y_FILA_2))
            else:
                self.zombies_fila_2.append(ZombieRapido(p.Y_FILA_2))
        intervalo = int(1000*a.intervalo_aparicion(self.nivel, self.ponderador))
        self.timer_aparicion_zombies.setInterval(intervalo)
        self.timer_aparicion_zombies.timeout.connect(self.aparicion_zombie)
        
    def generar_soles(self):
        x = randint(p.X_LIM_INFERIOR, p.X_LIM_SUPERIOR)
        y = randint(p.Y_LIM_INFERIOR, p.Y_LIM_SUPERIOR)
        self.senal_mandar_soles.emit(x, y, QPixmap(p.IMG_SOL))
    
    def sumar_soles(self):
        self.soles += self.agregar_soles

    def crear_balas(self):
        for planta in self.plantas:
            for i in range(len(planta.balas)):
                if planta.balas[i].aparecio is False:
                    self.senal_crear_bala.emit(planta.balas[i])
    
    def aparicion_zombie(self):
        lista = self.zombies_fila_1 + self.zombies_fila_2
        pos = randint(0, len(lista)-1)
        while lista[pos] in self.zombie_aparecio:
            if len(self.zombie_aparecio) == 2 * p.N_ZOMBIES:
                break
            pos = randint(0, len(lista)-1)
        if len(self.zombie_aparecio) < 2 * p.N_ZOMBIES:
            self.zombie_aparecio.append(lista[pos])
        if len(self.zombie_aparecio) <= 2 * p.N_ZOMBIES:
            self.senal_enviar_zombie.emit(lista[pos])
        if len(self.zombie_aparecio) == 2 * p.N_ZOMBIES:
            self.timer_aparicion_zombies.stop()
        if len(self.zombie_aparecio) == 1:
            self.timer_movimiento_zombies.start()        
    
    def mover_zombies(self):
        for zombie in self.zombie_aparecio:
            if zombie.llego is True:
                self.perdio()
                break
            for b in self.bloques:
                if self.bloques[b].posicion[0][0] <= zombie.x <= \
                    self.bloques[b].posicion[0][1]\
                    and self.bloques[b].posicion[1][0] <= zombie.y < \
                        self.bloques[b].posicion[1][1]:
                    zombie.bloque = self.bloques[b]
                    if self.bloques[b].ocupado is True:
                        if zombie.timer_mover.isActive() is True:
                            zombie.timer_mover.stop()
                        if zombie.timer_animacion_comer.isActive() is False and \
                            zombie.vivo is True:
                            zombie.timer_animacion_comer.start()
                            zombie.timer_comer.start()
                    else:
                        if zombie.timer_mover.isActive() is False and zombie.vivo is True:
                            zombie.timer_mover.start()
                    

    def actualizar_labels(self):
        self.senal_cargar_datos_iniciales.emit({
            'Soles': str(self.soles),
            'Puntaje': str(self.puntaje),
            'Nivel': str(self.nivel),
            'Zombies restantes': str(self.zombies_totales),
            'Zombies destruidos': str(self.zombies_destruidos)
        })
        for girasol in self.girasoles:
            if girasol.planta is not None:
                if girasol.planta.tipo == "girasol":
                    if len(girasol.planta.soles_creados) == p.CANTIDAD_SOLES:
                        for i in range(len(girasol.planta.soles_creados)):
                            x = girasol.planta.soles_creados[i][0]
                            y = girasol.planta.soles_creados[i][1]
                            self.senal_mandar_soles.emit(x, y, QPixmap(p.IMG_SOL))
                        girasol.planta.soles_creados = []
    

    def validar_compra_girasol(self, bloque):
        if bloque.ocupado is False and self.soles >= p.VALOR_GIRASOL:
            bloque.ocupado = True
            bloque.planta = Girasol()
            bloque.planta.posicion = bloque.posicion
            self.girasoles.append(bloque)
            self.soles -= p.VALOR_GIRASOL
            self.senal_compra_valida.emit(True, bloque, "")
        else:
            if bloque.ocupado is True:
                self.senal_compra_valida.emit(False, bloque, "Ya existe una planta en ese bloque")
            else:
                self.senal_compra_valida.emit(False, bloque, "No tienes soles suficientes")

    def validar_compra_planta_clasica(self, bloque):
        if bloque.ocupado is False and self.soles >= p.VALOR_PLANTA_CLASICA:
            bloque.ocupado = True
            bloque.planta = PlantaClasica()
            self.plantas.append(bloque.planta)
            bloque.planta.posicion = bloque.posicion
            self.soles -= p.VALOR_PLANTA_CLASICA
            self.senal_compra_valida.emit(True, bloque, "")
        else:
            if bloque.ocupado is True:
                self.senal_compra_valida.emit(False, bloque, "Ya existe una planta en ese bloque")
            else:
                self.senal_compra_valida.emit(False, bloque, "No tienes soles suficientes")
        
    def validar_compra_planta_azul(self, bloque):
        if bloque.ocupado == False and self.soles >= p.VALOR_PLANTA_AZUL:
            bloque.ocupado = True
            bloque.planta = PlantaAzul()
            self.plantas.append(bloque.planta)
            bloque.planta.posicion = bloque.posicion
            self.soles -= p.VALOR_PLANTA_AZUL
            self.senal_compra_valida.emit(True, bloque, "")
        else:
            if bloque.ocupado is True:
                self.senal_compra_valida.emit(False, bloque, "Ya existe una planta en ese bloque")
            else:
                self.senal_compra_valida.emit(False, bloque, "No tienes soles suficientes")
        
    def validar_compra_patata(self, bloque):
        if bloque.ocupado == False and self.soles >= p.VALOR_PAPA:
            bloque.ocupado = True
            bloque.planta = PlantaPatata()
            self.papas.append(bloque.planta)
            bloque.planta.posicion = bloque.posicion
            self.soles -= p.VALOR_PAPA
            self.senal_compra_valida.emit(True, bloque, "")
        else:
            if bloque.ocupado is True:
                self.senal_compra_valida.emit(False, bloque, "Ya existe una planta en ese bloque")
            else:
                self.senal_compra_valida.emit(False, bloque, "No tienes soles suficientes")
    def reiniciar_datos(self):
        self.zombies_totales = 2*p.N_ZOMBIES
        self.zombies_destruidos = 0
        self.soles = p.SOLES_INICIALES
        self.puntaje = 0
        self.plantas = []
        self.girasoles = []
        self.papas = []
        self.zombie_aparecio = []
        self.zombies_fila_1 = []
        self.zombies_fila_2 = []
        for b in self.bloques:
            self.bloques[b].planta = None
            self.bloques[b].ocupado = False
        self.actualizar_labels()
    
    def comprobar_avanzar_ronda(self):
        if self.soles >= p.COSTO_AVANZAR:
            self.gano_ronda()
    
    def cheatcodes(self, tecla):
        if tecla == "s" and self.frase == "":
            self.frase += tecla
        elif self.frase == "s" and tecla == "u":
            self.frase += tecla
        elif self.frase == "su" and tecla == "n":
            self.soles += p.SOLES_EXTRA
            self.frase = ""
        elif tecla == "k" and self.frase == "":
            self.frase += tecla
        elif self.frase == "k" and tecla == "i":
            self.frase += tecla
        elif self.frase == "ki" and tecla == "l":
            for i in range(len(self.zombie_aparecio)):
                self.zombie_aparecio[i].label.hide()
            self.zombies_destruidos = 2*p.N_ZOMBIES
            self.zombies_totales = 0
            self.puntaje = 2*p.N_ZOMBIES*self.agregar_puntaje
            self.gano_ronda()
            self.frase = ""
        else:
            self.frase = ""
