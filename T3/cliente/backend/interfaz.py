"""
Ventana principal del cliente que se encarga de funcionar como backend de la
mayoria de ventanas, de conectar señales y de procesar los mensajes recibidos
por el cliente
"""
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication

from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_espera import VentanaEspera
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_final import VentanaFinal



class Interfaz(QApplication):
    senal_mostrar_ventana_espera = pyqtSignal()
    senal_login_rechazado = pyqtSignal()

    def __init__(self, argv, cliente):
        super().__init__(argv)
        self.ventana_inicio = VentanaInicio()
        self.ventana_espera = VentanaEspera()
        self.ventana_juego = VentanaJuego()
        self.ventana_final = VentanaFinal()
        self.cliente = cliente
        self.conectar_senales()
        # -----------------------------------------
    def conectar_senales(self):
        self.cliente.senal_manejar_mensaje.connect(
            self.manejar_mensaje
            )
        self.ventana_inicio.senal_enviar_login.connect(
          self.cliente.enviar
          )
        self.ventana_inicio.senal_pasar_ventana.connect(
            self.ventana_espera.mostrar_ventana
        )
        self.ventana_espera.senal_volver_inicio.connect(
            self.ventana_inicio.mostrar_ventana
        )
        self.ventana_espera.senal_pasar.connect(
            self.ventana_juego.mostrar_ventana
        )
        self.ventana_juego.senal_pasar_ventana.connect(
            self.ventana_final.mostrar_ventana
        )

        self.ventana_final.senal_cerrar_ventana.connect(
            self.ventana_inicio.mostrar_ventana
        )

    def mostrar_ventana_espera(self):
        self.ventana_espera.mostrar_ventana()
    def manejar_mensaje(self, mensaje: dict):
        """
        Maneja un mensaje recibido desde el servidor.
        """
        try:
            comando = mensaje["comando"]
        except KeyError:
            return {}

        if comando == "respuesta_validacion_login":
            if mensaje["estado"] == "aceptado":
                self.senal_mostrar_ventana_espera.emit()
                self.mostrar_ventana_espera()
            else:
                self.senal_login_rechazado.emit()