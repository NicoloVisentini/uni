Mercurio = 0.38
Venere = 0.91
Terra = 1.00
Marte = 0.38
Giove = 2.34
Saturno = 1.06
Urano = 0.92
Nettuno = 1.19

peso_equivalente = 0.0

peso = float(input("Inserisci il peso in kg sulla terra: "))

condizione = True

while(condizione):
    pianeta = input("Inserisci il nome del pianeta per conoscerne il peso equivalente: ")

    if(pianeta == 'Mercurio'):
        peso_equivalente = peso * Mercurio
        condizione = False
    elif(pianeta == 'Venere'):
        peso_equivalente = peso * Venere
        condizione = False
    elif(pianeta == 'Terra'):
        peso_equivalente = peso * Terra
        condizione = False
    elif(pianeta == 'Marte'):
        peso_equivalente = peso * Marte
        condizione = False
    elif(pianeta == 'Giove'):
        peso_equivalente = peso * Giove
        condizione = False
    elif(pianeta == 'Saturno'):
        peso_equivalente = peso * Saturno
        condizione = False
    elif(pianeta == 'Urano'):
        peso_equivalente = peso * Urano
        condizione = False
    elif(pianeta == 'Nettuno'):
        peso_equivalente = peso * Nettuno
        condizione = False
    else:
        print("Nome pianeta non valido.")

print("Sulla terra il tuo peso è", peso, "Kg, mentre su", pianeta, "il tuo peso è", peso_equivalente)