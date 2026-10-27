min = input("Stringa: ")
mid = input("Stringa: ")
max = input("Stringa: ")

if min > mid:
    temporanea = min
    min = mid
    mid = temporanea
if mid > max:
    temporanea = mid
    mid = max
    max = temporanea
if min > mid:
    temporanea = min
    min = mid
    mid = temporanea

print("Le stringhe in ordine crescente sono:")
print(min)
print(mid)
print(max)
