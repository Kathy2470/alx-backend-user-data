#!/usr/bin/env python3
"""
Flask app module
"""

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def home():
    """Returns a JSON payload with a welcome message.
    """
    return jsonify(message="Bienvenue")


@app.route("/users", methods=["POST"])
def register_user():
    """Registers a new user with the provided email and password.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not email or not password:
        return jsonify(message="email and password are required"), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify(email=user.email, message="user created")
    except ValueError as e:
        return jsonify(message=str(e)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
