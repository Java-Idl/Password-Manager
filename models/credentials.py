class Credential:
    def __init__(self, user_id, website, username, encrypted_password):
        self.user_id = user_id
        self.website = website
        self.username = username
        self.encrypted_password = encrypted_password