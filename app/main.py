from fastapi import FastAPI
from app.routers import geo
from app.database import engine, Base  # Import Base and engine
from app.models import GeoData  # Ensure the model is imported
from contextlib import contextmanager

# Initialize the FastAPI application
app = FastAPI(
    title="Geospatial Data API",
    description="An API for managing geospatial data using FastAPI and PostGIS.",
    version="1.0.0"
)
@app.on_event("startup")
async def on_startup():
    # Synchronously create tables in the database
    Base.metadata.create_all(bind=engine)



# Include the geospatial routes
app.include_router(geo.router,prefix="/api/v1")
