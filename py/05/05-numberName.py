def caso_minore_100(numero):

    unita = ["zero", "uno", "due", "tre", "quattro", "cinque", 
             "sei", "sette", "otto", "nove"]

    speciali = ["undici", "dodici", "tredici", "quattordici", "quindici", 
                "sedici", "diciassette", "diciotto", "diciannove"]

    decine = ["dieci", "venti", "trenta", "quaranta", "cinquanta", 
              "sessanta", "settanta", "ottanta", "novanta"]

    if numero < 10:
        nome = unita[numero]

    elif numero == 10:
        nome = decine[numero - 10]

    elif numero < 20:
        nome = speciali[numero - 11]

    elif numero < 100:
        d = numero // 10
        u = numero % 10

        if u == 0:
            nome = decine[d - 1]
        elif u == 1:
            caso_1 = decine[d - 1]
            nome = caso_1[0:len(caso_1) - 1] + unita[u]
        elif u == 3:
            caso_3 = "tré"
            nome = decine[d - 1] + caso_3
        else:
            nome = decine[d - 1] + unita[u]

    return nome


def centinaia(numero):
    maggiore = numero // 100
    minore = numero % 100
    if maggiore == 1:
        if minore == 0:
            nome = "cento"
        else:
            controllo = caso_minore_100(minore)
            if controllo[0:4] == "otta":
                cambio = (controllo[1:len(controllo)])
                nome = "cento" + cambio
            else:
                nome = "cento" + caso_minore_100(minore)
    else:
        if minore == 0:
            nome = caso_minore_100(maggiore) + "cento"
        else:
            controllo = caso_minore_100(minore)
            if controllo[0:4] == "otta":
                cambio = (controllo[1:len(controllo)])
                nome = caso_minore_100(maggiore) + "cento" + cambio
            else:
                nome = caso_minore_100(maggiore) + "cento" + caso_minore_100(minore)

    return nome


def migliaia(numero):
    maggiore = numero // 1000
    minore = numero % 1000
    if maggiore == 1:
        if minore == 0:
            nome = "mille"
        else:
            if minore < 100:
                nome = "mille" + caso_minore_100(minore)
            else:
                nome = "mille" + centinaia(minore)
    else:
        if minore == 0:
            if maggiore < 100:
                nome = caso_minore_100(maggiore) + "mila"
            else:
                nome = centinaia(maggiore) + "mila"
        else:
            if minore < 100:
                if maggiore < 100:
                    nome = caso_minore_100(maggiore) + "mila" + caso_minore_100(minore)
                else:
                    nome = centinaia(maggiore) + "mila" + caso_minore_100(minore)
            else:
                if maggiore < 100:
                    nome = caso_minore_100(maggiore) + "mila" + centinaia(minore)
                else:
                    nome = centinaia(maggiore) + "mila" + centinaia(minore)
    return nome


def identifica(numero):
    
    if numero < 100:
        nome = caso_minore_100(numero)
    elif numero < 1000:
        nome = centinaia(numero)
    else:
        nome = migliaia(numero)

    return nome


numero = int(input("Numero intero positivo minore di un milione: "))

while numero <= 0 or numero >= 1000000:
    print("Numero non valido, riprova: ")
    numero = int(input())

nome = identifica(numero)

print(nome)