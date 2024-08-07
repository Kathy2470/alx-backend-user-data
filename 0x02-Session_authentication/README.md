0x02. Session authentication

User Authentication API

Overview
This project implements a user authentication system using Flask. The API supports user management, including creating, reading, updating, and deleting users, as well as handling session-based authentication.

Table of Contents
Getting Started
Requirements
Installation
Environment Variables
Usage
API Endpoints
License

Getting Started
These instructions will help you set up and run the project on your local machine for development and testing purposes.

Requirements
Python 3.7 or later
Flask
Flask-CORS

Environment Variables
You need to set the AUTH_TYPE environment variable to specify the authentication method:

auth: Basic authentication
basic_auth: Basic authentication with user credentials

API Endpoints
User Endpoints
GET /api/v1/users

Get a list of all users.
Response: List of user objects.
GET /api/v1/users/<user_id>

Get a specific user by ID. Use me as <user_id> to get the authenticated user.
Response: User object.
DELETE /api/v1/users/<user_id>

Delete a user by ID.
Response: Empty JSON object if the user is deleted.
POST /api/v1/users

Create a new user.
Request JSON: {"email": "user@example.com", "password": "password", "first_name": "First", "last_name": "Last"}
Response: Created user object.
PUT /api/v1/users/<user_id>

Update a user by ID.
Request JSON: {"first_name": "NewFirst", "last_name": "NewLast"}
Response: Updated user object.
Status Endpoints
GET /api/v1/status/

Get the status of the API.
Response: {"status": "OK"}
GET /api/v1/unauthorized/

Simulate an unauthorized error.
Response: 401 Unauthorized
GET /api/v1/forbidden/

Simulate a forbidden error.
Response: 403 Forbidden
