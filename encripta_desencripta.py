import os

# Definicion de funciones:


def encrypt_decrypt(base, exp, modulo):
    iterador = 1
    c = base

    while iterador < exp:
        c = (c * base) % modulo
        iterador += 1

    return c


def ascii2char(ascode):
    new_letra = chr(ascode)
    return new_letra


def char2ascii(caracter):
    new_ascii = ord(caracter)
    return new_ascii


print("################# ENCRIPTADOR / DESENCRIPTADOR #################\n")
# LLAVE PUBLICA: 3233
print("1. Encriptar")  # Llave: 17
print("2. Desencriptar")  # Llave: 2753
eleccion = int(input("   >_ "))
os.system("clear")
if eleccion == 2:
    print("Ingresar los ASCIIs a desencriptar:\n")
    asciis_sep = input("   >_ ")

    asciis = asciis_sep.split('|')

    des_asciis = []
    for encr_ascii in asciis:
        des_asciis.append(encrypt_decrypt(int(encr_ascii), 2753, 3233))

    frase = ""
    for ascii in des_asciis:
        frase += ascii2char(ascii)

    os.system("clear")
    print("Frase desencriptada:\n")
    print(frase)
elif eleccion == 1:
    print("Ingresar palabra(s) a encriptar:\n")
    palabras = input("   >_ ")

    asciis_a_encriptar = []
    for eachar in palabras:
        asciis_a_encriptar.append(char2ascii(eachar))

    encriptado = []
    for el_ascii in asciis_a_encriptar:
        encriptado.append(encrypt_decrypt(el_ascii, 17, 3233))

    frase_encriptada = ""
    for it in range(0, len(encriptado)):
        frase_encriptada += str(encriptado[it])+"|"

    frase_encriptada = frase_encriptada[:len(frase_encriptada)-1]
    print("La frase encriptada es:\n")
    print(frase_encriptada)
