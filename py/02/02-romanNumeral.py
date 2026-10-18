numero = int(input("Inserisci un numero intero positivo minore di 4000: "))

while(numero < 1 or numero >= 4000):
    print("Numero inserito non valido, riprova.")
    numero = int(input())

print("Numero decimale: ", numero)

contatore_M = 0
contatore_D = 0
contatore_C = 0
contatore_L = 0
contatore_X = 0
contatore_IX = 0
contatore_V = 0
contatore_IV = 0
contatore_I = 0

while(numero >= 1000):
    numero = numero - 1000
    contatore_M = contatore_M + 1

while(numero >= 500):
    numero = numero - 500
    contatore_D = contatore_D + 1

while(numero >= 100):
    numero = numero - 100
    contatore_C = contatore_C + 1

while(numero >= 50):
    numero = numero - 50
    contatore_L = contatore_L + 1

while(numero >= 10):
    numero = numero - 10
    contatore_X = contatore_X + 1

while(numero == 9):
    numero = numero - 9
    contatore_IX = contatore_IX + 1

while(numero >= 5):
    numero = numero - 5
    contatore_V = contatore_V + 1

while(numero == 4):
    numero = numero - 4
    contatore_IV = contatore_IV + 1

while(numero > 0):
    numero = numero - 1
    contatore_I = contatore_I + 1

M = "M" * contatore_M
D = "D" * contatore_D
C = "C" * contatore_C
L = "L" * contatore_L
X = "X" * contatore_X
IX = "IX" * contatore_IX
V = "V" * contatore_V
IV = "IV" * contatore_IV
I = "I" * contatore_I

numero_romano = M + D + C + L + X + IX + V + IV + I

print("Numero romano: ", numero_romano)