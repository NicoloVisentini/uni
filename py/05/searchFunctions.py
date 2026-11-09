def linearSearch(lista, valore):
    posizione = -1
    i = 0
    while i < len(lista) and posizione == -1:
        if lista[i] == valore:
            posizione = i
        i = i + 1

    return posizione

def iterativeBinarySearch(lista, valore):
    posizione = -1
    sinistra = 0
    destra = len(lista) - 1

    while sinistra <= destra and posizione == -1:
        centro = (sinistra + destra) // 2

        if lista[centro] == valore:
            posizione = centro
        elif lista[centro] < valore:
            sinistra = centro + 1
        else:
            destra = centro - 1

    return posizione

def recursiveBinarySearch(lista, valore, sx, dx):
    if sx > dx:
        posizione = -1
    else:
        centro = (sx + dx) // 2

        if lista[centro] == valore:
            posizione = centro
        elif lista[centro] < valore:
            posizione = recursiveBinarySearch(lista, valore, centro + 1, dx)
        else:
            posizione = recursiveBinarySearch(lista, valore, sx, centro - 1)

    return posizione


lista = []
lunghezza = int(input("Inserisci lunghezza lista: "))

for i in range(0, lunghezza):
    numero = int(input("Numero: "))
    lista.append(numero)

lista.sort()

valore = int(input("Valore da cercare: "))

print("Lista ordinata: ", lista)


posizione = linearSearch(lista, valore)

if posizione == -1:
    print("Il valore non e' presente nella lista")
else:
    print("Il valore si trova alla posizione ", posizione)


posizione = iterativeBinarySearch(lista, valore)

if posizione == -1:
    print("Il valore non e' presente nella lista")
else:
    print("Il valore si trova alla posizione ", posizione)


sx = 0
dx = len(lista) - 1

posizione = recursiveBinarySearch(lista, valore, sx, dx)

if posizione == -1:
    print("Il valore non e' presente nella lista")
else:
    print("Il valore si trova alla posizione ", posizione)
