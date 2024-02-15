"""
CP2414 Password Save Function
"""

import csv
import pandas as pd


def create_password_file_entry(username, password, salt):
    with open('password_database.csv', 'a', encoding='utf-8') as out_file:
        password_writer = csv.writer(out_file)
        password_writer.writerow([username, password, salt])

def remove_password_file_entry(username):
    df = pd.read_csv('password_database.csv', encoding='utf-8')
    df = df.drop(df[df.Name == username].index)
    df.to_csv('password_database.csv', index=False, encoding='utf-8')

