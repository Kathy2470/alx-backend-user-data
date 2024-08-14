#!/usr/bin/env python3
"""
Authentication module.

This module provides the Auth class to handle user authentication,
including registering users and validating login credentials.
"""

import uuid
from sqlalchemy.exc import NoResultFound
from db import DB
from models.user import User
import bcrypt


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """
        Initialize the Auth class with a database instance.
        """
        self._db = DB()

    def _generate_uuid(self) -> str:
        """
        Generate a new UUID and return it as a string.

        Returns:
            str: A string representation of a new UUID.
        """
        return str(uuid.uuid4())

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with the given email and password.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            User: The created User object.

        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            user = User(
                email=email,
                hashed_password=hashed_password
            )
            self._db.add_user(user)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login credentials.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode(), user.hashed_password.encode()
            )
        except NoResultFound:
            return False

    def _hash_password(self, password: str) -> str:
        """
        Hash the given password using bcrypt.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed.decode()
