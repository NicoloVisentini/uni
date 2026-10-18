numero = int(input("Inserisci un numero (compreso fra 0 e 255): "))

while(numero < 0 or numero > 255):
    print("Numero non valido. Riprova: ")
    numero = int(input())

b7 = numero // 128
numero = numero % 128
b6 = numero // 64
numero = numero % 64
b5 = numero // 32
numero = numero % 32
b4 = numero // 16
numero = numero % 16
b3 = numero // 8
numero = numero % 8
b2 = numero // 4
numero = numero % 4
b1 = numero // 2
b0 = numero % 2
print(str(b7) + str(b6) + str(b5) + str(b4) + str(b3) + str(b2) + str(b1) + str(b0))