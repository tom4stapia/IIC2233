from parametros import RUTA_ENTR, RUTA_OBJ, RUTA_PROG
from programones import TipoAgua, TipoFuego, TipoPlanta
from objetos import Baya, Pocion, Caramelo
from entrenador import Entrenador
from random import randint
from beautifultable import BeautifulTable
import sys


class LigaProgramon:
    def __init__(self):
        self.entrenadores = []
        self.perdedores = []
        self.programones_totales = []
        self.objetos_totales = []
        self.duplas = []
        self.ronda_actual = 1
        self.campeon = None
        # SE LLAMA A LLENAR_LIGA PARA CREAR LOS OBJETOS DE DISTINTOS ARCHIVOS
        self.llenar_liga()
    
    def resumen_campeonato(self):
        # SE CREA EL TEXTO PARA LA TABLA
        entrenadores = [self.entrenadores[n].nombre for n in range(len(self.entrenadores))]
        perdedores = [self.perdedores[n].nombre for n in range(len(self.perdedores))]
        activos = (", ".join(entrenadores))
        perdedores = (", ".join(perdedores))
        if len(self.perdedores) != 0:
            todos = activos+", "+perdedores
        else:
            todos = activos
        participantes = f"Participantes: {todos}\n"
        rondas = f"Ronda actual: {self.ronda_actual}\n"
        siguen = f"Entrenadores que siguen en la competencia: {activos}"
        # ### CITADO Y ADAPTADO ###
        # LINK EN README
        table = BeautifulTable()
        table.columns.header = ["Resumen campeonato"]
        table.rows.append([participantes+rondas+siguen])
        table.columns.alignment = BeautifulTable.ALIGN_LEFT
        table.columns.padding_left[0] = 0
        table.columns.padding_right[0] = 0
        table.set_style(BeautifulTable.STYLE_COMPACT)
        print(table)
        print()
        # FIN DE CITADO

    def simular_ronda(self, entrenador):
        # SE ORGANIZAN LAS DUPLAS PARA JUGAR
        self.duplas = []
        posiciones = []
        posicion_dupla = randint(0, len(self.entrenadores)-1)
        # SE ELIGE UNA DUPLA PARA EL USUARIO
        while self.entrenadores[posicion_dupla] == entrenador:
            posicion_dupla = randint(0, len(self.entrenadores)-1)
        for i in range(len(self.entrenadores)):
            if self.entrenadores[i] == entrenador:
                posiciones.append(i)
        posiciones.append(posicion_dupla)
        self.duplas.append((entrenador, self.entrenadores[posicion_dupla]))
        # SE ELIGEN ALEATORIAMENTE LAS OTRAS DUPLAS
        for i in range(round(len(self.entrenadores)/2)-1):
            primero = randint(0, len(self.entrenadores)-1)
            segundo = randint(0, len(self.entrenadores)-1)
            while primero in posiciones:
                primero = randint(0, len(self.entrenadores)-1)
            posiciones.append(primero)
            while segundo in posiciones:
                segundo = randint(0, len(self.entrenadores)-1)
            posiciones.append(segundo)
            self.duplas.append((self.entrenadores[primero], self.entrenadores[segundo]))
        subtable = BeautifulTable()
        # ### CITADO Y ADAPTADO ###
        # LINK EN README 
        for i in range(len(entrenador.programones)):
            subtable.rows.append([f"[{i+1}]", entrenador.programones[i].nombre])
        subtable.rows.append([f"[{len(entrenador.programones)+1}]", "Volver"])
        subtable.rows.append([f"[{len(entrenador.programones)+2}]", "Salir"])
        subtable.border.left = ''
        subtable.border.right = ''
        subtable.border.top = ''
        subtable.border.right = ''
        subtable.border.bottom = ''

        table = BeautifulTable()
        table.columns.header = ["Elige tu luchador"]
        table.rows.append([subtable])
        table.columns.padding_left[0] = 0
        table.columns.padding_right[0] = 0
        table.set_style(BeautifulTable.STYLE_COMPACT)
        print(table)
        print()
        # FIN DE CITADO
        # SE DA LA OPCION AL USUARIO PARA QUE ELIJA PROGRAMON PARA PELEAR
        opciones = [str(n+1) for n in range(len(entrenador.programones)+2)]
        opcion = input("\nSeleccione una opcion: ")
        while opcion not in opciones:
            opcion = input("\nSeleccione una opcion valida: ")
        if opcion == str(len(entrenador.programones)+1):
            pass
        elif opcion == str(len(entrenador.programones)+2):
            sys.exit()
        else:
            print(f"\nRonda {self.ronda_actual}")
            print()
            for i in range(len(self.duplas)):
                if i == 0:
                    # PROGRAMON USUARIO (ELEGIDO)
                    programon1 = entrenador.programones[int(opcion)-1]
                else:
                    # PROGRAMON RANDOM DE PRIMER ENTRENADOR
                    posicion_programon1 = randint(0, len(self.duplas[i][0].programones)-1)
                    programon1 = self.duplas[i][0].programones[posicion_programon1]
                # PROGRAMON RANDOM SEGUNDO ENTRENADOR
                posicion_programon2 = randint(0, len(self.duplas[i][1].programones)-1)
                programon2 = self.duplas[i][1].programones[posicion_programon2]
                # SE REVISA QUE PARAMETRO SE INGRESA A FUNCION LUCHAR
                if programon1.tipo == programon2.tipo:
                    valor1 = programon1.luchar(0)
                    valor2 = programon2.luchar(0)
                elif programon1.fuerte == programon2.tipo:
                    valor1 = programon1.luchar(1)
                    valor2 = programon2.luchar(-1)
                else:
                    valor1 = programon1.luchar(-1)
                    valor2 = programon2.luchar(1)
                # SE IMPRIME EL ENFRENTAMIENTO
                print(f"{self.duplas[i][0].nombre} usando al programon {programon1.nombre},"\
                      f" se enfrenta a {self.duplas[i][1].nombre} usando al "\
                      f"programon {programon2.nombre}")
                # SE REVISA GANADOR
                if valor1 > valor2:
                    programon1.gano_ronda()
                    print(f"{self.duplas[i][0].nombre} ha ganado la batalla")
                    self.perdedores.append(self.duplas[i][1])
                    self.entrenadores.remove(self.duplas[i][1])
                    self.duplas[i][0].energia = 100
                elif valor2 > valor1:
                    programon2.gano_ronda()
                    print(f"{self.duplas[i][1].nombre} ha ganado la batalla")
                    self.perdedores.append(self.duplas[i][0])
                    self.entrenadores.remove(self.duplas[i][0])
                    self.duplas[i][1].energia = 100
                else:
                    ganador = randint(0, 1)
                    if ganador == 1:
                        perdedor = 0
                        programon2.gano_ronda()
                    else:
                        perdedor = 1
                        programon1.gano_ronda()          
                    print(f"{self.duplas[i][ganador].nombre} ha ganado la batalla")
                    self.perdedores.append(self.duplas[i][perdedor])
                    self.entrenadores.remove(self.duplas[i][perdedor])
                    self.duplas[i][ganador].energia = 100
            self.ronda_actual += 1
            print()
            if self.ronda_actual == 5:
                self.campeon = self.entrenadores[0]

    def llenar_liga(self):
        # SE LLENAN LOS OBJETOS
        with open(RUTA_PROG, "r") as archivo:
            for linea in archivo:
                linea = linea.strip("\n").split(",")
                if linea[1] == "fuego":
                    programon = TipoFuego(nombre=linea[0], tipo=linea[1], nivel=int(linea[2]),\
                                          vida=int(linea[3]), ataque=int(linea[4]),\
                                          defensa=int(linea[5]), velocidad=int(linea[6]))
                    self.programones_totales.append(programon)
                elif linea[1] == "planta":
                    programon = TipoPlanta(nombre=linea[0], tipo=linea[1], nivel=int(linea[2]),\
                                           vida=int(linea[3]), ataque=int(linea[4]),\
                                           defensa=int(linea[5]), velocidad=int(linea[6]))
                    self.programones_totales.append(programon)
                elif linea[1] == "agua":
                    programon = TipoAgua(nombre=linea[0], tipo=linea[1], nivel=int(linea[2]),\
                                         vida=int(linea[3]), ataque=int(linea[4]), \
                                         defensa=int(linea[5]), velocidad=int(linea[6]))
                    self.programones_totales.append(programon)
        with open(RUTA_OBJ, "r") as archivo:
            for linea in archivo:
                linea = linea.strip("\n").split(",")
                if linea[1] == "baya":
                    objeto = Baya(nombre=linea[0], tipo=linea[1])
                    self.objetos_totales.append(objeto)
                elif linea[1] == "pocion":
                    objeto = Pocion(nombre=linea[0], tipo=linea[1])
                    self.objetos_totales.append(objeto)
                elif linea[1] == "caramelo":
                    objeto = Caramelo(nombre=linea[0], tipo=linea[1])
                    self.objetos_totales.append(objeto)
        with open(RUTA_ENTR, "r") as archivo:
            for linea in archivo:
                linea = linea.strip("\n").split(",")
                if linea[0] != "nombre":
                    programones = linea[1].split(";")
                    for i in range(len(programones)):
                        for j in range(len(self.programones_totales)):
                            if programones[i] == self.programones_totales[j].nombre:
                                programones[i] = self.programones_totales[j]
                    objetos = linea[3].split(";")
                    for i in range(len(objetos)):
                        for j in range(len(self.objetos_totales)):
                            if objetos[i] == self.objetos_totales[j].nombre:
                                objetos[i] = self.objetos_totales[j]
                    entrenador = Entrenador(nombre=linea[0], programones=programones,\
                                            energia=int(linea[2]), objetos=objetos)
                    self.entrenadores.append(entrenador)
                    