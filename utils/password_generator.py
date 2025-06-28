import string
import secrets

class PasswordGenerator:
    def __init__(self, length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_digits = use_digits
        self.use_special_chars = use_special_chars

    def generate_password(self):
        characters = string.ascii_lowercase
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_digits:
            characters += string.digits
        if self.use_special_chars:
            characters += string.punctuation

        return ''.join(secrets.choice(characters) for _ in range(self.length))