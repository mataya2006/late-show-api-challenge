# Late Show API Challenge

## Overview
This project is a Flask REST API for a Late Night TV show system built with:
- MVC architecture
- PostgreSQL database
- JWT token-based authentication
- Postman for API testing
- Git + GitHub for version control

## Folder Structure
```
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md
```

## Setup Instructions

### PostgreSQL Database
1. Install PostgreSQL if not already installed.
2. Create the database:
```sql
CREATE DATABASE late_show_db;
```

### Environment Variables
Set the following environment variables or update `server/config.py`:
- `DATABASE_URI`: PostgreSQL connection string, e.g. `postgresql://user:password@localhost:5432/late_show_db`
- `JWT_SECRET_KEY`: Secret key for JWT token generation

### Install Dependencies
Use pipenv to install dependencies:
```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### Database Migration and Seeding
Run the following commands to set up the database schema and seed data:
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

## Running the Application
Start the Flask development server:
```bash
python server/app.py
```

## Authentication Flow
- `POST /register`: Register a new user with `username` and `password`.
- `POST /login`: Login with credentials to receive a JWT access token.
- Protected routes require the header: `Authorization: Bearer <token>`.

## API Routes

| Route                  | Method | Auth Required | Description                          |
|------------------------|--------|---------------|------------------------------------|
| `/register`            | POST   | No            | Register a new user                 |
| `/login`               | POST   | No            | Login and receive JWT token         |
| `/episodes`            | GET    | No            | List all episodes                  |
| `/episodes/<int:id>`   | GET    | No            | Get episode details and appearances |
| `/episodes/<int:id>`   | DELETE | Yes           | Delete episode and related appearances |
| `/guests`              | GET    | No            | List all guests                    |
| `/appearances`         | POST   | Yes           | Create a new appearance            |

## Sample Request/Response

### Register
Request:
```json
{
  "username": "admin",
  "password": "password123"
}
```
Response:
```json
{
  "message": "User registered successfully"
}
```

### Login
Request:
```json
{
  "username": "admin",
  "password": "password123"
}
```
Response:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Create Appearance (Protected)
Request Header:
```
Authorization: Bearer <access_token>
```
Request Body:
```json
{
  "rating": 4,
  "guest_id": 1,
  "episode_id": 1
}
```
Response:
```json
{
  "id": 1,
  "rating": 4,
  "guest_id": 1,
  "episode_id": 1
}
```

## Postman Usage
Import the provided `challenge-4-lateshow.postman_collection.json` into Postman to test all API endpoints, including authentication and protected routes.

## GitHub Repository
[GitHub Repo Link](https://github.com/<username>/late-show-api-challenge)

## Notes
- Ensure PostgreSQL is running and accessible.
- Use the JWT token received from login for protected routes.
- The seed script populates initial data for users, guests, episodes, and appearances.

---

This completes the Late Show API Challenge setup and documentation.
