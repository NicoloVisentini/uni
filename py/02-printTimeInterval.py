n1 = int(input("Inserire il primo orario (es. 0930):"))
n2 = int(input("Inserire il secondo orario:"))

if(n1 > n2):
    n3 = 2360
    tempo = n3 - n1 + n2

else:
    tempo = n2 - n1

ore = tempo // 100
minuti = tempo % 100

print("Tempo trascorso:", ore ,"ore e", minuti ,"minuti")