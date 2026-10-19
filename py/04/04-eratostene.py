numero = int(input("Inserisci un numero intero positivo: "))

while numero <= 0:
    print("Errore, riprova: ")
    numero = int(input("Inserisci un numero intero positivo: "))

numeri = []

for i in range(0, numero):
    numeri.append(True)

if numero > 0:
    numeri[0] = False
if numero > 1:
    numeri[1] = False

n = 2
while n < numero:
    multiplo = n * 2
    while multiplo < numero:
        numeri[multiplo] = False
        multiplo = multiplo + n
    n = n + 1

for i in range(numero):
    if numeri[i]:
        print(i)