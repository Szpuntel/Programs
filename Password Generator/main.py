import sys
import random
import string
password_lenght = 1
password = []
characters_left = -1

def update_characters_left(number_of_characters):
    global characters_left
    if number_of_characters <0 or number_of_characters > characters_left:
      print("Too many characters", characters_left)
      sys.exit(0)
    else:
      characters_left -= number_of_characters

while password_lenght < 5:
    password_lenght = int(input("How long passowrd do you need ? (min. 5 characters):"))
    if password_lenght < 5:
        print("Lenght is not enough")
else:
    characters_left = password_lenght
    print("Characters left:", characters_left)

lowercase_letters = int(input("How many small letters do you want? "))
update_characters_left(lowercase_letters)
print("Characters left:",characters_left)

uppercase_letters = int(input("How many big letters do you want ? "))
update_characters_left(uppercase_letters)
print("Characters left:",characters_left)

special_characters = int(input("How many special characters do you want ? "))
update_characters_left(special_characters)
print("Characters left:",characters_left)

digits = int(input("How many digits do you want ? "))
update_characters_left(digits)

if characters_left >0:
    print("You didnt put enough signs for your password. Rest will be replaced with small letters.")
    lowercase_letters += characters_left

print()
print("Passowrd Lenght:", password_lenght)
print("Small letters:", lowercase_letters)
print("Big letters:", uppercase_letters)
print("Special signs", special_characters)
print("Digits:", digits)

for i in range(password_lenght):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1
random.shuffle(password)
print("Generated Password:", "".join(password))
