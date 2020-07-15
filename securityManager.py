import os.path as path

from cryptography.fernet import Fernet


class SecurityManager:
    def __init__(self):
        if not path.isfile('./key.security'):
            self.__create_key_security_file()
        else:
            self.__read_secret_key_from_file()
        self.__init_cipher()

    def encrypt_password(self, password: str) -> str:
        return self.__cipher.encrypt(password.encode()).decode()

    def decrypt_password(self, password: str) -> str:
        return self.__cipher.decrypt(password.encode()).decode()

    def __create_key_security_file(self):
        self.__init_secret_key(Fernet.generate_key())
        with open('key.security', 'w') as file:
            file.write('{}\n'.format(self.__secret_key.decode()))

    def __init_cipher(self):
        self.__cipher = Fernet(self.__secret_key)

    def __init_secret_key(self, value: bytes):
        self.__secret_key = value

    def __read_secret_key_from_file(self):
        with open('key.security', 'r') as file:
            key = ''.join(file.read().splitlines())
            self.__init_secret_key(key.encode())

    def __str__(self) -> str:
        return 'SecurityManager(secret_key: {})'.format(self.__secret_key)
