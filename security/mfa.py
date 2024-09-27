import pyotp
import qrcode

class MFA:
    def __init__(self, user_email):
        self.user_email = user_email
        self.secret = pyotp.random_base32()  # Generates a random secret for the user

    def generate_qr_code(self, issuer="PasswordManager"):
        totp = pyotp.TOTP(self.secret)
        uri = totp.provisioning_uri(self.user_email, issuer_name=issuer)
        qr = qrcode.make(uri)
        return qr

    def verify_token(self, token):
        totp = pyotp.TOTP(self.secret)
        return totp.verify(token)