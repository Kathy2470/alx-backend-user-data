#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

class DB:
    """
    DB class
    """
    def __init__(self):
        """
        Initialize DB instance
        """
        self._session = self.create_session()

    def create_session(self):
        """
        Create a new database session
        """
        engine = create_engine('mysql://root:root@localhost/my_db')
        Session = sessionmaker(bind=engine)
        return Session()

    def find_user_by(self, **kwargs):
        """
        Find a user by arbitrary keyword arguments

        Args:
            **kwargs: arbitrary keyword arguments

        Returns:
            User: the first user found matching the keyword arguments

        Raises:
            InvalidRequestError: if the keyword arguments are invalid
            NoResultFound: if no user is found matching the keyword arguments
        """
        try:
            return self._session.query(User).filter_by(**kwargs).first()
        except InvalidRequestError:
            raise
        except Exception as e:
            raise e
