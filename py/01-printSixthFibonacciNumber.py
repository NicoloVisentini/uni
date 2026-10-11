
n = int(input("inserisci un numero maggiore di 2 intero positivo:"))

while(n < 2):
    print("Numero inserito errato.")
    n = int(input("Riprova:"))

fibonacci = (n-1) + (n-2)

print(n)
print("Risultato fibonacci: ", fibonacci)