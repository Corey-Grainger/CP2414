UPPER_ASCII_VALUE_BOUNDARY = 126
LOWER_ASCII_VALUE_BOUNDARY = 32


def get_caesar_cipher_key():
    key = int(input("Please enter number of shifts for encryption: "))
    return key


def encrypt_using_caesar_cipher(plaintext, key):
    encrypted_characters = []
    for primary_character in plaintext:
        primary_value = ord(primary_character)
        secondary_value = primary_value + key
        processed_value = maintain_value_within_bounds(secondary_value)
        secondary_character = chr(processed_value)
        encrypted_characters.append(secondary_character)
    ciphertext = "".join(encrypted_characters)
    return ciphertext


def maintain_value_within_bounds(secondary_value):
    if secondary_value > UPPER_ASCII_VALUE_BOUNDARY:
        processed_value = LOWER_ASCII_VALUE_BOUNDARY + (secondary_value - UPPER_ASCII_VALUE_BOUNDARY)
    elif secondary_value < LOWER_ASCII_VALUE_BOUNDARY:
        processed_value = UPPER_ASCII_VALUE_BOUNDARY - (LOWER_ASCII_VALUE_BOUNDARY - secondary_value)
    else:
        processed_value = secondary_value
    return processed_value


def decrypt_using_caesar_cipher(ciphertext, key):
    decrypted_characters = []
    for primary_character in ciphertext:
        primary_value = ord(primary_character)
        secondary_value = primary_value - key
        processed_value = maintain_value_within_bounds(secondary_value)
        secondary_character = chr(processed_value)
        decrypted_characters.append(secondary_character)
    decrypted_text = "".join(decrypted_characters)
    return decrypted_text


def run_tests():
    key = get_caesar_cipher_key()
    plaintext = input("Message to encrypt: ")
    ciphertext = encrypt_using_caesar_cipher(plaintext, key)
    print(ciphertext)
    print(f"Decrypting message, output should be {plaintext}:")
    decrypted_text = decrypt_using_caesar_cipher(ciphertext, key)
    print(decrypted_text)


# run_tests()
