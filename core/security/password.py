import hashlib
import secrets
import string


class PasswordHandler:

    @staticmethod
    def generate_password(length=8) -> str:
        # Generate a random password with alphanumeric characters and special symbols
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password

    @staticmethod
    def hash(password: str) -> str:
        # Hash the password using SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify(hashed_password: str, password: str) -> bool:
        # Verify if the given password matches the hashed password
        return hashed_password == PasswordHandler.hash(password)

