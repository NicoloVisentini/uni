def rule1(password):
    if len(password) < 8:
        return False
    else:
        return True

def rule2(password):
    alfabeto_inglese_Maiuscolo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    trovata = False

    for carattere in password:
        i = 0
        while i < 26 and not trovata:
            if carattere == alfabeto_inglese_Maiuscolo[i]:
                trovata = True
            else:
                i = i + 1

    return trovata

def rule3(password):
    alfabeto_inglese_minuscolo = "abcdefghijklmnopqrstuvwxyz"
    trovata = False
    
    for carattere in password:
        i = 0
        while i < 26 and not trovata:
            if carattere == alfabeto_inglese_minuscolo[i]:
                trovata = True
            else:
                i = i + 1
    
    return trovata

def rule4(password):
    cifre_numeriche = "0123456789"
    trovata = False
    
    for carattere in password:
        i = 0
        while i < 10 and not trovata:
            if carattere == cifre_numeriche[i]:
                trovata = True
            else:
                i = i + 1
    
    return trovata

def rule5(password):
    caratteri_cifre = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    trovata = False
    
    for carattere in password:
        if carattere not in caratteri_cifre:
            trovata = True
    
    return trovata

def rule6(password):
    verifica = True
    
    for carattere in password:
        if carattere == " ":
            verifica = False
    
    return verifica

def rule7(password):
    verifica = True
    
    for i in range(len(password)):
        for j in range(i + 1, len(password)):
            if password[i] == password[j]:
                verifica = False
    
    return verifica

def isValid(password):
    valida = True

    if not rule1(password):
        print("La password non contiene almeno 8 caratteri")
        valida = False
    if not rule2(password):
        print("La password non ha almeno una lettera maiuscola")
        valida = False
    if not rule3(password):
        print("La password non ha almeno una lettera minuscola")
        valida = False
    if not rule4(password):
        print("La password non ha almeno una cifra numerica")
        valida = False
    if not rule5(password):
        print("La password non ha almeno un carattere che non sia una lettera né una cifra")
        valida = False
    if not rule6(password):
        print("La password contiene almeno uno spazio")
        valida = False
    if not rule7(password):
        print("La password contiene almeno un carattere ripetuto")
        valida = False
    return valida

def main():
    valida = False

    while not valida:
        password = input("Inserire una nuova password: ")
        valida = isValid(password)

    print("La password è accettabile.")

main()