


# Exercice 2: Dogs

"""Goal: Create a Dog class with methods for barking, running speed, and fighting.



Key Python Topics:

Classes and objects
Methods
Attributes


Instructions:

Step 1: Create the Dog Class

Create a class called Dog with name, age, and weight attributes.
Implement a bark() method that returns “<dog_name> is barking”.
Implement a run_speed() method that returns weight / age * 10.
Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.


Step 2: Create Dog Instances

Create three instances of the Dog class with different names, ages, and weights.


Step 3: Test Dog Methods

Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.


Example (Conceptual, No Direct Solution):

class Dog:
    def __init__(self, name, age, weight):
        # ... code to initialize attributes ...

    def bark(self):
        # ... code to return bark message ...

    def run_speed(self):
        # ... code to return run speed ...

    def fight(self, other_dog):
        # ... code to determine and return winner ...

# Step 2: Create dog instances
#... your code here

# Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

"""

class Dog:
    def __init__(self, name, age, weight):
        self.name   = name
        self.age    = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power    = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f"{self.name} a gagné le combat !"
        elif other_power > my_power:
            return f"{other_dog.name} a gagné le combat !"
        else:
            return "Match nul !"


dog1 = Dog("Rex",   3, 30)
dog2 = Dog("Bella", 5, 20)
dog3 = Dog("Max",   2, 25)

print(dog1.bark())
print(f"Vitesse de {dog2.name} : {dog2.run_speed():.2f}")
print(dog1.fight(dog2))
print(dog2.fight(dog3))