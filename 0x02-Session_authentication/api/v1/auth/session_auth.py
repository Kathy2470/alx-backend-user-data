#!/usr/bin/env python3
"""
Session Authentication module.
"""

from flask import request, jsonify
from models.user import User
from api.v1.app import auth


class SessionAuth:
    def __init__(self):
        self.user_id_by_session_id = {}

    def session_cookie(self, request=None):
        """
        Returns the session cookie from the request.
        """
        if request is None:
            return None
        return request.cookies.get(os.getenv('SESSION_NAME'))

    def user_id_for_session_id(self, session_id=None):
        """
        Returns the user ID for a given session ID.
        """
        if session_id is None:
            return None
        return self.user_id_by_session_id.get(session_id)

    def create_session(self, user_id=None):
        """
        Creates a session ID for the user ID.
        """
        import uuid
        if user_id is None:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def destroy_session(self, request=None):
        """
        Deletes the user session / logout.
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        if self.user_id_for_session_id(session_id) is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
