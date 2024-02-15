"""
CP2414 Password Save Function
"""

import csv


def create_password_file_entry(username: str, password: str, salt: int):
    with open('password_database.csv', 'a') as out_file:
        password_writer = csv.writer(out_file, )
        password_writer.writerow([username, password, salt])


def test_add_hashed_password():
    create_password_file_entry('Corey', "gggasdljdksfkjsnvjksa", 66)


test_add_hashed_password()
