import sys
from liga_progra import LigaProgramon
from beautifultable import BeautifulTable


class DCCampeonatoProgramon:
    def __init__(self, liga):
        self.liga = liga
        self.entrenador_elegido = None

    def reiniciar(self):
        # PARA REINICIAR CREO OTRO OBJETO DE AMBAS CLASES
        nueva_liga = LigaProgramon()
        nuevo_campeonato = DCCampeonatoProgramon(nueva_liga)
        nuevo_campeonato.empezar()
    
    def empezar(self):
        self.menu_inicio()

    def menu_inicio(self):
        # ### CITADO Y ADAPTADO ###
        # LINK EN README
        subtable = BeautifulTable()
        subtable.rows.append([" ", "Entrenador", "Programon(es)"])
        for i in range(len(self.liga.entrenadores)):
            lista = []
            lista.append(f"[{str(i+1)}]")
            lista.append(self.liga.entrenadores[i].nombre)
            programones = []
            for j in range(len(self.liga.entrenadores[i].programones)):
                programones.append(self.liga.entrenadores[i].programones[j].nombre)
            texto_programones = ("\n".join(programones))
            lista.append(texto_programones)
            subtable.rows.append(lista)
        subtable.rows.append([f"[{str(len(self.liga.entrenadores)+1)}]", "Salir", " "])
        subtable.border.left = ''
        subtable.border.right = ''
        subtable.border.top = ''
        subtable.border.right = ''
        subtable.border.bottom = ''

        table = BeautifulTable()
        table.columns.header = ["Menu de Inicio"]
        table.rows.append([subtable])
        table.columns.padding_left[0] = 0
        table.columns.padding_right[0] = 0
        table.set_style(BeautifulTable.STYLE_COMPACT)
        print(table)
        # ### FIN DE CITADO ###
        opciones = [str(n+1) for n in range(len(self.liga.entrenadores)+1)]
        opcion = input("\nSeleccione una opcion: ")
        while opcion not in opciones:
            opcion = input("\nSeleccione una opcion valida: ")
        if opcion == str(len(self.liga.entrenadores)+1):
            sys.exit()
        if self.entrenador_elegido is None:
            self.entrenador_elegido = self.liga.entrenadores[int(opcion)-1]
            print(f"\nBienvenido {self.entrenador_elegido.nombre}!")
        print()
        self.menu_entrenador()

    def menu_entrenador(self):
        # ### CITADO Y ADAPTADO ###
        # LINK EN README
        subtable = BeautifulTable()
        subtable.rows.append(["[1]", "Entrenamiento"])
        subtable.rows.append(["[2]", "Simular Ronda"])
        subtable.rows.append(["[3]", "Resumen campeonato"])
        subtable.rows.append(["[4]", "Crear objetos"])
        subtable.rows.append(["[5]", "Utilizar objeto"])
        subtable.rows.append(["[6]", "Estado entrenador"])
        subtable.rows.append(["[7]", "Volver"])
        subtable.rows.append(["[8]", "Salir"])
        subtable.border.left = ''
        subtable.border.right = ''
        subtable.border.top = ''
        subtable.border.right = ''
        subtable.border.bottom = ''

        table = BeautifulTable()
        table.columns.header = ["Menu de Entrenador"]
        table.rows.append([subtable])
        table.columns.padding_left[0] = 0
        table.columns.padding_right[0] = 0
        table.set_style(BeautifulTable.STYLE_COMPACT)
        print(table)
        # ### FIN DE CITADO ###
        opciones = [str(n+1) for n in range(8)]
        opcion = input("\nSeleccione una opcion: ")
        while opcion not in opciones:
            opcion = input("\nSeleccione una opcion valida: ")
        print()
        # SE ELIGE OPCION DEL MENU ENTRENADOR
        if opcion == "1":
            # ENTRENA PROGRAMON
            self.entrenador_elegido.menu_entrenamiento()
            # SE VUELVE AL MENU DE INICIO
            self.menu_entrenador()
        
        elif opcion == "2":
            # SE SIMULA UNA RONDA
            self.liga.simular_ronda(self.entrenador_elegido)
            # SE REVISA SI PERDIO O ES CAMPEON
            if self.entrenador_elegido in self.liga.perdedores or self.liga.campeon is not None:
                if self.entrenador_elegido in self.liga.perdedores:
                    if self.liga.campeon is not None:
                        print(f"{self.liga.campeon.nombre} ha ganado el campeonato!")
                    print(f"{self.entrenador_elegido.nombre} ha perdido! Reiniciando programa...")
                    print()
                elif self.liga.campeon is not None:
                    print(f"{self.liga.campeon.nombre} ha ganado el campeonato!")
                    print("Reiniciando programa...\n")
                self.reiniciar()
            else:
                # SI NO PIERDE O ES CAMPEON SE VUELVE AL MENU DE ENTRENADOR
                self.menu_entrenador()

        elif opcion == "3":
            # SE IMPRIME MENU DE ENTRENADOR
            self.liga.resumen_campeonato()
            print()
            self.menu_entrenador()

        elif opcion == "4":
            # SE CREA UN OBJETO
            self.entrenador_elegido.crear_objeto(self.liga.objetos_totales)
            self.menu_entrenador()
            
        elif opcion == "5":
            # SE APLICA OBJETO A PROGRAMON
            self.entrenador_elegido.menu_objetos()
            self.menu_entrenador()

        elif opcion == "6":
            # SE REVISA ESTADO DEL ENTRENADOR
            self.entrenador_elegido.estado_entrenador()
            self.menu_entrenador()

        elif opcion == "7":
            # AL VOLVER EN EL MENU DE ENTRENADOR SE REINICIA EL JUEGO
            # NO PUEDE RETOMAR COMO OTRO ENTRENADOR
            self.reiniciar()
        
        elif opcion == "8":
            sys.exit()
            