password_manager/
│
├── database/
│   └── db.py           # Handle database connections (MySQL/Oracle) and operations.
│
├── models/
│   ├── user.py         # User model: class for user management (CRUD).
│   └── credential.py   # Credential model: class for credential management (CRUD).
│
├── security/
│   ├── hash.py         # Password hashing (bcrypt) for user and master password.
│   ├── encrypt.py      # AES-256 encryption for storing website credentials.
│   └── mfa.py          # Multi-Factor Authentication logic (Optional).
│
├── utils/
│   ├── password_generator.py   # Generate strong, customizable passwords.
│   └── email_validator.py      # Helper to validate emails (regex or service).
│
├── views/
│   ├── cli.py           # Command-line interface (if not using a GUI).
│   └── gui.py           # (Optional) If you choose to build a GUI.
│
├── main.py              # Main entry point to run the program.
│
└── requirements.txt     # For Python dependencies (bcrypt, pycryptodome, etc.).
