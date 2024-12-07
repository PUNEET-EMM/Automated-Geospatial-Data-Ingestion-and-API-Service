import requests
from sqlalchemy.orm import Session
from shapely.geometry import shape, Polygon
from geoalchemy2 import WKBElement
from app.models import GeoData
from app.database import SessionLocal
from app.config import GEOJSON_URL

# Function to fetch and load GeoJSON data into the database
def fetch_and_load_geojson(db: Session, url: str):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data from {url}")
        return

    geojson_data = response.json()
    
    for feature in geojson_data["features"]:
        # Extract the name (or set a default if it's missing)
        name = feature["properties"].get("name", "Unknown")
        
        # Extract the geometry and convert it to a Shapely object
        geometry_type = feature["geometry"]["type"]
        coordinates = feature["geometry"]["coordinates"]
        
        if geometry_type == "Polygon":
            geometry = Polygon(coordinates[0])  # The first element is the array of coordinates for the polygon
        else:
            print(f"Unsupported geometry type: {geometry_type}")
            continue
        
        # Convert Shapely geometry to WKB (Well-Known Binary) format
        wkb_geometry = geometry.wkb  # This will give us a binary representation of the geometry

        # Create a GeoData instance and add it to the database
        db_geodata = GeoData(
            name=name,
            geometry=WKBElement(wkb_geometry),  # Convert the WKB to GeoAlchemy2's WKBElement
            properties=feature["properties"]  # Store properties as JSON
        )
        db.add(db_geodata)
    
    # Commit the transaction
    db.commit()
    print("Data ingestion completed.")


db = SessionLocal()

fetch_and_load_geojson(db, GEOJSON_URL)

