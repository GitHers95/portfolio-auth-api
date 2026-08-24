# Portfolio Auth API

A REST API built with **FastAPI**, featuring JWT-based authentication and a PostgreSQL database, developed as part of a backend developer portfolio.

## Features

- User registration with secure password hashing (bcrypt)
- JWT-based login and authentication
- Protected routes using OAuth2 Bearer tokens
- PostgreSQL database with SQLAlchemy ORM
- Auto-generated interactive API documentation (Swagger UI)

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL + SQLAlchemy
- **Authentication:** JWT (python-jose) + Passlib (bcrypt)
- **Environment:** Python 3.13, Debian (WSL2)

## Project Structure


## API Endpoints

| Method | Endpoint         | Description                  | Auth required |
|--------|------------------|-------------------------------|----------------|
| POST   | `/auth/register` | Register a new user           | No             |
| POST   | `/auth/login`    | Login and receive a JWT token | No             |
| GET    | `/auth/me`       | Get current user info         | Yes            |

## Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL

### Installation

```bash
git clone https://github.com/GitHers95/portfolio-auth-api.git
cd portfolio-auth-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:


### Run the server

```bash
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for the interactive API documentation.

## Author

**GitHers95**