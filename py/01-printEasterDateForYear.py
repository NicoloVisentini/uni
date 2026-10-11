y = int(input("Inserisci un numero intero non negativo (un anno):"))

while (y < 0):
    print("Numero inserito errato.")
    y = int(input("Riprova."))

a = y % 19

b = y // 100

c = y % 100

d = b // 4

e = b % 4

g = (8 * b + 13) // 25

h = (19 * a + b - d - g + 15)% 30

j = c // 4

k = c % 4

m = (a + 11 * h) // 319

r = (2 * e + 2 * j - k - h + m + 32) % 7

n = (h - m + r + 90) // 25

p = (h - m + r + n +19) % 32

print("Pasqua è il giorno ", p ," del mese ", n ," dell'anno ", y ,".", sep="")