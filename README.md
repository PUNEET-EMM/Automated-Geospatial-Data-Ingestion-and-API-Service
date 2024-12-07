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

1. **Clone  the repositry**
```bash
git clone  https://github.com/PUNEET-EMM/Automated-Geospatial-Data-Ingestion-and-API-Service.git
cd <repository-folder>
```
 **Install required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```


2. **Configure the database:**

   Install PostgreSQL and enable the PostGIS extension:

   - Install PostgreSQL on your machine (refer to [PostgreSQL installation](https://www.postgresql.org/download/)).
   - Install PostGIS extension for PostgreSQL (refer to [PostGIS installation](https://postgis.net/install/)).

3. **Create a database with PostGIS:**

```bash
CREATE DATABASE geo_database;
\c geo_database;
CREATE EXTENSION postgis;
```

4. **Update the `DATABASE_URL` in `app/config.py`:**

   In the `config.py` file within the `app` folder, update the `DATABASE_URL` to match your PostgreSQL setup:

```python
DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/geo_database"
```

5. **Run the application:**

```bash
uvicorn app.main:app --reload
```

   This will start the FastAPI server locally.

6. **Access the app:**

   Open your browser and visit the following URL to interact with the API documentation:

   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


### Docker Setup
==========================

Prerequisites
-------------
- Docker and Docker Compose installed.

Steps
-----
1. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

2. Access the application:
    - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

API Endpoints
-------------
| Method | Endpoint                        | Description                     |
|--------|---------------------------------|---------------------------------|
| GET    | /geo_data/{geo_data_id}         | Get geo-data by ID              |
| PUT    | /geo_data/{geo_data_id}         | Update geo-data by ID          |
| DELETE | /geo_data/{geo_data_id}         | Delete geo-data by ID          |
| PATCH  | /geo_data/{geo_data_id}         | Partially update geo-data      |
| POST   | /geo_data                       | Create geo-data                |
| GET    | /geo_data                       | Get all geo-data               |

Swagger UI provides an interactive way to test these endpoints.

Configuration
-------------
1. **Database URL**: Update the `DATABASE_URL` in `app/config.py`:
    ```python
    DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/geo_database"
    ```


 



   