class User:
    def __init__(self, username, email, hashed_password):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password