
# Challenge 1

number = int(input("Enter a number: "))
length = int(input("Enter the length: "))
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)
print(multiples)

# Challenge 2

user_word = input("Enter a string: ")
cleaned_word = ""
for letter in user_word:
    if len(cleaned_word) == 0 or letter != cleaned_word[-1]:
        cleaned_word += letter
print(cleaned_word)