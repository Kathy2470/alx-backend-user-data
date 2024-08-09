#!/usr/bin/env python3
"""Session authentication views module
"""

from flask import Blueprint, request, jsonify
from models.user import User
from api.v1.app import auth  # Import here to avoid circular import issues

auth_bp = Blueprint('session_auth', __name__)

@auth_bp.route('/auth_session/login', methods=['POST'])
def login():
    """Handles POST requests to authenticate a user and create a session
    """
    from api.v1.app import auth  # Import inside the function to avoid circular import

    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search(email=email)
    if user is None:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(SESSION_NAME, session_id)
    return response
