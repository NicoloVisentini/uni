def recMin(lista):
    if len(lista) == 1:
        min = lista[0]
    else:
        min_resto = recMin(lista[1:])
        if lista[0] < min_resto:
            min = lista[0]
        else:
            min = min_resto

    return min


lunghezza = int(input("Lunghezza lista: "))

while lunghezza <= 0:
    print("Lunghezza non valida, riprova: ")
    lunghezza = int(input())

lista = []

i = 0
while i < lunghezza:
    numero = int(input("Numero: "))
    lista.append(numero)
    i = i + 1

    print("Il minimo e': ", recMin(lista))