

# Exercise 1 : convertir des listes en dictionnaires

"""Principaux sujets en Python :

Création de dictionnaires
Fonction Zip ou compréhension de dictionnaire


Instructions

On vous donne deux listes. Convertissez-les en un dictionnaire où la première liste contient les clés et la seconde liste contient les valeurs correspondantes.

"""

keys   = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))
result = {k: v for k, v in zip(keys, values)}
print(result)

# Exercise 2 :  Cinemax n° 2

"""Principaux sujets en Python :

Parcourir les dictionnaires
Les conditionnelles
Calculs


Instructions

Écrivez un programme qui calcule le coût total des billets de cinéma pour une famille en fonction de l'âge de ses membres.

L'âge des membres de la famille est stocké dans un dictionnaire.
Les règles de tarification des billets sont les suivantes :
Moins de 3 ans : gratuit
De 3 à 12 ans : 10 $
Plus de 12 ans : 15 $


Données familiales :

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


Parcourez le familydictionnaire pour calculer le coût total.
Imprimez le prix du billet pour chaque membre de la famille.
Imprimez le coût total à la fin.


Prime:

Permettez à l'utilisateur de saisir les noms et âges des membres de sa famille, puis calculez le coût total du billet.

"""
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    total += price
    print(f"{name.capitalize()} ({age} ans) : ${price}")

print(f"\nCoût total : ${total}")

# Exercise 3 : Zara

"""Principaux sujets en Python :

Création de dictionnaires
Accéder aux éléments du dictionnaire et les modifier
Les méthodes de dictionnaire comme .pop()et.update()


Instructions

Créer et manipuler un dictionnaire contenant des informations sur la marque Zara.



Informations sur la marque :

name: Zara
creation_date: 1975
creator_name: Amancio Ortega Gaona
type_of_clothes: men, women, children, home
international_competitors: Gap, H&M, Benetton
number_stores: 7000
major_color: 
    France: blue, 
    Spain: red, 
    US: pink, green


Créez un dictionnaire contenant brandles données fournies.
Modifiez et accédez au dictionnaire comme suit :
Modifiez la valeur de number_storesà 2.
Imprimez une phrase décrivant les clients de Zara en utilisant la type_of_clotheslégende.
Ajoutez une nouvelle clé country_creationavec la valeur Spain.
Vérifiez si international_competitorscela existe et, si oui, ajoutez « Desigual » à la liste.
Supprimez la creation_dateclé.
Imprimez le dernier élément dans international_competitors.
Imprimer les principales couleurs aux États-Unis.
Affichez le nombre de clés dans le dictionnaire.
Imprimez toutes les clés du dictionnaire.


Prime:

Créez un autre dictionnaire appelé more_on_zaraavec creation_dateet number_stores. Fusionnez ce dictionnaire avec le dictionnaire original brandet affichez le résultat.

"""

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2

clients = ", ".join(brand["type_of_clothes"])
print(f"Zara crée des vêtements pour : {clients}.")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

brand.pop("creation_date")

print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])

print(f"Nombre de clés : {len(brand)}")

print(list(brand.keys()))

more_on_zara = {"creation_date": 1975, "number_stores": 2}
brand.update(more_on_zara)
print(brand)

# Exercise 4 : Un peu de geographie 

"""Objectif : Créer une fonction qui décrit une ville et son pays.

Principaux sujets en Python :

Fonctions à plusieurs paramètres
valeurs des paramètres par défaut
formatage de chaînes


Étape 1 : Définir une fonction avec des paramètres

Définissez une fonction nommée describe_city().
Cette fonction doit accepter deux paramètres : cityet country.
Attribuez au countryparamètre une valeur par défaut, telle que « Inconnu ».


Étape 2 : Imprimer un message

À l'intérieur de la fonction, configurez le code pour afficher une phrase comme «est dans".
Remplacez <city>et <country>par les valeurs des paramètres.


Étape 3 : Appeler la fonction

Appelez la describe_city()fonction avec différentes combinaisons de ville et de pays.
Essayez de l'appeler avec et sans fournir l'argument pays pour voir la valeur par défaut en action.
Exemple : describe_city("Reykjavik", "Iceland")et describe_city("Paris").


Résultat attendu :

Reykjavik is in Iceland.
Paris is in Unknown.

"""
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")
describe_city("Abidjan", "Côte d'Ivoire")

# Exercise 5 : Aléatoire 

"""Objectif : Créer une fonction qui génère des nombres aléatoires et les compare.

Principaux sujets en Python :

randommodule
random.randint()fonction
Instructions conditionnelles ( if, else)


Étape 1 : Importer le randommodule

Au début de votre script, utilisez cette fonction import randompour accéder aux fonctions de génération de nombres aléatoires.


Étape 2 : Définir une fonction avec un paramètre

Créez une fonction qui accepte un nombre compris entre 1 et 100 comme paramètre.


Étape 3 : Générer un nombre aléatoire

À l'intérieur de la fonction, utilisez-la random.randint(1, 100)pour générer un entier aléatoire compris entre 1 et 100.


Étape 4 : Comparer les nombres

S'ils sont identiques, afficher un message de réussite. Sinon, afficher un message d'échec et les deux nombres.


Étape 5 : Appeler la fonction

Appelez la fonction avec un nombre compris entre 1 et 100.


Résultat attendu :

Success! (if the numbers match)
Fail! Your number: 50, Random number: 23 (if they don't match)

"""

import random

def guess(number):
    random_number = random.randint(1, 100)
    if number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {number}, Random number: {random_number}")
guess(50)

# Exercise 6 : Creons des T-shirts personnalises

