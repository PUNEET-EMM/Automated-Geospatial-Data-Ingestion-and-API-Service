from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from shapely.geometry import mapping
from geoalchemy2.shape import to_shape  # Convert from PostGIS geometry to Shapely
from app import crud
from app.schemas import GeoDataCreate, GeoDataGeoJSONResponse, GeoDataUpdate
from app.database import get_db  # Dependency for database session
from geoalchemy2.shape import to_shape
from shapely.geometry import mapping

router = APIRouter()





def geo_data_to_dict(geo_data):
    """
    Convert a GeoData SQLAlchemy model to a dictionary compatible with GeoJSON.
    """
    geometry = to_shape(geo_data.geometry) if geo_data.geometry else None
    geojson = mapping(geometry) if geometry else None
    return {
        "id": geo_data.id,
        "geometry": geojson,
        "name": geo_data.name,
        "properties": geo_data.properties or {},
    }



# Endpoint: Get GeoData by ID
@router.get("/geo_data/{geo_data_id}", response_model=GeoDataGeoJSONResponse)
def get_geo_data_by_id(geo_data_id: int, db: Session = Depends(get_db)):
    geo_data = crud.get_geo_data_by_id(db, geo_data_id)
    if not geo_data:
        raise HTTPException(status_code=404, detail="GeoData not found")
    return geo_data_to_dict(geo_data)


# Endpoint: Create new GeoData
@router.post("/geo_data", response_model=GeoDataGeoJSONResponse)
def create_geo_data(geo_data: GeoDataCreate, db: Session = Depends(get_db)):
    try:
        created_geo_data = crud.create_geo_data(db, geo_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return geo_data_to_dict(created_geo_data)



# Endpoint: Get all GeoData
@router.get("/geo_data", response_model=list[GeoDataGeoJSONResponse])
def get_all_geo_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    geo_data_list = crud.get_all_geo_data(db, skip, limit)
    return [geo_data_to_dict(geo) for geo in geo_data_list]


@router.put("/geo_data/{geo_data_id}", response_model=GeoDataGeoJSONResponse)
def update_geo_data(geo_data_id: int, geo_data: GeoDataUpdate, db: Session = Depends(get_db)):
    updated_geo_data = crud.update_geo_data(db, geo_data_id, geo_data)
    if not updated_geo_data:
        raise HTTPException(status_code=404, detail="GeoData not found")
    return geo_data_to_dict(updated_geo_data)



# Endpoint: Delete GeoData by ID
@router.delete("/geo_data/{geo_data_id}", response_model=GeoDataGeoJSONResponse)
def delete_geo_data(geo_data_id: int, db: Session = Depends(get_db)):
    deleted_geo_data = crud.delete_geo_data(db, geo_data_id)
    if not deleted_geo_data:
        raise HTTPException(status_code=404, detail="GeoData not found")
    return geo_data_to_dict(deleted_geo_data)


@router.patch("/geo_data/{geo_data_id}", response_model=GeoDataGeoJSONResponse)
def partial_update_geo_data(geo_data_id: int, geo_data: GeoDataUpdate, db: Session = Depends(get_db)):
    updated_geo_data = crud.partial_update_geo_data(db, geo_data_id, geo_data)  # geo_data is the Pydantic model
    if not updated_geo_data:
        raise HTTPException(status_code=404, detail="GeoData not found")
    return geo_data_to_dict(updated_geo_data)