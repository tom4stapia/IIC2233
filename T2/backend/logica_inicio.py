from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, str)
    senal_abrir_juego = pyqtSignal(str)
    senal_enviar_usuario = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario):
        if usuario.isalnum() is True:
            if p.MIN_CARACTERES > len(usuario):
                error = "No cumple con el minimo de caracteres."
                self.senal_respuesta_validacion.emit(False, error)
            elif p.MAX_CARACTERES < len(usuario):
                error = "No cumple con el maximo de caracteres."
                self.senal_respuesta_validacion.emit(False, error)
            else:
                self.senal_abrir_juego.emit(usuario)
                self.senal_respuesta_validacion.emit(True, "")
                self.senal_enviar_usuario.emit(usuario)
        else:
            if len(usuario) == 0:
                error = f"Debe contener al menos {p.MIN_CARACTERES} caracteres."
                self.senal_respuesta_validacion.emit(False, error)
            else:
                error = "No debe contener caracteres que no sean alfanumericos."
                self.senal_respuesta_validacion.emit(False, error)