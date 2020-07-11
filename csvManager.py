import os.path as path


class CSVManager:
    def __init__(self):
        self.__filename = 'accounts'
        self.__secret_key = 'something'
        if not path.isfile('./{}.csv'.format(self.__filename)):
            self.__create_file()

    def __get_filename(self):
        return self.__filename

    def __create_file(self):
        with open('{}.csv'.format(self.__filename), 'w') as file:
            csv_columns = 'username;password;description\n'
            file.write(csv_columns)

    def __str__(self):
        return 'CSVManager(filename: {})'.format(self.__filename)

    def add_account(self, account):
        with open('{}.csv'.format(self.__filename), 'a') as file:
            line = '{};{};{}\n'.format(account.username, account.password, account.description)
            file.write(line)
