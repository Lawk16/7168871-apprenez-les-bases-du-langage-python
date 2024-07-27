def main():
# Ecrivez votre code ici !
# Attention tout votre code doit être indenté comme ce commentaire
    
# Création de deux variables 

nombre_a_gauche = input("Entrez le nombre à gauche : ")
nombre_a_droite = input("Entrez le nombre à droite : ")

# Création de la variable operation 
operation = input("Entrez le symbole de l'opération (+,-,*,/) que vous voulez : ")

# Création de la variable resultat
resultat = 0

# Vérification des deux nombres entiers
print("Le nombre à gauche est un entier (True or False) : ",nombre_a_gauche.isnumeric())
print("Le nombre à droite est un entier (True or False) : ",nombre_a_droite.isnumeric())
if nombre_a_gauche.isnumeric()==False or nombre_a_droite.isnumeric()==False :
    print("Erreur: les deux nombres doivent être des nombres entiers")
    exit()
    
else :
    nombre_a_gauche = int(nombre_a_gauche)
    nombre_a_droite = int(nombre_a_droite)
    

# Vérification du symbole, calcul et affichage du résultat
match operation :
    case "+" :
        resultat = (nombre_a_gauche + nombre_a_droite)
        print("Le résultat de l'addition de ces deux nombres est : r = ",resultat)
    case "-" :
        resultat = (nombre_a_gauche - nombre_a_droite)
        print("Le résultat de la soustraction de ces deux nombres est : r = ",resultat)
    case "*" :
        resultat = (nombre_a_gauche * nombre_a_droite)
        print("Le résultat du produit de ces deux nombres est : r = ",resultat)
    case "/" :
        if  nombre_a_droite==0 :
            print("Erreur: impossible de diviser par zéro.")
        else :
            resultat = (nombre_a_gauche / nombre_a_droite)
            print("Le résultat du quotient de ces deux nombres est : r = ",resultat)
    case _ :
        print("Erreur: le symbole d'opération doit être '+', '-', '*', ou '/'.")
        exit()

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
