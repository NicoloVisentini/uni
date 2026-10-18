x1 = float(input("Inserisci coordinata x del centro della prima circonferenza: "))
y1 = float(input("Inserisci coordinata y del centro della prima circonferenza: "))
r1 = float(input("Inserisci raggio della prima circonferenza: "))

x2 = float(input("Inserisci coordinata x del centro della seconda circonferenza: "))
y2 = float(input("Inserisci coordinata y del centro della seconda circonferenza: "))
r2 = float(input("Inserisci raggio della seconda circonferenza: "))

d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

if d == 0 and r1 == r2:
    print("Le due circonferenze sono coincidenti")

elif d == r1 + r2:
    print("Le due circonferenze sono tangenti esternamente")

elif d == abs(r1 - r2) and d != 0:
    print("Le due circonferenze sono tangenti internamente")

elif d < r1 + r2 and d > abs(r1 - r2):
    print("Le due circonferenze sono secanti")

elif d == 0 and r1 != r2:
    print("Le due circonferenze sono concentriche (ma non coincidenti)")

elif d < abs(r1 - r2):
    print("Le due circonferenze sono una interna all'altra, ma non concentriche")

else:
    print("Le due circonferenze sono (reciprocamente) esterne")