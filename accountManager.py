import os.path as path
from typing import List

from account import Account
from security import SecurityManager


class AccountManager:
    def __init__(self):
        self.__filename = 'accounts'
        self.__security = SecurityManager()
        if not path.isfile('./{}.csv'.format(self.__filename)):
            self.__create_csv_file()

    def add_account(self, account: Account):
        with open('{}.csv'.format(self.__filename), 'a') as file:
            password = self.__security.encrypt_password(account.password)
            line = '{};{};{}\n'.format(account.username, password, account.description)
            file.write(line)

    def get_all_accounts(self) -> List[Account]:
        with open('{}.csv'.format(self.__filename), 'r') as file:
            lines = [line.split(';') for line in file.read().splitlines()[1:]]
            arr = list(map(self.__map_array_to_account, lines))
            return arr

    def __create_csv_file(self):
        with open('{}.csv'.format(self.__filename), 'w') as file:
            csv_columns = 'username;password;description\n'
            file.write(csv_columns)

    def __map_array_to_account(self, array: List[str]) -> Account:
        password = self.__security.decrypt_password(array[1])
        return Account(array[0], password, array[2])

    def __str__(self) -> str:
        return 'AccountManager(filename: {})'.format(self.__filename)
