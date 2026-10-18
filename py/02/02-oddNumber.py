condizione = True
contatore = 0

while(condizione):
    numero = int(input("Scrivi un numero dispari: "))
    if(numero %2 == 0):
        if(contatore == 0):
            print("Ho detto dispari! Riprova")
            contatore = contatore + 1
        else:
            print("Ripassa il concetto di numero dispari, ti saluto.")
            break
    elif(numero %2 != 0):
        print("Complimenti! Il numero", numero, "è dispari!")
        condizione = False
    