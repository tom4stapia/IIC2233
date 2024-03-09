import tablero
import parametros
import os
import funciones


# SE CREA UNA FUNCION RECURSIVA PARA CUANDO EL JUGADOR JUEGUE.
def jugar(tablero_mostrar, tablero_puntajes, bestias, usuario, puntaje):
    ruta_usuario = os.path.join("partidas", str(usuario)+".txt")
    ruta_puntajes = "puntajes.txt"
    opciones_menu = ["1", "2", "3"]
    opcion_menu = "a"
    if puntaje == 0:
        tablero.print_tablero(tablero_mostrar)
    # SE OFRECE EL MENU DE JUEGO.
    while opcion_menu not in opciones_menu:
        print("\nMenu del juego: \n[1] Descubrir sector.")
        print("[2] Guardar partida. \n[3] Salir de la partida.")
        opcion_menu = input("Ingrese su opción: ")

    if opcion_menu == "1":
        print("\nSeleccione una fila y una columna:")
        # EL JUGADOR PUEDE INGRESAR UN STRING POR ERROR, POR ESO SE REVISA.
        # TAMBIEN PUEDE EXCEDER LOS LIMITES.
        posible_fila = (input("Fila: "))
        fila = funciones.obtener_fila(tablero_mostrar, posible_fila)
        posible_columna = input("Columna: ")
        columna = funciones.obtener_columna(tablero_mostrar, posible_columna)
        # SI INGRESA LUGAR YA DESCUBIERTO SE PIDE NUEVAMENTE FILA Y COLUMNA.
        while tablero_mostrar[fila][columna] != " ":
            print("\nInserte una posicion no descubierta...\n")
            posible_fila = (input("Fila: "))
            fila = funciones.obtener_fila(tablero_mostrar, posible_fila)
            posible_columna = (input("Columna: "))
            columna = funciones.obtener_columna(tablero_mostrar, posible_columna)
        if tablero_puntajes[fila][columna] != "N":
            # SE CAMBIA EL VALOR DEL TABLERO QUE SE MUESTRA.
            # AL NO SER UNA BESTIA, SE AGREGA PUNTAJE.
            tablero_mostrar[fila][columna] = str(tablero_puntajes[fila][columna])
            puntaje += 1
            tablero.print_tablero(tablero_mostrar)
            # SE VERIFICA SI GANA
            gana_jugador = funciones.gano(tablero_mostrar, bestias)
            if gana_jugador is True:
                print("HAS GANADO")
                total_puntaje = bestias * puntaje * int(parametros.POND_PUNT)
                # SE CALCULA EL PUNTAJE TOTAL PARA GUARDAR ARCHIVO.
                with open(ruta_usuario, "w") as archivo:
                    archivo.write(str(total_puntaje))
                # SE AGREGA A PUNTAJES LO OBTENIDO.
                with open(ruta_puntajes, "a") as archivo:
                    archivo.write(usuario+","+str(total_puntaje)+"\n")
                # SE VUELVE AL MENU DE INICIO.               
                os.system("python menu_inicio.py") 
            
            else:
                # SI NO GANA SE VUELVE A OFRECER EL MENU DE JUEGO.
                jugar(tablero_mostrar, tablero_puntajes, bestias, usuario, puntaje)
        
        else:
            # SI PIERDE SE CREA ARCHIVO CON PUNTAJE.
            # SE CREA EL TABLERO CON TODAS LAS BESTIAS.
            tablero_perder = funciones.transformar_perder(tablero_mostrar, tablero_puntajes)
            print("Has perdido.\n")
            tablero.print_tablero(tablero_perder)
            total_puntaje = bestias * puntaje * int(parametros.POND_PUNT)
            
            with open(ruta_usuario, "w") as archivo:
                archivo.write(str(total_puntaje))
                
            with open(ruta_puntajes, "a") as archivo:
                archivo.write(usuario+","+str(total_puntaje)+"\n")             
            
            os.system("python menu_inicio.py")
    
    else:
        # EL CASO DE GUARDAR Y SALIR SON SIMILARES
        # SI GUARDA O SALE CON GUARDAR COMPARTEN PROCESO.
        # SI NO GUARDA NO SE MODIFICA O CREA ARCHIVO DEL JUGADOR.
        guardar = " "
        if opcion_menu == "3":
            correcto = ["1", "0"]
            print("[0] Guardar partida\n[1] No guardar partida")
            guardar = input("Ingrese opcion: ")
            while guardar not in correcto:
                guardar = input("Ingrese opcion valida: ")
        if guardar == "0" or opcion_menu == "2":
            tablero_mostrar_archivo = funciones.lista_a_archivo(tablero_mostrar)
            tablero_puntajes_archivo = funciones.lista_a_archivo(tablero_puntajes)
            datos_jugador = usuario+"\nFIN\n"+str(puntaje)+"\nFIN\n"+str(bestias)+"\nFIN\n"
            datos_partida = tablero_mostrar_archivo+tablero_puntajes_archivo+datos_jugador

            with open(ruta_usuario, "w") as archivo:
                archivo.write(datos_partida)
            
            os.system("python menu_inicio.py")
        
        else:
            os.system("python menu_inicio.py")