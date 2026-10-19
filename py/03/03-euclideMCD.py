n = int(input("Inserisci n intero positivo: "))
m = int(input("Inserisci m intero positivo: "))

if(n <= 0 or m <= 0):
    print("Errore")
else:
    if(n > m):
        temp = n
        n = m
        m = temp

    resto = m % n

    while(resto != 0):
        m = n
        n = resto
        resto = m % n

    print("MCD è", n)

