def sommaPrimi(numero):
    if numero == 1:
        risultato = 1
    else:
        risultato = numero + sommaPrimi(numero - 1)
        
    return risultato


numero = int(input("Numero intero positivo: "))

if numero <= 0:
    print("Errore")
else:
    print(sommaPrimi(numero))