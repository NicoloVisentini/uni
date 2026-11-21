def palindroma(stringa):

    if len(stringa) <= 1:
        verifica = True
    elif stringa[0] != stringa[len(stringa) - 1]:
        verifica = False
    else:
        verifica = palindroma(stringa[1:len(stringa) - 1])

    return verifica


# main
stringa = input("Parola palindroma: ")

palindroma = palindroma(stringa)

if palindroma:
    print("La parola inserita e' palindroma.")
else:
    print("La parola inserita NON e' palindroma.")