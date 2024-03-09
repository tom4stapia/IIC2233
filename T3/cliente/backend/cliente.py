"""
Modulo contiene implementación principal del cliente
"""
from PyQt5.QtCore import pyqtSignal, QObject
import socket
import json
from threading import Thread
from cripto import encriptar, desencriptar

class Cliente(QObject):
    senal_manejar_mensaje = pyqtSignal(dict)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de iniciar el cliente y conectar el socket
        """
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.comenzar_a_escuchar()
        except ConnectionRefusedError as e:
            print(f"\n-ERROR: No se pudo conectar al servidor.{e}-")

        except ConnectionError as e:
            print(f"\n-ERROR: El servidor no está inicializado. {e}-")

    def comenzar_a_escuchar(self):
        """
        Instancia el Thread que escucha los mensajes del servidor
        """
        thread = Thread(target=self.escuchar_servidor, daemon=True)
        thread.start()
    
    def escuchar_servidor(self):
        """
        Recibe mensajes constantes desde el servidor y responde.
        """
        try:
            while True:
                mensaje = self.recibir()
                self.senal_manejar_mensaje.emit(mensaje)
        except ConnectionResetError:
            print("Error de conexión con el servidor")
        finally:
            self.socket_cliente.close()

    def recibir(self):
        """
        Se encarga de recibir lis mensajes del servidor.
        """
        # TODO: Completado por estudiante
        try:
            largo_bytes_mensaje = self.socket_cliente.recv(4)
            largo_mensaje = int.from_bytes(largo_bytes_mensaje, byteorder='big')
            bytes_mensaje = bytearray()
            while len(bytes_mensaje) < largo_mensaje:
                num_bloque = self.socket_cliente.recv(4)
                bloque = self.socket_cliente.recv(32)
                if largo_bytes_mensaje - len(bytes_mensaje) < 12:
                    mensaje = bloque[4: 4 + largo_bytes_mensaje - len(bytes_mensaje)]
                else:
                    mensaje = bloque[4:16]
                bytes_mensaje += mensaje
            mensaje = self.decodificar_mensaje(bytes_mensaje)
            return mensaje
        except:
            raise ConnectionError

    def enviar(self, mensaje):
        bloques = self.codificar_mensaje(mensaje)
        for bloque in bloques:
            self.socket_cliente.sendall(bloque)

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            mensaje_bytes = mensaje_json.encode()
            mensaje_encriptado = encriptar(mensaje_bytes)
            largo_mensaje = len(mensaje_encriptado).to_bytes(4, byteorder="big")
            bloques = []
            bloques.append(largo_mensaje)
            num_bloque = 0
            while len(mensaje_encriptado) > 0:
                num_bloque_byte = num_bloque.to_bytes(4, byteorder="little")
                mensaje_bloque = mensaje_encriptado[:12]
                while len(mensaje_bloque) != 32:
                    mensaje_bloque.extend(b'\x00')

                bloques.append(num_bloque_byte + mensaje_bloque)
                mensaje_encriptado = mensaje_encriptado[12:]
                num_bloque += 1
            return bloques
        except json.JSONDecodeError:
            print("ERROR: No se pudo codificar el mensaje")
            return b""

    def decodificar_mensaje(self, bytes_mensaje):
        try:
            mensaje = desencriptar(bytes_mensaje)
            mensaje = mensaje.decode()
            mensaje = json.loads(mensaje)
            return mensaje
        except json.JSONDecodeError:
            print("ERROR: No se pudo decodificar el mensaje")
            return {}

