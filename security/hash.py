import bcrypt

class Hasher:
    def __init__(self, salt_rounds=12):
        self.salt_rounds = salt_rounds

    def hash_password(self, plain_password):
        salt = bcrypt.gensalt(self.salt_rounds)
        hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def verify_password(self, plain_password, hashed_password):
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))