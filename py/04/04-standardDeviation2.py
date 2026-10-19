numeri = []

riga = input("Numero, oppure riga vuota per terminare: ")

while riga != "":
    numeri.append(int(riga))
    riga = input("Numero, oppure riga vuota per terminare: ")

n = len(numeri)

if n == 1:
    print("La deviazione di un solo numero vale 0")
elif n < 1:
    print("Non si può calcolare la deviazione senza numeri")
else:
    B = 0
    A = 0

    for numero in numeri:
        B = B + numero
        A = A + numero**2

    D = ((A-B*B/n)/(n-1))**(1/2)

    print("La deviazione è", D)