#!/usr/bin/env python3
""" API v1 views initialization
"""

from flask import Blueprint
from api.v1.views.session_auth import auth_bp

# Initialize Blueprint
v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

# Register blueprints
v1.register_blueprint(auth_bp)
