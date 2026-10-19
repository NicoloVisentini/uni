valori = []
riga = input("Valore, oppure STOP: ")
while riga != "STOP":
    valori.append(int(riga))
    riga = input("Valore, oppure STOP: ")

quantita = len(valori)
n = 0
while n * n < quantita:
    n = n + 1

valido = n * n == quantita and quantita > 0

numero = 1
while numero <= quantita and valido:
    if not numero in valori:
        valido = False
    numero = numero + 1

matrice = []
if valido:
    riga_indice = 0
    while riga_indice < n:
        inizio = riga_indice * n
        matrice.append(valori[inizio:inizio + n])
        riga_indice = riga_indice + 1

    for riga_matrice in matrice:
        testo = ""
        for valore in riga_matrice:
            testo = testo + str(valore) + " "
        print(testo)

    costante = 0
    for valore in matrice[0]:
        costante = costante + valore

    i = 0
    while i < n and valido:
        somma_riga = 0
        somma_colonna = 0
        j = 0
        while j < n:
            somma_riga = somma_riga + matrice[i][j]
            somma_colonna = somma_colonna + matrice[j][i]
            j = j + 1
        if somma_riga != costante or somma_colonna != costante:
            valido = False
        i = i + 1

    diagonale1 = 0
    diagonale2 = 0
    i = 0
    while i < n:
        diagonale1 = diagonale1 + matrice[i][i]
        diagonale2 = diagonale2 + matrice[i][n - 1 - i]
        i = i + 1
    if diagonale1 != costante or diagonale2 != costante:
        valido = False

if valido:
    print("Quadrato magico perfetto")
else:
    print("Non è un quadrato magico perfetto")