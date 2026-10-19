numeri = []

riga = input("Numero, oppure riga vuota per terminare: ")

while riga != "":
    numeri.append(int(riga))
    riga = input("Numero, oppure riga vuota per terminare: ")

if len(numeri) < 2:
    print("Errore")
else:
    somma = 0
    somma_assoluti = 0
    prodotto = 1

    for numero in numeri:

        somma = somma + numero

        if numero < 0:
            somma_assoluti = somma_assoluti - numero
        else:
            somma_assoluti = somma_assoluti + numero

        prodotto = prodotto * numero

    media = somma / len(numeri)

    print("Somma:", somma)
    print("Somma assoluti:", somma_assoluti)
    print("Prodotto:", prodotto)
    print("Media:", media)