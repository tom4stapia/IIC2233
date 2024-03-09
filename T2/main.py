import sys

from dccruzvszombies import DCCruzVsZombies

if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)
    sys.__excepthook__ = hook

    juego = DCCruzVsZombies(sys.argv)
    juego.iniciar()
    sys.exit(juego.exec())
