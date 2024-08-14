#!/usr/bin/env python3
"""
Flask app for user registration.
"""

from flask import Flask, request, jsonify
from auth import Auth
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)

# Instantiate the Auth object
AUTH = Auth()


@app.route("/", methods=["GET"])
def home():
    """Handle GET requests at the root endpoint."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """Handle POST requests to register a user."""
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"message": "email and password are required"}), 400

    try:
        # Attempt to register the user
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 201
    except ValueError as e:
        # Handle user already exists error
        return jsonify({"message": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
