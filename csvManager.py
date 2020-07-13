import os.path as path
from typing import List

from account import Account


def map_array_to_account(array) -> Account:
    return Account(array[0], array[1], array[2])


class CSVManager:
    def __init__(self):
        self.__filename = 'accounts'
        self.__secret_key = 'something'
        if not path.isfile('./{}.csv'.format(self.__filename)):
            self.__create_file()

    def __get_filename(self) -> str:
        return self.__filename

    def __create_file(self):
        with open('{}.csv'.format(self.__filename), 'w') as file:
            csv_columns = 'username;password;description\n'
            file.write(csv_columns)

    def __str__(self) -> str:
        return 'CSVManager(filename: {})'.format(self.__filename)

    def add_account(self, account):
        with open('{}.csv'.format(self.__filename), 'a') as file:
            line = '{};{};{}\n'.format(account.username, account.password, account.description)
            file.write(line)

    def get_all_accounts(self) -> List[Account]:
        with open('{}.csv'.format(self.__filename), 'r') as file:
            lines = [line.split(';') for line in file.read().splitlines()[1:]]
            arr = list(map(map_array_to_account, lines))
            return arr
