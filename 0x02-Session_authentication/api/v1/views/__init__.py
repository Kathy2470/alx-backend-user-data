#!/usr/bin/env python3
""" API v1 views initialization
"""

from flask import Blueprint

# Importing blueprints for session_auth
from api.v1.views.session_auth import auth as session_auth

# Initialize Blueprint
v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

# Register blueprints
v1.register_blueprint(session_auth)
