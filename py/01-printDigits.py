numero = int(input("Inserisci un numero intero positivo con massimo 5 cifre:"))

while(numero < 1 or numero > 99999):
    print("Il numero inserito non rispetta le richieste.")
    numero = int(input("Riprova:"))

print("Il numero inserito e'", numero)

divisore = 10000

for i in range(5):
    cifra = numero // divisore
    print(cifra)
    numero = numero % divisore
    divisore = divisore // 10