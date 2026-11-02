def maiuscolo(testo):
    minuscole = "abcdefghijklmnopqrstuvwxyz"
    Maiuscole = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    risultato = ""

    for carattere in testo:
        posizione = 0
        trovata = False

        while posizione < 26 and not trovata:
            if carattere == minuscole[posizione]:
                trovata = True
            else:
                posizione = posizione + 1

        if trovata:
            risultato = risultato + Maiuscole[posizione]
        else:
            risultato = risultato + carattere

    return risultato


stringa = maiuscolo(input("Stringa: "))

chiave = 0
while chiave < 1 or chiave > 25:
    chiave = int(input("Chiave: "))

stringa_codificata = ""
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

i = 0
while i < len(stringa):
    posizione = 0
    trovata = False

    while posizione < 26 and not trovata:
        if stringa[i] == alfabeto[posizione]:
            trovata = True
        else:
            posizione = posizione + 1

    if trovata:
        stringa_codificata = stringa_codificata + alfabeto[(posizione + chiave) % 26]
    else:
        stringa_codificata = stringa_codificata + stringa[i]

    i = i + 1

print("Stringa iniziale:", stringa)
print("Chiave:", chiave)
print("Stringa codificata:", stringa_codificata)