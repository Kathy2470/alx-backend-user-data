#!/usr/bin/env python3
""" Main module for API
"""

from flask import Flask
from api.v1.views import v1  # Ensure this is the correct import

def create_app():
    """ Create and configure the app
    """
    app = Flask(__name__)
    app.register_blueprint(v1)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
