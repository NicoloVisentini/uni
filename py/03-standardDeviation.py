A = 0
B = 0
n = 0

riga = input("Inserisci numero o 'STOP' per fermare: ")

while(riga != 'STOP'):

    numero = int(riga)
    B = B + numero
    A = A + numero**2
    n = n + 1

    riga = input("Inserisci numero o 'STOP' per fermare: ")

if(n <= 1):
    print("Errore")
else:
    D = ((A-B*B/n)/(n-1))**(1/2)
    print("La deviazione standard è", D)