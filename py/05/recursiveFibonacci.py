def fibonacci(n):
    if n == 1 or n == 2:
        risultato = 1
    else:
        risultato = fibonacci(n - 1) + fibonacci(n - 2)

    return risultato


# main
n = int(input("n positivo: "))
if n <= 0:
    print("Input non valido.")
else:
    print(fibonacci(n))