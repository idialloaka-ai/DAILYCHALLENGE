# EXERCISE 1: Hello world

print("Hello world\n"*4, end="")

# EXERCISE 2: Some math

print((99**3)*8)

# EXERCISE 3: What is the output

5 < 3 # False
3 == 3 # True
3 == "3" # False
"3" > 3 # TypeError: '>' not supported between instances of 'str' and 'int'
"Hello" == "hello" # False

# EXERCISE 4: Your computer brand

computer_brand = "Lenovo"
print(f"I have a {computer_brand} computer.")

# EXERCISE 5: Your imformation

name = "Ibrahim"
age = 22
shoe_size = 45
info = f"my name is {name}, i am {age} years old, and i wear size {shoe_size} shoes."
print(info)

# EXERCISE 6: A & B

a = 9
b = 6
if a > b:
    print("Hello World")

# EXERCISE 7: Odd or even

nombre_text = input("Enter a number: ")
nombre = int(nombre_text)
if nombre % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# EXERCISE 8: What is your name?

mon_nom = "Ibrahim"
nom_utilisateur = input("What is your name? ")
if nom_utilisateur.lower() == mon_nom.lower():
    print(f"Wow, we have the same name, {mon_nom}! but i'm more handsome than you.")
else :
    print(f"Nice to meet you, {nom_utilisateur}!It doesn't hurt you not to have the same name as me?")

# EXERCISE 9: tell enough to ride a roller coaster

height = int(input("Enter your height in cm: "))
if height >= 145:
    print("You are tall enough to ride !")
else:
    print("You need to grow some more to ride !")