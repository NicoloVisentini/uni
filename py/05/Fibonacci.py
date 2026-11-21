n = int(input("n positivo: "))
if n <= 0:
    print("Input non valido.")
else:
    precedente = 1
    corrente = 1
    i = 2
    while i < n:
        successivo = precedente + corrente
        precedente = corrente
        corrente = successivo
        i = i + 1
    print(corrente)