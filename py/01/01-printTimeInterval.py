n1 = int(input("Inserire il primo orario (es. 0930):"))
n2 = int(input("Inserire il secondo orario (successivo al primo):"))

tempo = n2 - n1

ore = tempo // 100
minuti = tempo % 100

print("Tempo trascorso:", ore ,"ore e", minuti ,"minuti")