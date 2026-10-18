aggettivo = input("Inserisci un aggettivo qualificativo maschile o femminile: ")

lunghezza = len(aggettivo)

print("Aggettivo inserito:", aggettivo.capitalize())

if(aggettivo[lunghezza - 1] == "o"):
    forma_diminutiva = aggettivo[0 : lunghezza - 1] + "ino"
    print("Forma diminutiva:", forma_diminutiva.capitalize())

    superlativo_assoluto = aggettivo[0 : lunghezza - 1] + "issimo"
    print("Superlativo assoluto", superlativo_assoluto.capitalize())

elif(aggettivo[lunghezza - 1] == "a"):
    forma_diminutiva = aggettivo[0 : lunghezza - 1] + "ina"
    print("Forma diminutiva:", forma_diminutiva.capitalize())
    
    superlativo_assoluto = aggettivo[0 : lunghezza - 1] + "issima"
    print("Superlativo assoluto", superlativo_assoluto.capitalize())

else:
    print("aggettivo non a e non o, errore")