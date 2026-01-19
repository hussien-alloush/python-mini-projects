import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    has_number = False
    has_special = False

    while len(pwd) < min_length or (numbers and not has_number) or (special_characters and not has_special):
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

    return pwd

pwd = generate_password(10)
print(pwd)
