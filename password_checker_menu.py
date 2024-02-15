from automatic_password_generator import generate_random_password
from password_checker import is_valid_password
from password_hashing import hash_password
from password_hashing import cross_reference_hashed_password

MENU = 'menu goes here'


def main():
    print(MENU)
    choice = int(input('> '))
    while choice != 3:
        if choice == 1:
            password = generate_random_password()
            print(password)
        elif choice == 2:
            password = input('Password: ')
            while not is_valid_password(password):
                print('invalid')
                password = input('Password: ')
            print(password)
            print('Success!')
        else:
            print('Invalid Input')
        print(MENU)
        choice = int(input('> '))
    print('Done')
    hashed_password = hash_password(password)


if __name__ == '__main__':
    main()
