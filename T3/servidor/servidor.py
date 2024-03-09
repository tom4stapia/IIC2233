"""
Modulo contiene la implementación principal del servidor
"""
import json
import socket
import threading
from logica import Logica
from cripto import encriptar, desencriptar

class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.logica = Logica(self)
        self.id_cliente = 0
        self.log("".center(80, "-"))
        self.log("Inicializando servidor...")
        self.sockets = {}
        self.iniciar_servidor()

    def iniciar_servidor(self):
        """
        Crea el socket, lo enlaza y comienza a escuchar
        """
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.log("Servidor escuchando...")
        self.comenzar_a_aceptar()

    def comenzar_a_aceptar(self):
        """
        Crea y comienza el thread encargado de aceptar clientes
        """
        thread = threading.Thread(target=self.aceptar_clientes, daemon=True)
        thread.start()

    def aceptar_clientes(self):
        """
        Es arrancado como thread para de aceptar clientes, este se ejecuta
        siempre que se este conectado y acepta el socket del servidor. Luego
        se crea y comienza a escuchar al cliente. para finalmente aumentar en 1
        el id_cliente.
        """
        try:
            while True:
                socket_cliente, _ = self.socket_servidor.accept()
                self.sockets[str(socket_cliente)] = socket_cliente
                thread_cliente = threading.Thread(target=self.escuchar_cliente, 
                                args=(self.id_cliente, socket_cliente), daemon=True)
                self.id_cliente += 1
                thread_cliente.start()

        except ConnectionError:
            self.log('Error de conexión con el cliente')
        
    def escuchar_cliente(self, id_cliente, socket_cliente):
        """
        Ciclo encargado de escuchar a cada cliente de forma individual, esta
        funcion se ejecuta siempre que el servidor este conectado, recibe el
        socket del cliente y si hay un mensaje, lo procesa con la funcion
        instanciada en la logica.
        """
        self.log(f"Comenzando a escuchar al cliente {id_cliente}...")
        try:
            while True:
                mensaje = self.recibir_mensaje(socket_cliente)
                respuesta = self.logica.procesar_mensaje(mensaje, socket_cliente)
                if respuesta != {}:
                    self.enviar_mensaje(respuesta, socket_cliente)

        except ConnectionError:
            self.eliminar_cliente(id_cliente, socket_cliente)
            self.log('Error de conexión con el cliente')


    def recibir_mensaje(self, socket_cliente):
        """
        Recibe un mensaje del cliente, lo DECODIFICA usando el protocolo
        establecido y lo des-serializa retornando un diccionario.
        """
        largo_bytes_mensaje = socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_bytes_mensaje, byteorder='big')
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            num_bloque = socket_cliente.recv(4)
            bloque = socket_cliente.recv(32)
            if largo_mensaje - len(bytes_mensaje) < 12:
                mensaje = bloque[4: 4 + largo_mensaje - len(bytes_mensaje)]
            else:
                mensaje = bloque[4:16]
            bytes_mensaje += mensaje
        
        mensaje = self.decodificar_mensaje(bytes_mensaje)
        return mensaje

    def enviar_mensaje(self, mensaje, socket_cliente) -> None:
        """
        Recibe una instruccion,
        lo CODIFICA usando el protocolo establecido y lo envía al cliente
        """
        # TODO: Completado por estudiante
        bloques = self.codificar_mensaje(mensaje)
        for bloque in bloques:
            socket_cliente.sendall(bloque)
        

    def eliminar_cliente(self, id_cliente, socket_cliente):
        """
        Elimina un cliente del diccionario de clientes conectados
        """
        pass

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
            self.log("ERROR: No se pudo codificar el mensaje")
            return b""

    def decodificar_mensaje(self, bytes_mensaje):
        # TODO: Completado por estudiante
        try:
            mensaje = desencriptar(bytes_mensaje)
            mensaje = mensaje.decode()
            mensaje = json.loads(mensaje)
            return mensaje
        except json.JSONDecodeError:
            self.log("ERROR: No se pudo decodificar el mensaje")
            return {}


    def log(self, mensaje: str):
        """
        Imprime un mensaje en consola
        """
        print("|" + mensaje.center(80, " ") + "|")