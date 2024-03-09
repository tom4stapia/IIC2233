"""
Módulo principal del cliente.
"""
import sys
from os.path import join
from backend.cliente import Cliente
from backend.interfaz import Interfaz
from cripto import data_json

if __name__ == "__main__":
    HOST = data_json("HOST")
    PORT = data_json("PORT")
    try:
        def hook(type_, value, traceback):
            print(type_)
            print(traceback)
        sys.__excepthook__ = hook
        cliente = Cliente(HOST, PORT)
        interfaz = Interfaz(sys.argv, cliente)
        if cliente.conectado is True:
            interfaz.ventana_inicio.show()
        sys.exit(interfaz.exec_())

    except ConnectionError as e:
        print("Ocurrió un error.", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente...")
        sys.exit()
