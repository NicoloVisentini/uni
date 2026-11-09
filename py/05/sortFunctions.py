def selectionSort(lista):

    i = 0
    while i < len(lista) - 1:
        min = i
        j = i + 1

        while j < len(lista):
            if lista[j] < lista[min]:
                min = j
            j = j + 1

        temp = lista[i]
        lista[i] = lista[min]
        lista[min] = temp
        i = i + 1
        
    return lista


def insertionSort(lista):

    i = 1
    while i < len(lista):
        valore = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valore:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = valore
        i = i + 1

    return lista


def mergeSort(lista):
    if len(lista) <= 1:
        risultato = lista[:]
    else:
        centro = len(lista) // 2
        sinistra = mergeSort(lista[:centro])
        destra = mergeSort(lista[centro:])
        risultato = merge(sinistra, destra)

    return risultato

def merge(sinistra, destra):
    risultato = []
    i = 0
    j = 0

    while i < len(sinistra) and j < len(destra):
        if sinistra[i] <= destra[j]:
            risultato.append(sinistra[i])
            i = i + 1
        else:
            risultato.append(destra[i])
            j = j + 1

    while i < len(sinistra):
        risultato.append(sinistra[i])
        i = i + 1

    while j < len(destra):
        risultato.append(destra[j])
        j = j + 1

    return risultato
    

# main
lunghezza = int(input("Lunghezza lista: "))

while lunghezza <= 0:
    print("Lunghezza non valida, riprova: ")
    lunghezza = int(input)

lista = []

i = 0
while i < lunghezza:
    numero = int(input("Numero: "))
    lista.append(numero)
    i = i + 1

if lunghezza == 1:
    print("La lista con un solo numero e' gia' ordinata: ", lista)
else:
    print("Lista inizile: ", lista)

    lista_selectionSort = selectionSort(lista)
    lista_insertionSort = insertionSort(lista)
    lista_mergeSort = mergeSort(lista)

    print("Lista ordinata con selectionSort: ", lista_selectionSort)
    print("Lista ordinata con insertionSort: ", lista_insertionSort)
    print("Lista ordinata con mergeSort: ", lista_mergeSort)
