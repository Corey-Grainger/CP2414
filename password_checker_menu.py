"""CP2414 Password example program"""

import csv
from automatic_password_generator import generate_random_password
from password_checker import is_valid_password
from password_hashing import hash_password
from password_save_function import create_password_file_entry
from password_save_function import remove_password_file_entry
from password_hashing import cross_reference_hashed_password

MENU = '(S)ign up\n(C)hange password\n(L)ogin\n(Q)uit'


def main():
    print(MENU)
    choice = (input('> ').upper())
    while choice != "Q":
        if choice == "S":
            requested_username = get_valid_username()
            hashed_password, salt = get_valid_password()
            create_password_file_entry(requested_username, hashed_password, salt)
            print('Account Created!')
        elif choice == "C":
            username = input("Enter username: ")
            current_password = input("Enter old password: ")
            is_valid_credential = authenticate_password(username, current_password)
            while not is_valid_credential:
                print("Invalid username of password")
                username = input("Enter username: ")
                current_password = input("Enter old password: ")
                is_valid_credential = authenticate_password(username, current_password)
            new_password, salt = get_valid_password()
            remove_password_file_entry(username)
            create_password_file_entry(username, new_password, salt)
        elif choice == "L":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authenticate_password(username, password):
                print("Access granted")
            else:
                print("Invalid username or password")
        else:
            print('Invalid Input')
        print(MENU)
        choice = (input('> ')).upper()
    print('Done')


def get_valid_password():
    random_password = generate_random_password()
    print(f"Your suggested random password is {random_password}")
    password = input('Password: ')
    password_confirmation = input('Confirm Password: ')
    while not is_valid_password(password, password_confirmation):
        print('invalid')
        password = input('Password: ')
        password_confirmation = input('Confirm Password: ')
    hashed_password, salt = hash_password(password)
    return hashed_password, salt


def get_valid_username():
    username = input("Enter username: ")
    while not is_valid_username(username):
            print("Username already in use")
            username = input("Enter username: ")
    return username


def is_valid_username(username):
    with open("password_database.csv", 'r') as in_file:
        reader = csv.DictReader(in_file, delimiter=',')
        for row in reader:
            saved_username = row['Username']
            if username.lower() == saved_username.lower():
                return False
        return True


def authenticate_password(username, password):
    with open("password_database.csv", 'r') as in_file:
        reader = csv.DictReader(in_file, delimiter=',')
        for row in reader:
            saved_username = row['Username']
            hashed_password = row['Hash_Password']
            if username == saved_username:
                return cross_reference_hashed_password(password, hashed_password)
        return False


if __name__ == '__main__':
    main()
