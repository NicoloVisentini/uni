n = int(input("Inserisci un numero intero positivo maggiore di 1: "))

while(n <= 1):
    print("Errore, riprova:")
    n = int(input())

for i in range(2, n + 1):
    primo = True
    divisore = 2
    while divisore < i and primo:
        if i % divisore == 0:
            primo = False
        divisore = divisore + 1
    if primo:
        print(i)
