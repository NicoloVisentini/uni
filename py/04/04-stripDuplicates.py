testo = input("Testo: ")
risultato = ""

if len(testo) > 0:
    risultato = testo[0]
    i = 1
    while i < len(testo):
        if testo[i] != testo[i - 1]:
            risultato = risultato + testo[i]
        i = i + 1

print(risultato)