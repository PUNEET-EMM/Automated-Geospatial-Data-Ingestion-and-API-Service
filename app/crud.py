# from turtle import shape
from sqlalchemy.orm import Session
from geoalchemy2 import WKBElement, WKTElement
from app.models import GeoData
from app.schemas import GeoDataCreate, GeoDataUpdate
from sqlalchemy.exc import IntegrityError
from typing import Optional
from shapely.geometry import shape



def get_geo_data_by_id(db: Session, geo_data_id: int):
    return db.query(GeoData).filter(GeoData.id == geo_data_id).first()


def get_all_geo_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(GeoData).offset(skip).limit(limit).all()


def delete_geo_data(db: Session, geo_data_id: int):
    db_geo_data = db.query(GeoData).filter(GeoData.id == geo_data_id).first()
    if not db_geo_data:
        return None
    db.delete(db_geo_data)
    db.commit()
    return db_geo_data


def create_geo_data(db: Session, geo_data: GeoDataCreate):
    try:
        # Convert GeoJSON to Shapely geometry
        shapely_geometry = shape(geo_data.geometry)  # GeoJSON to Shapely object
    except Exception as e:
        raise ValueError(f"Invalid geometry format: {e}")

    # Convert Shapely geometry to WKB
    wkb_geometry = shapely_geometry.wkb

    # Create GeoData instance
    new_geo_data = GeoData(
        name=geo_data.name,
        geometry=WKBElement(wkb_geometry, srid=4326),  # WKBElement with SRID
        properties=geo_data.properties or {}
    )

    db.add(new_geo_data)
    db.commit()
    db.refresh(new_geo_data)

    return new_geo_data


from shapely.geometry import shape
from geoalchemy2 import WKBElement

def update_geo_data(db: Session, geo_data_id: int, geo_data_update: GeoDataUpdate):
    # Fetch the existing GeoData entry from the database
    existing_geo_data = db.query(GeoData).filter(GeoData.id == geo_data_id).first()

    if not existing_geo_data:
        return None  # GeoData not found

    try:
        # Convert updated GeoJSON to Shapely geometry
        shapely_geometry = shape(geo_data_update.geometry)  # GeoJSON to Shapely object
    except Exception as e:
        raise ValueError(f"Invalid geometry format: {e}")

    # Convert Shapely geometry to WKB
    wkb_geometry = shapely_geometry.wkb

    # Update the fields in the existing GeoData
    existing_geo_data.name = geo_data_update.name
    existing_geo_data.geometry = WKBElement(wkb_geometry, srid=4326)  # Set the WKB with SRID
    existing_geo_data.properties = geo_data_update.properties or {}

    # Commit the changes to the database
    db.commit()

    # Refresh the instance to reflect the updated data
    db.refresh(existing_geo_data)

    return existing_geo_data


def partial_update_geo_data(db: Session, geo_data_id: int, geo_data_update: GeoDataUpdate):
    # Fetch the existing GeoData entry from the database
    existing_geo_data = db.query(GeoData).filter(GeoData.id == geo_data_id).first()

    if not existing_geo_data:
        return None  # GeoData not found

    try:
        # Convert updated GeoJSON to Shapely geometry (only if the geometry is provided)
        if geo_data_update.geometry:
            shapely_geometry = shape(geo_data_update.geometry)  # GeoJSON to Shapely object
            # Convert Shapely geometry to WKB
            wkb_geometry = shapely_geometry.wkb
            existing_geo_data.geometry = WKBElement(wkb_geometry, srid=4326)  # Set the WKB with SRID
    except Exception as e:
        raise ValueError(f"Invalid geometry format: {e}")

    # Update the fields in the existing GeoData (only if they are provided)
    if geo_data_update.name is not None:
        existing_geo_data.name = geo_data_update.name
    if geo_data_update.properties is not None:
        existing_geo_data.properties = geo_data_update.properties

    # Commit the changes to the database
    db.commit()

    # Refresh the instance to reflect the updated data
    db.refresh(existing_geo_data)

    return existing_geo_data  # Returning the updated object



