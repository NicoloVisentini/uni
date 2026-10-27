stringa = input("Inserisci una stringa: ")

stringa_inversa = ""

i = len(stringa) - 1

while i >= 0:
    stringa_inversa = stringa_inversa + stringa[i]
    i = i - 1

print(stringa_inversa)

if stringa != stringa_inversa:
    print("La stringa inserita NON e palindroma.")
else:
    print("La stringa inserita e palindroma.")
    print("Stringa iniziale:", stringa, "Stringa invertita:", stringa_inversa)
