#!/usr/bin/env python3
""" User model module
"""
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """User class"""
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True)
    email = Column(String(60), nullable=False)
    password = Column(String(60), nullable=False)
    first_name = Column(String(60), nullable=True)
    last_name = Column(String(60), nullable=True)

    def to_dict(self):
        """Convert to dictionary"""
        return {
            'email': self.email,
            'first_name': self.first_name,
            'id': self.id,
            'last_name': self.last_name
        }

    @classmethod
    def create(cls, data):
        """Create a new user"""
        new_user = cls(**data)
        new_user.save()
        return new_user

    def update(self, data):
        """Update a user"""
        for key, value in data.items():
            setattr(self, key, value)
        self.save()

    def delete(self):
        """Delete a user"""
        self.delete()

    @classmethod
    def get(cls, user_id):
        """Get a user by ID"""
        return cls.query.get(user_id)

    @classmethod
    def all(cls):
        """Get all users"""
        return cls.query.all()
