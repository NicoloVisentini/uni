n = int(input("Inserisci un numero: "))

if(n <= 0):
    print("Input non valido")
else:
    print("***STAMPA DEI NUMERI DA 1 A N***")
    print("N?:", n)
    for i in range(1, n + 1):
        print(i)