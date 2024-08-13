#!/usr/bin/env python3
"""
Users view module
"""

from flask import Blueprint, jsonify, request, abort
from models.user import User
from api.v1.auth import auth

users_bp = Blueprint('users', __name__)


@users_bp.route('', methods=['GET'])
def get_users():
    """
    Get all users
    """
    users = User.all()
    return jsonify([user.to_dict() for user in users])


@users_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a user
    """
    if user_id == 'me':
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict())
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@users_bp.route('', methods=['POST'])
def create_user():
    """
    Create a user
    """
    user = User.create(request.get_json())
    return jsonify(user.to_dict()), 201


@users_bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a user
    """
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.update(request.get_json())
    return jsonify(user.to_dict())


@users_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user
    """
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.delete()
    return jsonify({}), 200
