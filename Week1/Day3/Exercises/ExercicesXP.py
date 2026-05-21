
# Exercice 1 : Les chats

"""Principaux sujets en Python :

Classes et objets
instanciation d'objet
Attributs
Fonctions


Instructions:

Utilisez la Catclasse fournie pour créer trois objets chat. Ensuite, créez une fonction pour trouver le chat le plus âgé et afficher ses détails.



Étape 1 : Créer des objets Chat

Utilisez cette Catclasse pour créer trois objets chat avec des noms et des âges différents.


Étape 2 : Créer une fonction pour trouver le chat le plus âgé

Créez une fonction qui prend les trois objets chat en entrée.
Dans cette fonction, comparez l'âge des chats pour trouver le plus âgé.
Renvoie l'objet chat le plus ancien.


Étape 3 : Imprimer les informations du chat le plus âgé

Appelez la fonction pour obtenir le chat le plus âgé.
Afficher une chaîne formatée : « Le chat le plus âgé est <cat_name>, et a <cat_age>ans. »
Remplacez <cat_name>et <cat_age>par le nom et l'âge du chat le plus âgé.


Exemple:

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
# cat1 = create the object

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    # ... code to find and return the oldest cat ...

# Step 3: Print the oldest cat's details

"""

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age  = cat_age

cat1 = Cat("Felix", 3)
cat2 = Cat("Luna",  7)
cat3 = Cat("Milo",  5)

def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest

oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"Le chat le plus âgé est {oldest.name}, et a {oldest.age} ans.")

# Exercice 2 : Chiens

"""Objectif : Créer une Dogclasse, instancier des objets, appeler des méthodes et comparer la taille des chiens.



Principaux sujets en Python :

Classes et objets
instanciation d'objet
Méthodes
Attributs
Instructions conditionnelles ( if)


Instructions:

Créez une Dogclasse avec des méthodes pour aboyer et sauter. Instanciez des objets chien, appelez leurs méthodes et comparez leurs tailles.



Étape 1 : Créer la classe Chien

Créez une classe appelée Dog.
Dans cette __init__méthode, prenez nameet heightcomme paramètres et créez les attributs correspondants.
Créez une bark()méthode qui affiche « <dog_name>fait ouaf ! ».
Créez une jump()méthode qui imprime « <dog_name>saute <x>cm de haut ! », où xest height * 2.


Étape 2 : Créer des objets Chien

Créez davids_dogdes sarahs_dogobjets avec leurs noms et hauteurs respectifs.


Étape 3 : Imprimer les informations sur le chien et les méthodes d’appel

Inscrivez le nom et la taille de chaque chien.
Appelez les méthodes bark()et jump()pour chaque chien.


Étape 4 : Comparer la taille des chiens


"""

class Dog:
    def __init__(self, name, height):
        self.name   = name
        self.height = height

    def bark(self):
        print(f"{self.name} fait ouaf !")

    def jump(self):
        print(f"{self.name} saute {self.height * 2} cm de haut !")


davids_dog = Dog("Rex",   50)
sarahs_dog = Dog("Bella", 35)

for dog in [davids_dog, sarahs_dog]:
    print(f"{dog.name} — taille : {dog.height} cm")
    dog.bark()
    dog.jump()

# Comparaison
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} est plus grand que {sarahs_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
     print(f"{sarahs_dog.name} est plus grand que {davids_dog.name}.")
else:
    print("Les deux chiens font la même taille.")

# Exercice 3 : Qui est le producteur de la chanson ?

"""Objectif : Créer une Songclasse pour représenter les paroles de chansons et les imprimer.



Principaux sujets en Python :

Classes et objets
instanciation d'objet
Méthodes
Listes


Instructions:

Créez une Songclasse avec une méthode permettant d'imprimer les paroles d'une chanson ligne par ligne.



Étape 1 : Créer la classe de chansons

Créez une classe appelée Song.
Dans la __init__méthode, prenez lyrics(une liste) comme paramètre et créez un attribut correspondant.
Créez une sing_me_a_song()méthode qui affiche chaque élément de la lyricsliste sur une nouvelle ligne.


Exemple:

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

Résultat : Il y a une dame qui est persuadée que tout ce qui brille n'est pas or et elle achète un escalier vers le paradis


"""

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
])

