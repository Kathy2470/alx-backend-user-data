#!/usr/bin/env python3
"""
Main file
"""
import logging

from auth import Auth

# Suppress SQLAlchemy engine logging
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print(f"could not create a new user: {err}")

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print(f"could not create a new user: {err}")
