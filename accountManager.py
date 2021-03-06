import os.path as path
from typing import List

from account import Account
from securityManager import SecurityManager


def equal_accounts(account_1: Account, account_2: Account) -> bool:
    if account_1.username != account_2.username or \
            account_1.password != account_2.password or \
            account_1.description != account_2.description:
        return False
    return True


def find_account_index(accounts: List[Account], account: Account) -> int:
    index = 0
    for acc in accounts:
        if equal_accounts(acc, account):
            break
        index = index + 1
    return index


class AccountManager:
    def __init__(self):
        self.__filename = 'accounts'
        self.__security = SecurityManager()
        if not path.isfile('./{}.csv'.format(self.__filename)):
            self.__create_csv_file()

    def add_account(self, account: Account):
        if self.__is_account_already_exists(account) is False:
            with open('{}.csv'.format(self.__filename), 'a') as file:
                password = self.__security.encrypt_password(account.password)
                line = '{};{};{}\n'.format(account.username, password, account.description)
                file.write(line)
        else:
            print('{} already exists!'.format(account))

    def get_all_accounts(self) -> List[Account]:
        with open('{}.csv'.format(self.__filename), 'r') as file:
            lines = [line.split(';') for line in file.read().splitlines()[1:]]
            arr = list(map(self.__map_array_to_account, lines))
            return arr

    def remove_account(self, account: Account):
        if self.__is_account_already_exists(account) is True:
            accounts = self.get_all_accounts()
            index = find_account_index(accounts, account)
            accounts.pop(index)
            self.__write_accounts_in_csv_file(accounts)

    def update_account(self, old_account: Account, new_account: Account):
        if self.__is_account_already_exists(old_account) is True:
            accounts = self.get_all_accounts()
            index = find_account_index(accounts, old_account)
            accounts[index] = new_account
            self.__write_accounts_in_csv_file(accounts)

    def __create_csv_file(self):
        with open('{}.csv'.format(self.__filename), 'w') as file:
            csv_columns = 'username;password;description\n'
            file.write(csv_columns)

    def __is_account_already_exists(self, account: Account) -> bool:
        accounts = self.get_all_accounts()
        res = [True if equal_accounts(account, acc) else False for acc in accounts]
        return any(res)

    def __map_array_to_account(self, array: List[str]) -> Account:
        password = self.__security.decrypt_password(array[1])
        return Account(array[0], password, array[2])

    def __write_accounts_in_csv_file(self, accounts: List[Account]):
        self.__create_csv_file()
        for acc in accounts:
            self.add_account(acc)

    def __str__(self) -> str:
        return 'AccountManager(filename: {})'.format(self.__filename)
