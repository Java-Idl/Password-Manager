import re

class EmailValidator:
    def __init__(self):
        # Regular expression pattern for validating an Email
        self.email_pattern = re.compile(
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        )

    def is_valid(self, email):
        """
        Validate the given email address.
        
        :param email: Email address to validate.
        :return: True if valid, False otherwise.
        """
        return bool(self.email_pattern.match(email))

    def is_valid_with_feedback(self, email):
        """
        Validate the given email address and provide feedback.
        
        :param email: Email address to validate.
        :return: Tuple (is_valid, feedback message).
        """
        if not isinstance(email, str):
            return False, "Email must be a string."

        if not email:
            return False, "Email cannot be empty."

        if self.is_valid(email):
            return True, "Email is valid."
        
        return False, "Email is invalid. Please check the format."