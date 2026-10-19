numero = int(input("Inserisci un numero intero positivo: "))

if numero <= 0:
    print("Errore")
else:
    divisore = 2

    while numero > 1:
        if numero % divisore == 0:
            print(divisore)
            numero = numero // divisore
        else:
            divisore = divisore + 1