#!/usr/bin/env python3
"""
Auth module
"""

from db import DB
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.exc import NoResultFound
import uuid

class User:
    def __init__(self, email: str, hashed_password: bytes):
        self.email = email
        self.hashed_password = hashed_password


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize Auth instance."""
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hashes a password using bcrypt.

        Args:
            password (str): The password to hash.

        Returns:
            bytes: The hashed password.
        """
        return hashpw(password.encode('utf-8'), gensalt())

    def _generate_uuid(self) -> str:
        """Generates a new UUID.

        Returns:
            str: The string representation of the UUID.
        """
        return str(uuid.uuid4())

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user with email and password.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            User: The registered user.

        Raises:
            ValueError: If the user already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Validates a user's login credentials.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            bool: True if the login is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False
