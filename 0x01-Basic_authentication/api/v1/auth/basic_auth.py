#!/usr/bin/env python3
""" BasicAuth module
"""

import base64
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User

UserType = TypeVar('UserType', bound='User')


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """ Extracts the Base64 part of the Authorization header """
        if (authorization_header is None or
                not isinstance(authorization_header, str)):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ Decodes the Base64 Authorization header """
        if (base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None
        try:
            decoded_bytes = base64.b64decode(
                base64_authorization_header
            )
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """ Extracts user email and password from the decoded Base64 header """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str)):
            return None, None
        credentials = decoded_base64_authorization_header.split(':', 1)
        if len(credentials) != 2:
            return None, None
        return tuple(credentials)

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> UserType:
        """ Retrieves the User instance based on email and password """
        if (user_email is None or not isinstance(user_email, str) or
                user_pwd is None or not isinstance(user_pwd, str)):
            return None
        users = User.search({'email': user_email})
        if not users:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> UserType:
        """ Overridden method to retrieve the User instance for a request """
        auth_header = self.authorization_header(request)
        base64_auth = self.extract_base64_authorization_header(auth_header)
        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        email, password = self.extract_user_credentials(decoded_auth)
        return self.user_object_from_credentials(email, password)
