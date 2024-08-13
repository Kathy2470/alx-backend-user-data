#!/usr/bin/env python3
""" Users view module
"""
from api.v1.app import app
from models.user import User
from api.v1.auth import auth

def get_users():
    """Get all users"""
    users = User.all()
    return jsonify([user.to_dict() for user in users])

def get_user(user_id):
    """Get a user"""
    if user_id == 'me':
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict())
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())

def create_user():
    """Create a user"""
    user = User.create(request.get_json())
    return jsonify(user.to_dict()), 201

def update_user(user_id):
    """Update a user"""
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.update(request.get_json())
    return jsonify(user.to_dict())

def delete_user(user_id):
    """Delete a user"""
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.delete()
    return jsonify({}), 200