"""Objectif : Créer une fonction permettant de décrire la taille et le message d'un t-shirt, avec des valeurs par défaut.

Principaux sujets en Python :

Fonctions avec paramètres et valeurs par défaut
Arguments clés


Étape 1 : Définir une fonction avec des paramètres

Définissez une fonction appelée make_shirt().
Cette fonction doit accepter deux paramètres : sizeet text.


Étape 2 : Imprimer un message récapitulatif

Configurez la fonction pour afficher une phrase résumant la taille et le message du t-shirt.


Étape 3 : Appeler la fonction



Étape 4 : Modifier la fonction avec les valeurs par défaut

Modifiez la make_shirt()fonction afin qu'elle sizeait une valeur par défaut de « large » et textqu'elle ait une valeur par défaut de « J'adore Python ».


Étape 5 : Appeler la fonction avec les valeurs par défaut et les valeurs personnalisées

Commandez make_shirt()un grand t-shirt avec le message par défaut.
Commandez make_shirt()un t-shirt de taille moyenne avec le message par défaut.
Appelez-nous make_shirt()pour commander un t-shirt de n'importe quelle taille avec un message différent.


Étape 6 (Bonus) : Arguments par mots-clés

Appelez make_shirt()en utilisant des arguments nommés (par exemple, make_shirt(size="small", text="Hello!")).


Résultat attendu :

The size of the shirt is large and the text is I love Python.
The size of the shirt is medium and the text is I love Python.
The size of the shirt is small and the text is Custom message.
"""
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()

make_shirt(size="medium")

make_shirt(size="small", text="Custom message")

make_shirt(text="Hello!", size="small")



# Exercise 7 : conseils sur la temperature

"""Objectif : Générer une température aléatoire et fournir des conseils en fonction de cette plage de températures.

Principaux sujets en Python :

Fonctions
Conditionnelles ( if/ elif)
nombres aléatoires
Nombres à virgule flottante (Bonus)
Gestion des saisons (Bonus)


Étape 1 : Créer la get_random_temp()fonction

Créez une fonction get_random_temp()qui renvoie un entier aléatoire compris entre -10 et 40 degrés Celsius.


Étape 2 : Créer la main()fonction

Créez une fonction appelée main(). À l'intérieur de cette fonction :
Appelez get_random_temp()pour obtenir une température aléatoire.
Stockez la température dans une variable et affichez un message convivial comme :
« La température actuelle est de 32 degrés Celsius. »


Étape 3 : Fournir des conseils basés sur la température

À l'intérieur main(), donnez des conseils en fonction de la température :
En dessous de 0°C : par exemple, « Brrr, il fait un froid de canard ! Mets des vêtements supplémentaires aujourd'hui. »
Entre 0°C et 16°C : par exemple, « Il fait assez froid ! N'oublie pas ton manteau. »
Entre 16°C et 23°C : par exemple, « Beau temps ».
Entre 24°C et 32°C : par exemple, « Il fait un peu chaud, pensez à bien vous hydrater. »
Entre 32°C et 40°C : par exemple, « Il fait vraiment chaud ! Reste au frais. »


Étape 4 : Températures à virgule flottante (Bonus)

Modifier get_random_temp()pour renvoyer un nombre à virgule flottante aléatoire afin random.uniform()d'obtenir des valeurs de température plus précises.


Étape 5 : Saisons mensuelles (Bonus)

Au lieu de générer directement une température aléatoire, demandez à l'utilisateur un mois (1-12) et déterminez la saison en utilisant if/ elifconditions.
Modifier get_random_temp()pour obtenir des températures spécifiques à chaque saison.


Résultat attendu :

The temperature right now is 32 degrees Celsius.
It's really hot! Stay cool.

"""
import random

def get_random_temp(season="summer"):
    ranges = {
        "winter": (-10, 5),
        "spring": (8,  20),
        "summer": (20, 40),
        "autumn": (5,  18)
    }
    low, high = ranges.get(season, (-10, 40))
    return round(random.uniform(low, high), 1)   

def main():
    month = int(input("Entrez un mois (1-12) : "))
    if   month in [12, 1, 2]:  season = "winter"
    elif month in [3, 4, 5]:  season = "spring"
    elif month in [6, 7, 8]:  season = "summer"
    else:                      season = "autumn"
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")

    if   temp < 0:              print("Brrr, il fait un froid de canard !")
    elif temp < 16:             print("Il fait assez froid ! N'oublie pas ton manteau.")
    elif temp < 24:             print("Beau temps !")
    elif temp <= 32:            print("Il fait un peu chaud, pensez à bien vous hydrater.")
    else:                       print("Il fait vraiment chaud ! Reste au frais.")

main()


# Exercise 8 : Garnitures de pizza

"""Principaux sujets en Python :

Boucles
Listes
formatage de chaînes


Instructions:

Écrivez une boucle qui demande à l'utilisateur de saisir les ingrédients de la pizza un par un.
Arrêtez la boucle lorsque l'utilisateur saisit 'quit'.
Pour chaque garniture saisie, imprimez :
"Adding [topping] to your pizza."
Après avoir quitté la boucle, affichez tous les ingrédients et le prix total de la pizza.
Le prix de base est de 10 $, et chaque garniture ajoute 2,50 $.

"""

BASE_PRICE    = 10
TOPPING_PRICE = 2.5
toppings = []

while True:
    topping = input("Ajouter une garniture (ou 'quit') : ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

print("\n--- Récapitulatif ---")
if toppings:
    print("Garnitures :")
    for t in toppings:
        print(f"  - {t}")
else:
    print("Pizza nature (sans garniture)")

total = BASE_PRICE + len(toppings) * TOPPING_PRICE
print(f"Prix total : ${total:.2f}")