stairway.sing_me_a_song()


# Exercice 4 : Apres-midi au zoo

"""But:

Créez une Zooclasse pour gérer les animaux. Cette classe doit permettre d'ajouter des animaux, de les afficher, de les vendre et de les organiser par ordre alphabétique.



Principaux sujets en Python :

Classes et objets
instanciation d'objet
Méthodes
Listes
Dictionnaires (pour le regroupement)
Manipulation de chaînes


Instructions
Étape 1 : Définir la Zooclasse
1. Créez une classe appelée Zoo.

2. Mettre en œuvre la __init__()méthode :

Elle prend en paramètre une chaîne de caractères zoo_namereprésentant le nom du zoo.
Initialisez une liste vide animalspour garder une trace des noms d'animaux.
3. Ajouter une méthode add_animal(new_animal):

Cette méthode ajoute un nouvel animal à la animalsliste.
N’ajoutez pas l’animal s’il figure déjà dans la liste.
4. Ajouter une méthode get_animals():

Cette méthode affiche tous les animaux actuellement présents dans le zoo.
5. Ajouter une méthode sell_animal(animal_sold):

Cette méthode vérifie si un animal spécifié figure dans la liste des animaux et, le cas échéant, le supprime de celle-ci.
6. Ajouter une méthode sort_animals():

Cette méthode classe les animaux par ordre alphabétique.
Il les regroupe également par la première lettre de leur nom.
Le résultat devrait être un dictionnaire contenant :
Chaque touche correspond à une lettre.
Chaque valeur est une liste d'animaux dont le nom commence par cette lettre.
Exemple de résultat :

{
   'B': ['Baboon', 'Bear'],
   'C': ['Cat', 'Cougar'],
   'G': ['Giraffe'],
   'L': ['Lion'],
   'Z': ['Zebra']
}
7. Ajouter une méthode get_groups():

Cette méthode imprime les animaux groupés tels que créés par sort_animals().
Exemple de résultat :

B: ['Baboon', 'Bear']
C: ['Cat', 'Cougar']
G: ['Giraffe']
...


Étape 2 : Créer un objet Zoo
Créez une instance de la Zooclasse et indiquez un nom pour le zoo.


Étape 3 : Appeler les méthodes du zoo
Utilisez les méthodes de votre Zooobjet pour tester l'ajout, la vente, l'affichage, le tri et le regroupement d'animaux.


Exemple (aucune logique interne fournie)
class Zoo:
    def __init__(self, zoo_name):
        pass

    def add_animal(self, new_animal):
        pass

    def get_animals(self):
        pass

    def sell_animal(self, animal_sold):
        pass

    def sort_animals(self):
        pass

    def get_groups(self):
        pass

# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()


Bonus : Modifiez la add_animal()méthode pour éviter *argsde la répéter à chaque fois pour un nouvel animal ; vous pouvez désormais passer plusieurs noms d’animaux séparés par une virgule.


"""

class Zoo:
    def __init__(self, zoo_name):
        self.name    = zoo_name
        self.animals = []

    def add_animal(self, *new_animals):   # bonus : *args
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()
        groups = {}
        for animal in self.animals:
            letter = animal[0].upper()
            if letter not in groups:
                groups[letter] = []
            groups[letter].append(animal)
        return groups

    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


brooklyn_safari = Zoo("Brooklyn Safari")

# Bonus : plusieurs animaux d'un coup
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon",
                           "Lion", "Zebra", "Cat", "Cougar")
brooklyn_safari.get_animals()

brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

brooklyn_safari.get_groups()

