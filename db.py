import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file="password_manager.db"):
        self.connection = None
        try:
            self.connection = sqlite3.connect(db_file)
            self.connection.row_factory = sqlite3.Row  # To return dict-like rows
            self.create_tables()
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            
            # Users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    hashed_password TEXT NOT NULL
                );
            ''')

            # Credentials table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS credentials (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    website TEXT NOT NULL,
                    username TEXT NOT NULL,
                    encrypted_password TEXT NOT NULL,
                    FOREIGN KEY ( user_id) REFERENCES users (id)
                );
            ''')

            self.connection.commit()
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_user(self, user):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO users (username, email, hashed_password)
                VALUES (?, ?, ?)
            ''', (user.username, user.email, user.hashed_password))
            self.connection.commit()
            return cursor.lastrowid  # Return the user ID
        except Error as e:
            print(f"Error adding user: {e}")
            return None

    def get_user_by_username(self, username):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT * FROM users
                WHERE username = ?
            ''', (username,))
            row = cursor.fetchone()
            if row:
                return dict(row)
            else:
                return None
        except Error as e:
            print(f"Error getting user by username: {e}")
            return None

    def add_credential(self, credential):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO credentials (user_id, website, username, encrypted_password)
                VALUES (?, ?, ?, ?)
            ''', (credential.user_id, credential.website, credential.username, credential.encrypted_password))
            self.connection.commit()
            return cursor.lastrowid  # Return the credential ID
        except Error as e:
            print(f"Error adding credential: {e}")
            return None

    def get_credentials_by_user_id(self, user_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT * FROM credentials
                WHERE user_id = ?
            ''', (user_id,))
            rows = cursor.fetchall()
            if rows:
                return [dict(row) for row in rows]
            else:
                return []
        except Error as e:
            print(f"Error getting credentials by user ID: {e}")
            return []