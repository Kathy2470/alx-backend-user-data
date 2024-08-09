#!/usr/bin/env python3
"""
Module that contains the method to get the current user.
"""

from flask import request
from api.v1.auth.session_auth import SessionAuth


class Auth:
    def __init__(self):
        self.session_auth = SessionAuth()

    def current_user(self, request=None):
        """
        Returns the current user based on the session cookie in the request.
        """
        if request is None:
            return None
        session_cookie = self.session_auth.session_cookie(request)
        if session_cookie is None:
            return None
        user_id = self.session_auth.user_id_for_session_id(session_cookie)
        if user_id is None:
            return None
        # Assuming User class exists with a method to get a user by ID
        return User.get(user_id)
