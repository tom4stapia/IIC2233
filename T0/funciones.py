# Aca las funciones, Completar tablero, Generar ranking...
import random


# SE REVISA SI GANA, IGUALANDO BESTIAS CON CASILLAS RESTANTES.
def gano(lista, bestias):
    bestias = int(bestias)
    contador = 0
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            if lista[i][j] == " ":
                contador += 1
    if bestias == contador:
        return True
    else:
        return False


# SE TRANSFORMA EL TABLERO A ARCHIVO.
def lista_a_archivo(lista):
    texto_tablero = ""
    for i in range(len(lista)):
        texto_por_fila = ""
        for j in range(len(lista[0])):
            texto_por_fila += str(lista[i][j])+","
        texto_por_fila = texto_por_fila.strip(",") 
        texto_por_fila += "\n"
        texto_tablero += texto_por_fila
    texto_tablero += "FIN\n"
    return texto_tablero


# SE COMPLETA EL TABLERO CON BESTIAS.
# LUEGO SE INGRESAN VALORES, SI HAY UNA BESTIA SE REVISA AL REDEDORES.
# SI HAY BESTIA SE SUMA UNO.
# DEPENDIENDO DEL LUGAR DEL TABLERO SE UTILIZA MECANISMO PARA REVISAR.
def completar_tablero(lista, bestias):
    for i in range(bestias):
        fila = random.randint(0, len(lista)-1)
        columna = random.randint(0, len(lista[0])-1)
        while lista[fila][columna] == "N":
            fila = random.randint(0, len(lista)-1)
            columna = random.randint(0, len(lista[0])-1)
        
        lista[fila][columna] = "N"
    
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            if lista[i][j] == "N":
                if i == 0 and j == 0:
                    if lista[i][j+1] != "N":
                        lista[i][j+1] += 1
                    if lista[i+1][j] != "N":
                        lista[i+1][j] += 1
                    if lista[i+1][j+1] != "N":
                        lista[i+1][j+1] += 1

                elif i == 0 and j == len(lista[0]) - 1:
                    if lista[i][j-1] != "N":
                        lista[i][j-1] += 1
                    if lista[i+1][j] != "N":
                        lista[i+1][j] += 1
                    if lista[i+1][j-1] != "N":
                        lista[i+1][j-1] += 1
                
                elif i == len(lista) - 1 and j == 0:
                    if lista[i][j+1] != "N":
                        lista[i][j+1] += 1
                    if lista[i-1][j] != "N":
                        lista[i-1][j] += 1
                    if lista[i-1][j+1] != "N":
                        lista[i-1][j+1] += 1

                elif i == len(lista) - 1 and j == len(lista[0]) - 1:
                    if lista[i][j-1] != "N":
                        lista[i][j-1] += 1
                    if lista[i-1][j] != "N":
                        lista[i-1][j] += 1
                    if lista[i-1][j-1] != "N":
                        lista[i-1][j-1] += 1
                
                elif i == 0:
                    if lista[i][j+1] != "N":
                        lista[i][j+1] += 1
                    if lista[i+1][j] != "N":
                        lista[i+1][j] += 1
                    if lista[i+1][j+1] != "N":
                        lista[i+1][j+1] += 1
                    if lista[i+1][j-1] != "N":
                        lista[i+1][j-1] += 1
                    if lista[i][j-1] != "N":
                        lista[i][j-1] += 1
                
                elif i == len(lista) - 1:
                    if lista[i][j-1] != "N":
                        lista[i][j-1] += 1
                    if lista[i-1][j] != "N":
                        lista[i-1][j] += 1
                    if lista[i-1][j-1] != "N":
                        lista[i-1][j-1] += 1
                    if lista[i-1][j+1] != "N":
                        lista[i-1][j+1] += 1
                    if lista[i][j+1] != "N":
                        lista[i][j+1] += 1
                
                elif j == 0:
                    if lista[i][j+1] != "N":
                        lista[i][j+1] += 1
                    if lista[i+1][j] != "N":
                        lista[i+1][j] += 1
                    if lista[i+1][j+1] != "N":
                        lista[i+1][j+1] += 1
                    if lista[i-1][j] != "N":
                        lista[i-1][j] += 1
                    if lista[i-1][j+1] != "N":
                        lista[i-1][j+1] += 1
                
                elif j == len(lista[0]) - 1:
                    if lista[i][j-1] != "N":
                        lista[i][j-1] += 1
                    if lista[i-1][j] != "N":
                        lista[i-1][j] += 1
                    if lista[i-1][j-1] != "N":
                        lista[i-1][j-1] += 1
                    if lista[i+1][j] != "N":
                        lista[i+1][j] += 1
                    if lista[i+1][j-1] != "N":
                        lista[i+1][j-1] += 1
                
                else:
                    if lista[i][j-1] != "N":
                        lista[i][j-1] += 1
                    if lista[i-1][j] != "N":
                        lista[i-1][j] += 1
                    if lista[i-1][j-1] != "N":
                        lista[i-1][j-1] += 1
                    if lista[i+1][j] != "N":
                        lista[i+1][j] += 1
                    if lista[i+1][j-1] != "N":
                        lista[i+1][j-1] += 1
                    if lista[i][j+1] != "N":
                        lista[i][j+1] += 1
                    if lista[i+1][j+1] != "N":
                        lista[i+1][j+1] += 1
                    if lista[i-1][j+1] != "N":
                        lista[i-1][j+1] += 1

    return lista


# FUNCION PARA ORDENAR RANKING
def ranking(lista):
    return lista[1]


# FUNCION PARA RETORNAR TABLERO CON TODAS LAS BESTIAS.
def transformar_perder(tablero_m, tablero_v):
    for i in range(len(tablero_m)):
        for j in range(len(tablero_m[0])):
            if tablero_m[i][j] == " " and tablero_v[i][j] == "N":
                tablero_m[i][j] = "N"
    return tablero_m


# FUNCION PARA OBTENER UNA FILA VALIDA.
def obtener_fila(tablero, valor):
    if valor.isdigit() is False:
        print("Ingrese un valor numerico dentro del rango permitido.\n")
        while valor.isdigit() is False:
            valor = (input("Fila: "))
    while int(valor) >= len(tablero):
        print("Ingrese una fila dentro del rango permitido.\n")
        valor = (input("Fila: "))
        if valor.isdigit() is False:
            print("Ingrese un valor numerico dentro del rango permitido.\n")
            while valor.isdigit() is False:
                valor = (input("Fila: "))
    return int(valor)


# FUNCION PARA OBTENER UNA COLUMNA VALIDA.
def obtener_columna(tablero, valor):
    if valor.isdigit() is False:
        print("Ingrese un valor numerico dentro del rango permitido.\n")
        while valor.isdigit() is False:
            valor = (input("Columna: "))
    while int(valor) >= len(tablero[0]):
        print("Ingrese una columna dentro del rango permitido.\n")
        valor = (input("Columna: "))
        if valor.isdigit() is False:
            print("Ingrese un valor numerico dentro del rango permitido.\n")
            while valor.isdigit() is False:
                valor = (input("Columna: "))
    return int(valor)
