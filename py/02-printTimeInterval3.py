n1 = int(input("Inserire il primo orario (es. 0930):"))
n2 = int(input("Inserire il secondo orario:"))

if(n1 > n2):
    n3 = 2360
    tempo = n3 - n1 + n2

else:
    tempo = n2 - n1

ore = tempo // 100
minuti = tempo % 100

if(ore == 1 and minuti == 1):
    print("Tempo trascorso: un'ora e un minuto")
elif(ore == 1 and minuti != 0):
    print("Tempo trascorso: un'ora e", minuti ,"minuti")
elif(minuti == 1 and ore != 0):
    print("Tempo trascorso:", ore ,"ore e un minuto")
elif(ore == 1 and minuti == 0):
    print("Tempo trascorso: un'ora")
elif(minuti == 1 and ore == 0):
    print("Tempo trascorso: un minuto")
elif(ore != 0 and minuti == 0):
    print("Tempo trascorso:", ore ,"ore")
elif(minuti != 0 and ore == 0):
    print("Tempo trascorso:", minuti ,"minuti")
else:
    print("Tempo trascorso:", ore ,"ore e", minuti ,"minuti")
