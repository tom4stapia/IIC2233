from cripto import data_json
from os.path import join


class Logica:
    def __init__(self, parent):
        # Esto permite ejecutar funciones de la clase Servidor
        self.parent = parent

        self.usuarios = {}

    def validar_login(self, nombre, socket_cliente):
        if nombre not in self.usuarios.values():
            self.usuarios[self.parent.id_cliente - 1] = nombre
            return {
                "comando": "respuesta_validacion_login",
                "estado": "aceptado",
                "nombre_usuario": nombre,
            }
        return {
            "comando": "respuesta_validacion_login",
            "estado": "rechazado",
            "error": "datos invalidos",
        }

    def procesar_mensaje(self, mensaje, socket_cliente):
        """
        Procesa un mensaje recibido desde el cliente
        """
        try:
            comando = mensaje["comando"]
        except KeyError:
            return {}
        if comando == "validar_login":
            respuesta = self.validar_login(
                mensaje["nombre usuario"], mensaje["contrasena"], socket_cliente
            )
        return respuesta
