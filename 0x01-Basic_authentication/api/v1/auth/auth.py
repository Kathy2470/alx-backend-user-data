#!/usr/bin/env python3
""" Auth module
"""
from typing import List, TypeVar
from flask import request

User = TypeVar('User')

class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns True if path is not in the excluded_paths list """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        path = path if path.endswith('/') else path + '/'
        return path not in (excluded_path if excluded_path.endswith('/') else excluded_path + '/' for excluded_path in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """ Returns the value of the Authorization header from the request """
        if request is None or not hasattr(request, 'headers'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """ Returns the current user based on the request """
        return None
