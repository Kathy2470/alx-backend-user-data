#!/usr/bin/env python3
"""
API routes initialization.
"""

from flask import Flask
from api.v1.views.session_auth import auth as session_auth

def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)
    app.register_blueprint(session_auth)

    return app
