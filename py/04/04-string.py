dna = input("Inserisci una stringa:")

valida = True

for carattere in dna:
	if(carattere != "A" and carattere != "C" and carattere != "G" and carattere != "T"):
		valida = False

if not valida:
	print("Sequenza non valida.")
else:
	risultato = ""
	i = len(dna) - 1
	while i >= 0:
		if dna[i] == "A":
			risultato = risultato + "T"
		elif dna[i] == "T":
			risultato = risultato + "A"
		elif dna[i] == "C":
			risultato = risultato + "G"
		elif dna[i] == "G":
			risultato = risultato + "C"
		i = i - 1
	
	print("Dna corretto e invertito:", risultato)
