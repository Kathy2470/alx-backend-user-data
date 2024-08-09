#!/usr/bin/env python3
""" Session Authentication view routes.
"""

from flask import Blueprint, request, jsonify, abort
from models.user import User
import os

auth = Blueprint('session_auth', __name__)

@auth.route('/api/v1/auth_session/login', methods=['POST'])
def login():
    """
    Handle user login, create session and return user info.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search(email=email)
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Import SessionAuth here to avoid circular import issues
    from api.v1.app import auth as app_auth
    session_id = app_auth.create_session(user.id)
    if session_id is None:
        return jsonify({"error": "session creation failed"}), 500

    response = jsonify(user.to_json())
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return response

@auth.route('/api/v1/auth_session/logout', methods=['DELETE'])
def logout():
    """
    Handle user logout and destroy session.
    """
    # Import SessionAuth here to avoid circular import issues
    from api.v1.app import auth as app_auth
    if not app_auth.destroy_session(request):
        abort(404)
    return jsonify({})
