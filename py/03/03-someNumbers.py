somma = 0
somma_assoluti = 0
prodotto = 1
contatore = 0

riga = input(print("Numero, oppure riga vuota per terminare: "))

while(riga != ""):
    numero = int(riga)
    somma = somma + numero

    if(numero < 0):
        somma_assoluti = somma_assoluti - numero
    else:
        somma_assoluti = somma_assoluti + numero

    prodotto = prodotto * numero

    contatore = contatore + 1

    riga = input(print("Numero, oppure riga vuota per terminare: "))

if(contatore < 2):
    print("Errore, servono almeno due numeri")
else:
    valore_medio = somma / contatore

    print("Somma:", somma)
    print("Somma assoluti:", somma_assoluti)
    print("Prodotto:", prodotto)
    print("Valore medio:", valore_medio)