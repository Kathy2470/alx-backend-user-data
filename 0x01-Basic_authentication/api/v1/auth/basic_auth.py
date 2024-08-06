#!/usr/bin/env python3
""" Basic Auth Module
"""
from typing import TypeVar, Tuple
from models.user import User
import base64

# Type variable for User instance
User = TypeVar('User', bound='User')


class BasicAuth:
    """ Basic Auth class for Basic Authentication
    """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """ Extracts the Base64 part of the Authorization header
        """
        if (authorization_header is None or
                not isinstance(authorization_header, str) or
                not authorization_header.startswith("Basic ")):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ Decodes the Base64 authorization header
        """
        if (base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            return message_bytes.decode('utf-8')
        except (TypeError, ValueError):
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """ Extracts the user email and password from the decoded Base64
        """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str) or
                ':' not in decoded_base64_authorization_header):
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> User:
        """ Returns the User instance based on email and password
        """
        if (user_email is None or not isinstance(user_email, str) or
                user_pwd is None or not isinstance(user_pwd, str)):
            return None
        users = User.search(user_email)
        if not users:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user
