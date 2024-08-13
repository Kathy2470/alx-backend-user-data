#!/usr/bin/env python3
"""
App module
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from api.v1.views.users import users_bp
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


# Register the Blueprint
app.register_blueprint(users_bp, url_prefix='/api/v1/users')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
