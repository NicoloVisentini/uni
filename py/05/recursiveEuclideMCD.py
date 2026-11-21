def mcd(m, n):
    if m % n == 0:
        risultato = n
    else:
        risultato = mcd(n, m % n)

    return risultato


# main
m = int(input("Numero intero positivo: "))
n = int(input("Numero intero positivo: "))

while m <= 0:
    print("Numero non valido, riprova: ")
    m = int(input())

while n <= 0:
    print("Numero non valido, riprova: ")
    n = int(input())

if n > m:
    temp = m
    m = n
    n = temp

print("L' mcd e': ", mcd(m, n))