from db import Database
from models.user import User
from models.credentials import Credential
from security.hash import Hasher
from security.encrypt import Encryptor
from security.mfa import MFA
from utils.email_validator import EmailValidator
from utils.password_generator import PasswordGenerator

# Create a single Encryptor object
encryptor = Encryptor()

def main():
    db = Database()
    db.create_tables()

    while True:
        print("\n--- Password Manager ---")
        print("1. Create User Account")
        print("2. Login")
        print("3. Generate Password")
        print("4. Add Credential")
        print("5. View Credentials")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            create_user(db)
        elif choice == '2':
            login_user(db)
        elif choice == '3':
            generate_password()
        elif choice == '4':
            add_credential(db)
        elif choice == '5':
            view_credentials(db)
        elif choice == '6':
            print("Exiting the Password Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def create_user(db):
    email_validator = EmailValidator()
    username = input("Enter username: ")
    email = input("Enter email: ")

    # Validate email
    is_valid, message = email_validator.is_valid_with_feedback(email)
    if not is_valid:
        print(message)
        return

    password = input("Enter password: ")
    hashed_password = Hasher().hash_password(password)

    user = User(username, email, hashed_password)
    if db.add_user(user):
        print("User account created successfully.")
    else:
        print("Failed to create user account. Username or email may already be in use.")

def login_user(db):
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = db.get_user_by_username(username)
    if user:
        if Hasher().verify_password(password, user['hashed_password']):
            print("Login successful.")
            return user
        else:
            print("Invalid password.")
    else:
        print("Invalid username.")
    return None

def generate_password():
    length = int(input("Enter password length (default is 12): ") or 12)
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password_generator = PasswordGenerator(length, use_uppercase, use_digits, use_special_chars)
    password = password_generator.generate_password()
    print(f"Generated password: {password}")

def add_credential(db):
    user_id = input("Enter user ID: ")
    website = input("Enter website/service name: ")
    username = input("Enter username for the service: ")
    password = input("Enter password for the service: ")

    encrypted_password = encryptor.encrypt_password(password)
    credential = Credential(user_id, website, username, encrypted_password.hex())
    
    db.add_credential(credential)
    print("Credential added successfully.")

def view_credentials(db):
    user_id = input("Enter user ID: ")
    credentials = db.get_credentials_by_user_id(user_id)

    if credentials:
        print("--- Your Credentials ---")
        for cred in credentials:
            decrypted_password = encryptor.decrypt_password(cred['encrypted_password'])
            print(f"Website: {cred['website']}, Username: {cred['username']}, Password: {decrypted_password}")
    else:
        print("No credentials found for the user.")

if __name__ == "__main__":
    main()