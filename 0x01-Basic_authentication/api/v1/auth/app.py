#!/usr/bin/env python3
"""Basic Authentication Module."""

from typing import Any, Dict, Tuple

from flask import Flask, jsonify, request, abort
from models import User

app = Flask(__name__)


def check_auth(username: str, password: str) -> bool:
    """Check if a username and password are correct.

    Args:
        username (str): The username to check.
        password (str): The password to check.

    Returns:
        bool: True if authentication is successful, otherwise False.
    """
    user = User.get_user(username)
    if user and user.check_password(password):
        return True
    return False


def authenticate() -> None:
    """Send a 401 response that enables Basic Auth."""
    abort(401, 'Authentication required')


@app.route('/login', methods=['POST'])
def login() -> Tuple[str, int]:
    """Handle login requests.

    Returns:
        Tuple[str, int]: A tuple containing response message,status code.
    """
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        authenticate()
    return jsonify({'message': 'Login successful'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
