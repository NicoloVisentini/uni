a = int(input("Estremo inferiore positivo: "))
b = int(input("Estremo superiore: "))
seme = int(input("Seme intero: "))

if a <= 0 or a >= b:
    print("Input non valido")
else:
    seme = (seme * 1103515245 + 12345) % 2147483648
    segreto = a + seme % (b - a + 1)
    tentativi = 0
    indovinato = False

    while not indovinato:
        tentativo = int(input("Tentativo: "))
        tentativi = tentativi + 1
        if tentativo < segreto:
            print("Troppo piccolo!")
        elif tentativo > segreto:
            print("Troppo grande!")
        else:
            indovinato = True

    print("Complimenti! Tentativi:", tentativi)