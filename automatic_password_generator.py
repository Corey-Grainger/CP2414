"""CP2414
Automatic password generator"""

import random
from password_checker import is_valid_password

REQUIRED_NUMBER_OF_CHARACTERS=12
REQUIRED_NUMBER_OF_UPPERCASE_CHARACTERS=1
REQUIRED_NUMBER_OF_LOWERCASE_CHARACTERS=1
REQUIRED_NUMBER_OF_SPECIAL_CHARACTERS=1
REQUIRED_NUMBER_OF_DIGITS=1
UPPERCASE_CHARACTERS= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
DIGITS= "1234567890"
SPECIAL_CHARACTERS= "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def generate_random_password():
    """Returns a random password with the specific characteristics."""
    password_characters = []
    random_password = ""
    for i in range(REQUIRED_NUMBER_OF_UPPERCASE_CHARACTERS):
        password_characters.append(random.choice(UPPERCASE_CHARACTERS))
    for i in range(REQUIRED_NUMBER_OF_LOWERCASE_CHARACTERS):
        password_characters.append(random.choice(LOWERCASE_CHARACTERS))
    for i in range(REQUIRED_NUMBER_OF_DIGITS):
        password_characters.append(random.choice(DIGITS))
    for i in range(REQUIRED_NUMBER_OF_SPECIAL_CHARACTERS):
        password_characters.append(random.choice(SPECIAL_CHARACTERS))
    while len(password_characters) < REQUIRED_NUMBER_OF_CHARACTERS:
        password_characters.append(
            random.choice(UPPERCASE_CHARACTERS + LOWERCASE_CHARACTERS + DIGITS + SPECIAL_CHARACTERS))
    random.shuffle(password_characters)
    for character in password_characters:
        random_password += character
    return random_password


# test_password_generator()

