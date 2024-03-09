from parametros import ENERGIA_ENTRENAMIENTO
import sys
from random import randint, random
from beautifultable import BeautifulTable


class Entrenador:
    def __init__(self, nombre, energia: int, programones, objetos):
        self.nombre = nombre
        self._energia = energia
        self.programones = programones
        self.objetos = objetos

    @property
    def energia(self):
        return self._energia
    
    @energia.setter
    def energia(self, agregar):
        if agregar > 100:
            self._energia = 100
        elif agregar < 0:
            self._energia = 0
        else:
            self._energia = agregar
        return self._energia

    def estado_entrenador(self):
        lista_objetos = []
        for i in range(len(self.objetos)):
            lista_objetos.append(self.objetos[i].nombre)
        objetos = (", ".join(lista_objetos))
        # SE IMPRIME ESTADO ENTRENADOR Y PROGRAMONES
        # ### CITADO Y ADAPTADO ###
        table = BeautifulTable()
        table.columns.header = ["Estado entrenador"]
        table.rows.append([f"Nombre: {self.nombre}\nEnergia: {self.energia}\nObjetos: {objetos}"])
        table.columns.alignment = BeautifulTable.ALIGN_LEFT
        table.columns.padding_left[0] = 0
        table.columns.padding_right[0] = 0
        table.border.bottom = ''
        print(table)
        subtable = BeautifulTable()
        subtable.rows.append(["Nombre", "Tipo", "Nivel", "Vida"])
        for i in range(len(self.programones)):
            nombre = self.programones[i].nombre
            tipo = self.programones[i].tipo
            nivel = self.programones[i].nivel
            vida = self.programones[i].vida
            subtable.rows.append([nombre, tipo, nivel, vida])
        subtable.border.left = ''
        subtable.border.right = ''
        subtable.border.top = ''
        subtable.border.right = ''
        subtable.border.bottom = ''
        table = BeautifulTable()
        table.columns.header = ["Programones"]
        table.rows.append([subtable])
        table.columns.padding_left[0] = 0
        table.columns.padding_right[0] = 0
        print(table)
        print("[1] Volver\n[2] Salir")
        # FIN CITADO
        opciones = ["1", "2"]
        opcion = input("\nSeleccione una opcion: ")
        while opcion not in opciones:
            opcion = input("\nSeleccione una opcion valida: ")
        if opcion == "1":
            print()
        elif opcion == "2":
            sys.exit()
            
    def crear_objeto(self, objetos_totales):
        # ### CITADO Y ADAPTADO ### 
        subtable = BeautifulTable()
        subtable.rows.append(["[1]", "Baya"])
        subtable.rows.append(["[2]", "Poción"])
        subtable.rows.append(["[3]", "Caramelo"])
        subtable.rows.append(["[4]", "Volver"])
        subtable.rows.append(["[5]", "Salir"])
        subtable.border.left = ''
        subtable.border.right = ''
        subtable.border.top = ''
        subtable.border.right = ''
        subtable.border.bottom = ''

        table = BeautifulTable()
        table.columns.header = ["Menu objetos"]
        table.rows.append([subtable])
        table.columns.padding_left[0] = 0
        table.columns.padding_right[0] = 0
        table.set_style(BeautifulTable.STYLE_COMPACT)
        print(table)
        # FIN CITADO
        opciones = [str(n+1) for n in range(5)]
        opcion = input("\nIngrese una opcion: ")
        while opcion not in opciones:
            opcion = input("\nIngrese una opcion valida: ")
        # SI ELIGE BAYA
        if opcion == "1":
            # SE ELIGE CUALQUIER OBJETO DEL TIPO BAYA
            posicion_objeto = randint(0, len(objetos_totales)-1)
            while objetos_totales[posicion_objeto].tipo != "baya":
                posicion_objeto = randint(0, len(objetos_totales)-1)
            # SE REVISA QUE ENTRENADOR TENGA ENERGIA PARA CREAR OBJETO
            if self.energia - objetos_totales[posicion_objeto].gasto >= 0: 
                self.energia -= objetos_totales[posicion_objeto].gasto
                # EN CASO DE TENERLA, SI CUMPLE CON PROBABILIDAD SE CREA OBJETO
                if random() <= objetos_totales[posicion_objeto].prob_exito:
                    print(f"El objeto {objetos_totales[posicion_objeto].nombre} ha sido creado.")
                    self.objetos.append(objetos_totales[posicion_objeto])
                else:
                    print("No se logro crear el objeto")
            else:
                print("No tiene la energia suficiente para crear el objeto.")
            print()
        # SE ELIGE POCION Y OCURRE EL MISMO MECANISMO
        elif opcion == "2":
            posicion_objeto = randint(0, len(objetos_totales)-1)
            while objetos_totales[posicion_objeto].tipo != "pocion":
                posicion_objeto = randint(0, len(objetos_totales)-1)
            if self.energia - objetos_totales[posicion_objeto].gasto >= 0: 
                self.energia -= objetos_totales[posicion_objeto].gasto           
                if random() <= objetos_totales[posicion_objeto].prob_exito:
                    print(f"El objeto {objetos_totales[posicion_objeto].nombre} ha sido creado.")
                    self.objetos.append(objetos_totales[posicion_objeto])
                else:
                    print("No se logro crear el objeto")
            else:
                print("No tiene la energia suficiente para crear el objeto.")
            print()
        # SE ELIGE CARAMELO Y OCURRE EL MISMO MECANISMO
        elif opcion == "3":
            posicion_objeto = randint(0, len(objetos_totales)-1)
            while objetos_totales[posicion_objeto].tipo != "caramelo":
                posicion_objeto = randint(0, len(objetos_totales)-1)
            if self.energia - objetos_totales[posicion_objeto].gasto >= 0: 
                self.energia -= objetos_totales[posicion_objeto].gasto
                if random() <= objetos_totales[posicion_objeto].prob_exito:
                    print(f"El objeto {objetos_totales[posicion_objeto].nombre} ha sido creado.")
                    self.objetos.append(objetos_totales[posicion_objeto])
                else:
                    print("No se logro crear el objeto")
            else:
                print("No tiene la energia suficiente para crear el objeto.")
            print()
        elif opcion == "4":
            print()
        elif opcion == "5":
            sys.exit()

    def menu_entrenamiento(self):
        # ### CITADO Y ADAPTADO ###
        subtable = BeautifulTable()
        for i in range(len(self.programones)):
            subtable.rows.append([f"[{i+1}]", self.programones[i].nombre])
        subtable.rows.append([f"[{len(self.programones)+1}]", "Volver"])
        subtable.rows.append([f"[{len(self.programones)+2}]", "Salir"])
        subtable.border.left = ''
        subtable.border.right = ''
        subtable.border.top = ''
        subtable.border.right = ''
        subtable.border.bottom = ''

        table = BeautifulTable()
        table.columns.header = ["Menu de entrenamiento"]
        table.rows.append([subtable])
        table.columns.padding_left[0] = 0
        table.columns.padding_right[0] = 0
        table.set_style(BeautifulTable.STYLE_COMPACT)
        print(table)
        # FIN CITADO
        opciones = [str(n+1) for n in range(len(self.programones)+2)]
        opcion = input("\nSeleccione una opcion: ")
        while opcion not in opciones:
            opcion = input("\nSeleccione una opcion valida: ")
        if opcion == str(len(self.programones)+1):
            print()
        elif opcion == str(len(self.programones)+2):
            sys.exit()
        else:
            # SE REVISA SI TIENE ENERGIA SUFICIENTE PARA ENTRENAR PROGRAMON ELEGIDO.
            if self.energia - ENERGIA_ENTRENAMIENTO >= 0:
                print(f"La energía del entrenador {self.nombre} ha disminuido"\
                      f" en {ENERGIA_ENTRENAMIENTO}")
                self.energia -= ENERGIA_ENTRENAMIENTO
                self.programones[int(opcion)-1].entrenamiento()
            else:
                nombre_programon = self.programones[int(opcion)-1].nombre
                print(f"No tiene energia suficiente para mejorar a {nombre_programon}")
                print()

    def menu_objetos(self):
        # ### CITADO Y ADAPTADO ###
        subtable = BeautifulTable()
        for i in range(len(self.objetos)):
            subtable.rows.append([f"[{i+1}]", self.objetos[i].nombre])
        subtable.rows.append([f"[{len(self.objetos)+1}]", "Volver"])
        subtable.rows.append([f"[{len(self.objetos)+2}]", "Salir"])
        subtable.border.left = ''
        subtable.border.right = ''
        subtable.border.top = ''
        subtable.border.right = ''
        subtable.border.bottom = ''

        table = BeautifulTable()
        table.columns.header = ["Objetos disponibles"]
        table.rows.append([subtable])
        table.columns.padding_left[0] = 0
        table.columns.padding_right[0] = 0
        table.set_style(BeautifulTable.STYLE_COMPACT)
        print(table)
        # FIN CITADO
        # SE DA LA OPCION DE ELEGIR OBJETO DEL USUARIO PARA MEJORAR PROGRAMON
        opciones = [str(n+1) for n in range(len(self.objetos)+2)]
        opcion_objeto = input("\nSeleccione una opcion: ")
        while opcion_objeto not in opciones:
            opcion_objeto = input("\nSeleccione una opcion valida: ")
        if opcion_objeto == str(len(self.objetos)+1):
            pass
        elif opcion_objeto == str(len(self.objetos)+2):
            sys.exit()
        else:
            # ### CITADO Y ADAPTADO ###
            subtable = BeautifulTable()
            for i in range(len(self.programones)):
                subtable.rows.append([f"[{i+1}]", self.programones[i].nombre])
            subtable.rows.append([f"[{len(self.programones)+1}]", "Volver"])
            subtable.rows.append([f"[{len(self.programones)+2}]", "Salir"])
            subtable.border.left = ''
            subtable.border.right = ''
            subtable.border.top = ''
            subtable.border.right = ''
            subtable.border.bottom = ''

            print()
            table = BeautifulTable()
            table.columns.header = ["Elige un programon"]
            table.rows.append([subtable])
            table.columns.padding_left[0] = 0
            table.columns.padding_right[0] = 0
            table.set_style(BeautifulTable.STYLE_COMPACT)
            print(table)
            # FIN CITADO
            # SE ELIGE PROGRAMON PARA APLICAR OBJETO
            opciones = [str(n+1) for n in range(len(self.programones)+2)]
            opcion = input("\nSeleccione una opcion: ")
            while opcion not in opciones:
                opcion = input("\nSeleccione una opcion valida: ")
            if opcion == str(len(self.programones)+1):
                print()
                self.menu_objetos()
            elif opcion == str(len(self.programones)+2):
                sys.exit()
            else:
                print()
                print(f"Programon beneficiado: {self.programones[int(opcion)-1].nombre}")
                print(f"Objeto utilizado: {self.objetos[int(opcion_objeto)-1].nombre} "\
                      f"(tipo {self.objetos[int(opcion_objeto)-1].tipo})")
                self.objetos[int(opcion_objeto)-1].aplicar_objeto(self.programones[int(opcion)-1])
                self.objetos.remove(self.objetos[int(opcion_objeto)-1])
                print()
