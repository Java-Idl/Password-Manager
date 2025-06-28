from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt_password(self, password):
        return self.fernet.encrypt(password.encode())

    def decrypt_password(self, encrypted_password):
        return self.fernet.decrypt(encrypted_password).decode()