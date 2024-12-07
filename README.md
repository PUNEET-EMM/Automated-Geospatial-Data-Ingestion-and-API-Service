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
  * Python 3.10 or higher
  * PostgreSQL with PostGIS enabled

### Steps to setup
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

Here’s the updated and more descriptive API endpoints table to match the revised paths and naming conventions:

## API Endpoints

| **Method** | **Endpoint**                          | **Description**                           |
|------------|---------------------------------------|-------------------------------------------|
| `GET`      | `/api/v1/geo_data/view/{geo_data_id}`  | Retrieve geo-data by ID.                  |
| `PUT`      | `/api/v1/geo_data/update/{geo_data_id}` | Update a geo-data entry by ID.            |
| `DELETE`   | `/api/v1/geo_data/delete/{geo_data_id}` | Delete a geo-data entry by ID.            |
| `PATCH`    | `/api/v1/geo_data/patch/{geo_data_id}` | Partially update a geo-data entry by ID.  |
| `POST`     | `/api/v1/geo_data/create`             | Create a new geo-data entry.              |
| `GET`      | `/api/v1/geo_data/list`               | Retrieve a list of all geo-data entries.  |


## Schema for Creating Geo-Data (`POST /api/v1/geo_data/create`)

### Request Body:

```json
{
  "name": "string",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -73.99756,
          40.73083
        ],
        [
          -73.996,
          40.73177
        ],
        [
          -73.996,
          40.73288
        ],
        [
          -73.99756,
          40.73382
        ],
        [
          -73.99756,
          40.73083
        ]
      ]
    ]
  },
  "properties": {
    "key": "value"
  }
}
```


Swagger UI provides an interactive way to test these endpoints.




 



   