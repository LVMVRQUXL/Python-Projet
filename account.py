class Account:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def __get__username(self):
        return self._username

    def __get__password(self):
        return self._password

    def __set__username(self, username):
        if type(username) is not str or username == '':
            raise ValueError
        self._username = username

    def __set__password(self, password):
        if type(password) is not str or password == '':
            raise ValueError
        self._password = password

    def __str__(self):
        return '(username: {}; password: {})'.format(self._username, self._password)

    username = property(__get__username, __set__username)
    password = property(__get__password, __set__password)
