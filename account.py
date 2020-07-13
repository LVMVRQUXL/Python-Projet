def is_valid_str(string: str) -> bool:
    if type(string) is not str or string == '':
        return False
    return True


class Account:
    def __init__(self, username: str, password: str, description: str):
        if is_valid_str(username) is False or \
                is_valid_str(password) is False or \
                is_valid_str(description) is False:
            raise ValueError
        self.username = username
        self.password = password
        self.description = description

    def __get__description(self) -> str:
        return self.__description

    def __get__password(self) -> str:
        return self.__password

    def __get__username(self) -> str:
        return self.__username

    def __set__description(self, description: str):
        self.__description = description

    def __set__password(self, password: str):
        self.__password = password

    def __set__username(self, username: str):
        self.__username = username

    def __str__(self) -> str:
        return 'Account(username: {}, password: {}, description: {})'.format(
            self.username, self.password, self.description
        )

    description = property(__get__description, __set__description)
    password = property(__get__password, __set__password)
    username = property(__get__username, __set__username)
