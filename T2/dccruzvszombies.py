from PyQt5.QtWidgets import QApplication
from backend.logica_inicio import LogicaInicio
from backend.logica_post_ronda import LogicaPostRonda
from backend.logica_ranking import LogicaRanking
from backend.logica_ventana_juego import LogicaVentanaJuego
from frontend.ventana_post_ronda import VentanaPostJuego
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_ranking import Ranking
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_inicio import VentanaInicio


class DCCruzVsZombies(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        # Instanciar Ventanas
        self.ventana_inicio = VentanaInicio()
        self.ventana_juego = VentanaJuego()
        self.ventana_postjuego = VentanaPostJuego()
        self.ventana_ranking = Ranking()
        self.ventana_principal = VentanaPrincipal()

        # Instanciar Lógicas
        self.logica_post_ronda = LogicaPostRonda()
        self.logica_ranking = LogicaRanking()
        self.logica_inicio = LogicaInicio()
        self.logica_juego = LogicaVentanaJuego(self.ventana_juego.bloques)
        
        # Conectar Señales
        self.conectar_inicio()
        self.conectar_ranking()
        self.conectar_juego()
        self.conectar_post_juego()

    def conectar_inicio(self):
        self.ventana_inicio.senal_enviar_login.connect(
            self.logica_inicio.comprobar_usuario)
        self.logica_inicio.senal_respuesta_validacion.connect(
            self.ventana_inicio.recibir_validacion)
        self.ventana_inicio.senal_ordenar_ranking.connect(
            self.logica_ranking.ordenar_ranking)
        self.ventana_inicio.senal_abrir_ventanap.connect(
            self.ventana_principal.mostrar_ventana)
        self.logica_inicio.senal_enviar_usuario.connect(
            self.logica_post_ronda.recibir_usuario)

    def conectar_ranking(self):
        self.logica_ranking.senal_abrir_ranking.connect(
            self.ventana_ranking.actualizar_ranking)
        self.ventana_ranking.senal_ranking_revisado.connect(
            self.ventana_inicio.show)
        
        self.ventana_principal.senal_ventana_juego.connect(
            self.ventana_juego.mostrar_ventana)
        self.ventana_principal.senal_datos.connect(
            self.logica_juego.recibir_datos)
        
    def conectar_juego(self):
        self.ventana_juego.senal_compra_girasol.connect(
            self.logica_juego.validar_compra_girasol)
        self.ventana_juego.senal_compra_plantac.connect(
            self.logica_juego.validar_compra_planta_clasica)
        self.ventana_juego.senal_compra_plantaa.connect(
            self.logica_juego.validar_compra_planta_azul)
        self.ventana_juego.senal_compra_papa.connect(
            self.logica_juego.validar_compra_patata)
        self.logica_juego.senal_compra_valida.connect(
            self.ventana_juego.compra_exitosa)
        self.logica_juego.senal_cargar_datos_iniciales.connect(
            self.ventana_juego.setear_datos)
        self.ventana_juego.senal_creacion_zombies.connect(
            self.logica_juego.crear_zombies)
        self.ventana_juego.senal_empezar.connect(
            self.logica_juego.correr_timers)
        self.logica_juego.senal_enviar_zombie.connect(
            self.ventana_juego.aparece_zombie)
        self.logica_juego.senal_mandar_soles.connect(
            self.ventana_juego.aparece_sol)
        self.ventana_juego.senal_sumar_soles.connect(
            self.logica_juego.sumar_soles)
        self.logica_juego.senal_crear_bala.connect(
            self.ventana_juego.aparece_bala)
        self.ventana_juego.senal_empezar_planta.connect(
            self.logica_juego.empezar_timer_planta)
        self.ventana_juego.senal_reanudar.connect(
            self.logica_juego.correr_timers)
        self.ventana_juego.senal_pausar.connect(
            self.logica_juego.parar_timers)
        self.logica_juego.senal_gana_ronda.connect(
            self.ventana_juego.gana_ronda)
        self.logica_juego.senal_pierde.connect(
            self.ventana_juego.pierde_ronda)
        self.ventana_juego.senal_reiniciar.connect(
            self.logica_juego.reiniciar_datos)
        self.logica_juego.senal_datos.connect(
            self.ventana_postjuego.actualizar_datos)
        self.ventana_juego.senal_abrir_ventana_post.connect(
            self.ventana_postjuego.mostrar_datos)
        self.ventana_juego.senal_salir_juego.connect(
            self.logica_juego.perdio)
        self.ventana_juego.senal_avanzar_ronda.connect(
            self.logica_juego.comprobar_avanzar_ronda)
        self.ventana_juego.senal_tecla.connect(
            self.logica_juego.cheatcodes)
        self.ventana_juego.senal_empezar_ronda.connect(
            self.logica_juego.configurar_timers)
        
    def conectar_post_juego(self):
        self.ventana_postjuego.senal_pasar_ronda.connect(
            self.logica_post_ronda.comprobar_ronda)
        self.ventana_postjuego.senal_agregar_ranking.connect(
            self.logica_post_ronda.agregar_ranking)
        self.logica_post_ronda.senal_continuar_juego.connect(
            self.ventana_postjuego.recibir_validacion)
        self.ventana_postjuego.senal_salir.connect(
            self.ventana_inicio.mostrar_ventana)
        self.ventana_postjuego.senal_pasar.connect(
            self.ventana_juego.paso_de_ronda)
        
    def iniciar(self):
        self.ventana_inicio.show()
