#!/usr/bin/env python3
"""
App module
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from api.v1.views.users import (
    get_users, get_user, create_user, update_user, delete_user
)
from api.v1.auth import auth

app = Flask(__name__)
CORS(app, origins='*')


@app.before_request
def before_request():
    """
    Before request function
    """
    request.current_user = auth.current_user(request)


@app.errorhandler(404)
def not_found(error):
    """
    Error 404 handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error):
    """
    Error 401 handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Status route
    """
    return jsonify({"status": "OK"})


app.add_url_rule(
    '/api/v1/users', view_func=get_users, methods=['GET'],
    strict_slashes=False
)
app.add_url_rule(
    '/api/v1/users', view_func=create_user, methods=['POST'],
    strict_slashes=False
)
app.add_url_rule(
    '/api/v1/users/<user_id>', view_func=get_user, methods=['GET'],
    strict_slashes=False
)
app.add_url_rule(
    '/api/v1/users/<user_id>', view_func=update_user, methods=['PUT'],
    strict_slashes=False
)
app.add_url_rule(
    '/api/v1/users/<user_id>', view_func=delete_user, methods=['DELETE'],
    strict_slashes=False
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
