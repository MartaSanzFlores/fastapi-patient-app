# Patient Appointment Manager

## Description

This project is a **FastAPI backend** application designed to manage patients and their medical appointments. It allows creating, reading, updating, and deleting patient records, as well as linking appointments to patients.

A simple **Vue.js frontend** is currently under construction to provide a basic user interface.

## Technologies Used

**Backend**
- Python 3.11
- FastAPI
- SQLModel (ORM based on SQLAlchemy)
- MySQL (via Docker)
- Docker Compose
- Pydantic (data validation)
- Pytest (unit testing)

**Frontend (WIP)**
- Vue.js 3 (Composition API)
- HTML/CSS

## Features

- Fast & lightweight REST API built with FastAPI
- Swagger UI for interactive documentation
- Dockerized architecture
- Unit-tested endpoints (Pytest)
- CRUD operations for patients and appointments
- Appointment linkage to specific patients
- Input validation with Pydantic
- Basic frontend: list, create & view patients (Vue.js - WIP)
- Graceful error handling (validation, duplicates, not found, etc.)

## Project Structure

- app/main.py : entry point, FastAPI setup
- app/models.py : SQLModel data models (Patient, Appointment)
- app/crud/ : CRUD logic (patients, appointments)
- app/routes/ : API route handlers
- app/database.py : database connection & table creation

---

## Installation & Running

### 1. Clone the repository

```bash
git clone https://github.com/MartaSanzFlores/fastapi-patient-app.git
cd AppFastPatients
```

### 2. Create a .env file with the following variables:

```bash
MYSQL_USER=myuser
MYSQL_PASSWORD=mypassword
MYSQL_DATABASE=patients_db
MYSQL_HOST=db
MYSQL_PORT=3306
DATABASE_URL=mysql+mysqlconnector://myuser:mypassword@db:3306/patients_db
```

### 3. Build and run the app with Docker:

```bash
docker-compose up --build
```

### 4. Test the API is running:

Visit http://localhost:8000
Expected response:

```bash
{"message":"API is up and running"}
```

### 5. Open the Swagger documentation:

Go to http://localhost:8000/docs

### TESTING

Run unit tests inside the container:

```bash
docker exec -it appfastpatients-app-1 pytest
```

## Possible Improvements

- User authentication (JWT)
- Frontend interface (Vue.js / React / simple HTML)
- Pagination & filtering in list endpoints
- Enhanced security (CORS, input sanitation)