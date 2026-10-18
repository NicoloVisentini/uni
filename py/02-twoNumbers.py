n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))

somma = n1 + n2

prodotto = n1 * n2

media = (n1 + n2) / 2

if(n1 > n2):
    massimo = n1
else:
    massimo = n2

if(n1 < n2):
    minimo = n1
else:
    minimo = n2

differenza = n1 - n2

if(differenza < 0):
    differenza_valore_assoluto = differenza * -1
else:
    differenza_valore_assoluto = differenza

print("Somma:", somma)
print("Prodotto:", prodotto)
print("Valore medio:", media)
print("Valore massimo:", massimo)
print("Valore minimo:", minimo)
print("Differenza (in valore assoluto)", differenza_valore_assoluto)