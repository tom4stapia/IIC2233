import math
import parametros
import os
import funciones
import sys
import menu_juego
import tablero


print("Seleccione una opción: \n[1] Crear partida \n[2] Cargar partida")
print("[3] Ver ranking\n[0] Salir")

opcion = 10
opciones = ["0", "1", "2", "3"]
# SE LE PIDE AL USUARIO QUE INGRESE UNA OPCION VALIDA.
while opcion not in opciones:
    opcion = (input("Indique su opción (0, 1, 2 o 3): "))

    if opcion not in opciones:
        print("\nDebes ingresar una opción valida.\n")

# SI LA OPCION ES SALIR, CIERRA EL PROGRAMA.
if opcion == "0":
    sys.exit()

elif opcion == "1":
    print("BIENVENIDO!")
    usuario = input("Por favor ingresa tu nombre de usuario: ")
    archivo_usuario = usuario+".txt"
    # SE REVISA QUE EL USUARIO NO ESTE EN LA CARPETA PARTIDAS.
    # CASO CONTRARIO VUELVE AL MENU DE INICIO.
    if archivo_usuario not in os.listdir("partidas"):
        # SE PIDEN DIMENSIONES PARA CREAR TABLERO.
        dimensiones = []
        for i in range(2, 15):
            dimensiones.append(str(i+1))
        filas = ""
        columnas = ""
        print("Ingrese las dimensiones del tablero, deben ser entre 3 y 15 ambos incluidos.")
        while filas not in dimensiones:
            filas = (input("Número de filas: "))

            if filas not in dimensiones:
                print("\nDebes ingresar una opción valida.\n")

        while columnas not in dimensiones:
            columnas = (input("Número de columnas: "))

            if columnas not in dimensiones:
                print("\nDebes ingresar una opción valida.\n")
        filas = int(filas)
        columnas = int(columnas)
        print("\nCREANDO TABLERO...\n")

        # DEFINO NUMERO DE BESTIAS
        numero_de_bestias = math.ceil(filas * columnas * (parametros.PROB_BESTIA))
        # SE UTILIZAN DOS LISTAS DISTINTAS.
        # TABLERO 1 ES LA QUE INGRESA EN UNA FUNCION QUE LA RELLENA DE VALORES.
        # TABLERO MOSTRAR ES EL QUE INGRESA EN LA FUNCION QUE SE OTORGA.
        tablero_1 = []
        tablero_mostrar = []
        for i in range(filas):
            lista_fila = []
            lista_fm = []
            for j in range(columnas):
                lista_fila.append(0)
                lista_fm.append(" ")
            tablero_1.append(lista_fila)
            tablero_mostrar.append(lista_fm)

        print(f"{numero_de_bestias} BESTIAS INGRESANDO AL JUEGO...\n")

        tablero_puntajes = funciones.completar_tablero(tablero_1, numero_de_bestias)
        # TABLERO MOSTRAR TIENE POSICIONES OCULTAS, TABLERO PUNTAJES EL VALOR DE CADA CASILLA.
        # SE LLAMA AL MENU DE JUEGO
        menu_juego.jugar(tablero_mostrar, tablero_puntajes, numero_de_bestias, usuario, 0)    
    else:
        print("El usuario ya ha sido creado. Intentelo nuevamente.")
        os.system("python menu_inicio.py")

elif opcion == "2":
    print("BIENVENIDO DE VUELTA!")
    usuario = input("Por favor ingresa tu nombre de usuario: ")
    archivo_usuario = usuario+".txt"
    # SE REVISA QUE EL USUARIO YA HAYA SIDO CREADO.
    # CASO CONTRARIO SE VUELVE AL MENU DE INICIO.
    if archivo_usuario not in os.listdir("partidas"):
        print("No existe registro de ese usuario. Vuelve a intentarlo.")
        os.system("python menu_inicio.py")   
    else:
        # SE ABRE ARCHIVO QUE CONTIENE LOS DATOS DE LA PARTIDA DEL USUARIO.
        # LOS JUGADORES QUE HAYAN FINALIZADO LA PARTIDA, TIENEN UN ARCHIVO CON SU PUNTAJE.
        ruta_usuario = os.path.join("partidas", archivo_usuario)
        with open(ruta_usuario, "r") as archivo:
            lista_jugar = archivo.readlines()
        if len(lista_jugar) == 1:
            print("Su partida ha finalizado. Vuelve a intentarlo.")
            os.system("python menu_inicio.py")
        else:
            # SE GUARDAN EN VARIABLES LOS DATOS DE LA PARTIDA EN CURSO.
            # SE DISTINGUEN PORQUE ESTAN SEPARADOS POR STRING FIN\n
            tablero_mostrar = []
            tablero_valores = []
            contador = 0           
            for i in range(len(lista_jugar)):
                if lista_jugar[i] == "FIN\n":
                    contador = i
                    break
                tablero_mostrar.append(lista_jugar[i].strip("\n").split(","))            
            for i in range(contador + 1, len(lista_jugar)):
                if lista_jugar[i] == "FIN\n":
                    contador = i
                    break
                tablero_valores.append(lista_jugar[i].strip("\n").split(","))
            lista_final = []
            for i in range(contador + 1, len(lista_jugar), 2):
                lista_final.append(lista_jugar[i].strip("\n"))           
            usuario = lista_final[0]
            puntaje = int(lista_final[1])
            bestias = int(lista_final[2])
            if puntaje != 0:
                tablero.print_tablero(tablero_mostrar)
            # SE VUELVE A JUGAR.
            menu_juego.jugar(tablero_mostrar, tablero_valores, bestias, usuario, puntaje)
elif opcion == "3":
    # SE ABRE EL ARCHIVO PUNTAJES.TXT
    # SE GUARDAN LOS DATOS EN UNA LISTA.
    # SE TRANSFORMA A INT LOS PUNTAJES.
    ruta_puntajes = "puntajes.txt"
    ranking_desorden = []
    with open(ruta_puntajes, "r") as archivo:
        for linea in archivo:
            ranking_desorden.append(linea.strip("\n").split(","))
    for i in range(len(ranking_desorden)):
        ranking_desorden[i][1] = int(ranking_desorden[i][1])
    # SE ORDENA EN UNA NUEVA LISTA DE MAYOR A MENOR LOS PUNTAJES.
    ranking_oficial = sorted(ranking_desorden, key=funciones.ranking, reverse=True)
    # SE REVISA SI ALGUIEN YA HA FINALIZADO LA PARTIDA.
    # CASO CONTRARIO SE COMPARA SI HAY MAS DE 10 O NO.
    if len(ranking_desorden) == 0:
        print("Nadie ha terminado una partida.")
    else:
        if len(ranking_oficial) < 10:
            for i in range(len(ranking_oficial)):
                nombre = ranking_oficial[i][0]
                puntaje = ranking_oficial[i][1]
                lugar = i+1
                print(f"En {lugar} lugar: {nombre} con {puntaje} puntos.")
        else:
            for i in range(10):
                nombre = ranking_oficial[i][0]
                puntaje = ranking_oficial[i][1]
                lugar = i+1
                print(f"En {lugar} lugar: {nombre} con {puntaje} puntos.")
    # SE VUELVE AL MENU DE INICIO.
    os.system("python menu_inicio.py")
