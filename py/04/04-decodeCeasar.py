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


stringa = maiuscolo(input("Stringa codificata: "))

chiave = 0
while chiave < 1 or chiave > 25:
    chiave = int(input("Chiave: "))

stringa_decodificata = ""
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
        stringa_decodificata = stringa_decodificata + alfabeto[(posizione - chiave) % 26]
    else:
        stringa_decodificata = stringa_decodificata + stringa[i]

    i = i + 1

print("Stringa codificata:", stringa)
print("Chiave:", chiave)
print("Stringa decodificata:", stringa_decodificata)