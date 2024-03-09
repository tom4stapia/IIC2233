import os
import json


def data_json(key):
    ruta = os.path.join("parametros.json")
    with open(ruta, 'r', encoding="UTF-8") as archivo:
        data = json.load(archivo)
    valor = data[key]
    return valor


def encriptar(msg: bytearray) -> bytearray:
    # Completar con el proceso de encriptación
    A = []
    B = []
    C = []
    for i in range(0, len(msg), 3):
        if i < len(msg):
            A.append(msg[i])
        if i + 1 < len(msg):
            B.append(msg[i+1])
        if i + 2 < len(msg):
            C.append(msg[i+2])
    suma_mitad_b = 0
    for i in range(1, len(B) - 1):
        suma_mitad_b += B[i]
    valor = A[0] + suma_mitad_b + C[-1]
    mensaje = bytearray()
    if valor % 2 == 0:
        mensaje.extend(b'\x00')
        mensaje.extend(bytes(C))
        mensaje.extend(bytes(A))
        mensaje.extend(bytes(B))
    else:
        mensaje.extend(b'\x01')
        mensaje.extend(bytes(A))
        mensaje.extend(bytes(C))
        mensaje.extend(bytes(B))
    return mensaje


def desencriptar(msg: bytearray) -> bytearray:
    # Completar con el proceso de desencriptación
    mensaje = []
    A = []
    B = []
    C = []
    for i in range(1, len(msg)):
        mensaje.append(msg[i])
    largo = len(mensaje)
    if largo % 3 == 2:
        largo_a = largo//3 + 1
        largo_b = largo//3 + 1
        largo_c = largo//3
    
    elif largo % 3 == 1:
        largo_a = largo//3 + 1
        largo_b = largo//3
        largo_c = largo//3
    else:
        largo_a = largo//3
        largo_b = largo//3
        largo_c = largo//3
    
    n = msg[0]
    if n == 0:
        C = mensaje[:largo_c]
        A = mensaje[largo_c: largo_c + largo_a]
        B = mensaje[largo_a + largo_c:]
    else:
        A = mensaje[:largo_a]
        C = mensaje[largo_a: largo_c + largo_a]
        B = mensaje[largo_a + largo_c:]
    M = []
    for i in range(len(A)):
        if i < len(A):
            M.append(A[i])
        if i < len(B):
            M.append(B[i])
        if i < len(C):
            M.append(C[i])

    msg_real = bytearray()
    msg_real.extend(bytes(M))

    return msg_real


if __name__ == "__main__":
    # Testear encriptar
    msg_original = bytearray(b'\x05\x08\x03\x02\x04\x03\x05\x09\x05\x09\x01')
    msg_esperado = bytearray(b'\x01\x05\x02\x05\x09\x03\x03\x05\x08\x04\x09\x01')

    msg_encriptado = encriptar(msg_original)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")
    
    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado)
    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")
