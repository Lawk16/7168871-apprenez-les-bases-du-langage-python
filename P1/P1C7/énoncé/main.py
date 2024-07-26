# Écrivez votre code ici !
# Création du dictionnaire fruits
fruits = {
  "pomme" : "rouge" ,
  "banane" : "jaune" ,
  "orange" : "orange"
}

# Ajout de la clé "kiwi" avec la valeur "vert"
fruits["kiwi"] = "vert"

# Stockage de la valeur correspondant à la clé banane dans une variable appellée banane_couleur
banane_couleur = fruits["banane"]
print("La banne est",banane_couleur,)

# Modification de la valeur associée à "pomme" pour "vert"
fruits ["pomme"] = "vert"

# Suppression de la clé "banane" du dictionaire et affichage
fruits.pop("banane")
print(fruits)

# Affichage des clés restants
print(fruits.keys()) 
