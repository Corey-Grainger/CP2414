"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 8
MAX_LENGTH = 20
MIN_LOWERCASE = 1
MIN_UPPERCASE = 1
MIN_DIGIT = 1
MIN_SPECIAL = 1
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def is_valid_password(password):
    """Determine if password is a valid password."""
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_character_count = 0
    for char in password:
        if char.isupper():
            uppercase_count += 1
        if char.islower():
            lowercase_count += 1
        if char in SPECIAL_CHARACTERS:
            special_character_count += 1
        if char.isdigit():
            digit_count += 1
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    if uppercase_count < MIN_UPPERCASE or lowercase_count < MIN_LOWERCASE or digit_count < MIN_DIGIT:
        return False
    if IS_SPECIAL_CHARACTER_REQUIRED and special_character_count < MIN_SPECIAL:
        return False
    return True

