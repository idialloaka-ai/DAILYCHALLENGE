


# Challenge

"""Instructions : La ferme du vieux MacDonald

On vous fournit un exemple de code et son résultat. Votre tâche consiste à créer une Farmclasse qui produit le même résultat.



Étape 1 : Créer la classe Ferme

Créez une classe appelée Farm.
Cette classe représentera une ferme et ses animaux.


Étape 2 : Implémenter la __init__méthode

La Farmclasse devrait avoir une __init__méthode.
Il devrait prendre un paramètre : farm_name.
À l'intérieur __init__, créez deux attributs : un namepour stocker le nom de la ferme et un autre animalspour stocker les animaux (initialisez-les comme un dictionnaire vide).


Étape 3 : Mettre en œuvre la add_animalméthode

Créez une méthode appelée add_animal.
Elle doit prendre deux paramètres : ` count` animal_typeet count`number` (avec une valeur par défaut de 1). `count` correspond à la quantité d'animaux qui seront ajoutés au dictionnaire.
Le dictionnaire se présentera comme suit :
{'cow': 1, 'pig':3, 'horse': 2}
Si l'élément animal_typeexiste déjà dans le animalsdictionnaire, incrémentez son compteur de count.
Si l'élément n'existe pas, ajoutez-le au dictionnaire comme clé et avec la countvaleur donnée.


Étape 4 : Mettre en œuvre la get_infométhode

Créez une méthode appelée get_info.
Elle doit renvoyer une chaîne de caractères affichant le nom de la ferme, les animaux et leur nombre, ainsi que la phrase « EIEI-0 ! ».
Mettez en forme le résultat pour qu'il corresponde à l'exemple fourni.
Utilisez la mise en forme de chaînes de caractères pour aligner les noms et le nombre d'animaux en colonnes.


Étape 5 : Testez votre code

Créez un Farmobjet et appelez les méthodes add_animalet .get_info
Vérifiez que le résultat correspond à l'exemple fourni.


Exemple:

class Farm:
    def __init__(self, farm_name):
        # ... code to initialize name and animals attributes ...

    def add_animal(self, animal_type, count):
        # ... code to add or update animal count in animals dictionary ...

    def get_info(self):
        # ... code to format animal info from animals dictionary ...


# Test the code 
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
#output:
# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


Bonus : Agrandissez la ferme



Étape 6 : Mettre en œuvre la get_animal_typesméthode

Ajoutez une méthode appelée get_animal_typesà la Farmclasse.
Cette méthode doit renvoyer une liste triée de tous les types d'animaux (clés issues du animalsdictionnaire).
Utilisez la sorted()fonction pour trier la liste.


Étape 7 : Mettre en œuvre la get_short_infométhode

Ajoutez une méthode appelée get_short_infoà la Farmclasse.
Cette méthode devrait renvoyer une chaîne de caractères comme « La ferme de McDonald possède des vaches, des chèvres et des moutons. »
Appelez la get_animal_typesméthode pour obtenir la liste des animaux.
Construisez la chaîne de caractères en ajoutant un « s » au nom de l'animal si son nombre d'occurrences est supérieur à 1.
Utilisez la mise en forme de chaînes de caractères pour créer le résultat.


Étape 8 : mettre à jour la méthode add_animal

À utiliser **kwargspour le transfert de plusieurs animaux. Les clés seront le nom de l'animal et les valeurs, la quantité.
Vous pouvez alors appeler la méthode de cette manière :macdonald.add_animal('cow'= 5, 'sheep' = 2, 'goat' = 12)

"""

class Farm:
    def __init__(self, farm_name):
        self.name    = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):
        
        if kwargs:
            for animal, qty in kwargs.items():
                if animal in self.animals:
                    self.animals[animal] += qty
                else:
                    self.animals[animal] = qty
        elif animal_type:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

    def get_info(self):
        result = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            result += f"{animal:10}: {count}\n"
        result += "\n    E-I-E-I-0!"
        return result

    
    def get_animal_types(self):
        return sorted(self.animals.keys())

    
    def get_short_info(self):
        types = self.get_animal_types()
        animal_list = []
        for animal in types:
            if self.animals[animal] > 1:
                animal_list.append(animal + "s")
            else:
                animal_list.append(animal)
        if len(animal_list) > 1:
            animals_str = ", ".join(animal_list[:-1]) + " and " + animal_list[-1]
        else:
            animals_str = animal_list[0]
        return f"{self.name}'s farm has {animals_str}."



macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())


print(macdonald.get_animal_types())
print(macdonald.get_short_info())


macdonald.add_animal(cow=3, horse=2)
print(macdonald.get_info())

