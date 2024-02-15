"""Automatic password generator"""

import random
from password_checker import is_valid_password


def main():
    """Program to generate a random password with a specified requirements and check the password
    matches the requirements."""
    required_number_of_characters = int(input("How many characters: "))
    required_number_of_uppercase_characters = int(input("How many uppercase characters: "))
    required_number_of_lowercase_characters = int(input("How many lowercase characters: "))
    required_number_of_digits = int(input("How many digits: "))
    required_number_of_special_characters = int(input("How many special characters: "))
    random_password = generate_random_password(required_number_of_characters, required_number_of_uppercase_characters,
                                               required_number_of_lowercase_characters,
                                               required_number_of_special_characters, required_number_of_digits)
    print(random_password)
    print(is_valid_password(random_password, required_number_of_characters, required_number_of_characters,
                            required_number_of_uppercase_characters, required_number_of_lowercase_characters,
                            required_number_of_digits, required_number_of_special_characters))


def generate_random_password(required_number_of_characters=12, required_number_of_uppercase_characters=1,
                             required_number_of_lowercase_characters=1, required_number_of_special_characters=1,
                             required_number_of_digits=1, uppercase_characters="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                             lowercase_characters="abcdefghijklmnopqrstuvwxyz", digits="1234567890",
                             special_characters="!@#$%^&*()_-=+`~,./'[]<>?{}|\\"):
    """Generate a random password with the specified length and combination of characters."""
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


def test_password_generator():
    password = generate_random_password()
    print(password)
    print(is_valid_password(password))
    password = generate_random_password()
    print(password)
    print(is_valid_password(password))


# test_password_generator()
main()
