# FastAPI Geo Data API

This project is a FastAPI-based application for managing geo-data with PostgreSQL and PostGIS support. The API supports CRUD operations and is integrated with Swagger UI for API documentation.

---

## Features
- RESTful API for managing geo-data.
- Swagger UI available at `/docs` for testing endpoints.
- Uses PostgreSQL with PostGIS for spatial data management.

---

## Local Setup (Without Docker)

### Prerequisites
1. **Python 3.10 or higher**
2. **PostgreSQL with PostGIS enabled**
3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
### Steps

 Clone the repository: ```bash git clone <repository-url>
        cd <repository-folder> ```

Configure the database:

    Install PostgreSQL and enable PostGIS extension:

sudo apt-get install postgresql postgresql-contrib postgis

Start PostgreSQL service:

sudo service postgresql start

Create a database with PostGIS:

CREATE DATABASE geo_database;
\c geo_database;
CREATE EXTENSION postgis;

Update the DATABASE_URL in app/config.py:

    DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/geo_database"

Run the application:

uvicorn app.main:app --reload

Access the app at http://127.0.0.1:8000/docs.