#!/usr/bin/env python3


"""
Module defining the User model for the users table.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """
    User model for the users table.

    Attributes:
        id (int): The primary key of the user record.
        email (str): The user's email address.
        hashed_password (str): The hashed password of the user.
        session_id (str): The session ID of the user.
        reset_token (str): The password reset token for the user.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
