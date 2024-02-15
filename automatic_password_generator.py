"""Automatic password generator"""

import random
from password_checker import is_valid_password

required_number_of_characters=12
required_number_of_uppercase_characters=1
required_number_of_lowercase_characters=1
required_number_of_special_characters=1
required_number_of_digits=1
uppercase_characters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_characters = "abcdefghijklmnopqrstuvwxyz"
digits="1234567890"
special_characters="!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def generate_random_password():
    """Returns a random password with the specific characteristics."""
    password_characters = []
    random_password = ""
    for i in range(required_number_of_uppercase_characters):
        password_characters.append(random.choice(uppercase_characters))
    for i in range(required_number_of_lowercase_characters):
        password_characters.append(random.choice(lowercase_characters))
    for i in range(required_number_of_digits):
        password_characters.append(random.choice(digits))
    for i in range(required_number_of_special_characters):
        password_characters.append(random.choice(special_characters))
    while len(password_characters) < required_number_of_characters:
        password_characters.append(
            random.choice(uppercase_characters + lowercase_characters + digits + special_characters))
    random.shuffle(password_characters)
    for character in password_characters:
        random_password += character
    return random_password


# test_password_generator()

