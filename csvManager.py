import os.path as path

from cryptography.fernet import Fernet
from typing import List

from account import Account


def encrypt_password(password, key) -> str:
    return key.encrypt(password.encode()).decode()


def decrypt_password(password, key) -> str:
    return key.decrypt(password.encode()).decode()


class CSVManager:
    def __init__(self):
        self.__filename = 'accounts'
        if not path.isfile('./key.security'):
            self.__create_key_security_file()
        else:
            self.__set_secret_key_from_file()
        if not path.isfile('./{}.csv'.format(self.__filename)):
            self.__create_file()

    def __str__(self) -> str:
        return 'CSVManager(filename: {})'.format(self.__filename)

    def __create_key_security_file(self):
        self.__set_secret_key(Fernet.generate_key())
        with open('key.security', 'w') as file:
            file.write('{}\n'.format(self.__secret_key.decode()))

    def __create_file(self):
        with open('{}.csv'.format(self.__filename), 'w') as file:
            csv_columns = 'username;password;description\n'
            file.write(csv_columns)

    def __map_array_to_account(self, array) -> Account:
        password = decrypt_password(array[1], self.__secret_key)
        return Account(array[0], password, array[2])

    def __set_secret_key(self, secret_key):
        self.__secret_key = secret_key

    def __set_secret_key_from_file(self):
        with open('key.security', 'r') as file:
            key = ''.join(file.read().splitlines())
            self.__set_secret_key(Fernet(key.encode()))

    def add_account(self, account):
        with open('{}.csv'.format(self.__filename), 'a') as file:
            password = encrypt_password(account.password, self.__secret_key)
            line = '{};{};{}\n'.format(account.username, password, account.description)
            file.write(line)

    def get_all_accounts(self) -> List[Account]:
        with open('{}.csv'.format(self.__filename), 'r') as file:
            lines = [line.split(';') for line in file.read().splitlines()[1:]]
            arr = list(map(self.__map_array_to_account, lines))
            return arr
