import os

# Definicion de funciones:


def ordenamiento_burbuja(lista):
    for iterador in range(0, len(lista)-1):
        for j in range(0, len(lista)-1):
            n1 = float(lista[j])
            n2 = float(lista[j+1])
            if n1 > n2:
                content = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = content
    return lista


print "################# ORDENAMIENTO BURBUJA #################\n"
print "Ingrese la cantidad de numeros a ordenar:\n"
cant = input("   >_ ")

os.system("cls")

print "################# ORDENAMIENTO BURBUJA #################\n"

numeros = []
for i in range(0, cant):
    print "Ingrese el numero #%i:\n" % (i+1)
    numeros.append(raw_input("   >_ "))

os.system("pause")
os.system("cls")

print "################# ORDENAMIENTO BURBUJA #################\n"
print "Numeros a ordenar:\n"
output = ""
for item in numeros:
    output += "     " + item
print(output)

new_lista = ordenamiento_burbuja(numeros)

output = ""
print "Numeros ordenados:\n"
for item2 in new_lista:
    output += "     " + item2
print(output)

os.system("pause")
