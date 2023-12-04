num1 = input("Entrez votre premier chiffre: ")
num2 = input("Entrez votre deuxième chiffre: ")
operator = input("Quel calucul voulez-vous effectuer ?: ")
next = input("Voulez-vous continuer ? (Y/N): ")
historique = input("Souhaitez-vous afficher l'historique ? (Y/N): ")
history = []
#Demande à l'utilisateur ce qu'il veut

def calculatrice(num1, operator, num2):
    global next, historique, history
    while True:
        
        if operator == '+':
            print(float(num1) + float(num2))
            history.append(float(num1) + float(num2))
        elif operator == '-':
            print(float(num1) - float(num2))
            history.append(float(num1) - float(num2)) 
        elif operator == '*':
            print(float(num1) * float(num2))
            history.append(float(num1) * float(num2))
        elif operator == '/':
            if float(num1) != 0:
                print(float(num1) / float(num2))
                history.append(float(num1) / float(num2))
            else:
                print("Division par zéro impossible.")
                history.append("Erreur")
        elif operator == '%':
            if float(num2) != 0:
                print((num1/num2)*(100/num2))
                history.append((num1/num2)*(100/num2))
            else:
                print("Modulo par zéro impossible.")
                history.append("Erreur")
        else:
            print("Opérateur non valide.")
        if historique.upper() == 'Y':
            print(historique)
        if next.upper() == 'N':
            break
        num1 = input("Entrez votre premier chiffre: ")
        num2 = input("Entrez votre deuxième chiffre: ")
        operator = input("Quel calucul voulez-vous effectuer ?: ")
        next = input("Voulez-vous continuer ? (Y/N): ")
        historique = input("Souhaitez-vous afficher l'historique ? (Y/N): ")

print (calculatrice(num1, operator, num2))
print (next)
#Int et Float permet de changer des string en valeur -> Int base 10 (pas de nombres à virgules) Float = nombres à virgules.