s1 = input("Prima stringa: ")
s2 = input("Seconda stringa: ")

trovata = False
i = 0
while i <= len(s1) - len(s2) and not trovata:
    if s1[i:i + len(s2)] == s2:
        trovata = True
    i = i + 1

if trovata:
    print("La seconda stringa è una sottostringa della prima")
else:
    print("La seconda stringa non è una sottostringa della prima")