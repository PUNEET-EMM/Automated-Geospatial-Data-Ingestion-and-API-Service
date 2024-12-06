from pydantic import BaseModel, Field, model_validator
from typing import Any, Optional, Dict, List


class Geometry(BaseModel):
    type: str  # Geometry type, e.g., 'Polygon', 'Point', 'LineString'
    coordinates: list  # Coordinates list for the geometry

    @model_validator(mode="after")
    def validate_geometry(cls, values):
        geom_type = values.type
        coords = values.coordinates

        # Validate geometry type
        if geom_type not in ["Polygon", "Point", "LineString"]:
            raise ValueError(f"Unsupported geometry type: {geom_type}")

        # Ensure coordinates are a list
        if not isinstance(coords, list):
            raise ValueError("Coordinates must be a list")

        return values

    class Config:
        orm_mode = True


class GeoDataBase(BaseModel):
    name: str
    geometry: Geometry
    properties: Optional[Dict[str, Any]] = {}
    


class GeoDataCreate(BaseModel):
    name: str
    geometry: Dict[str, Any]  
    properties: Dict[str, Any] = Field(default_factory=dict)

class GeoDataUpdate(BaseModel):
    name: str
    geometry: Dict[str, Any]  
    properties: Dict[str, Any] = Field(default_factory=dict)



class GeoDataGeoJSONResponse(BaseModel):
    id: int
    name: str
    geometry: Geometry
    properties: Dict

    class Config:
        orm_mode = True


class GeoDataFeatureCollection(BaseModel):
    type: str = "FeatureCollection"
    features: List[GeoDataGeoJSONResponse]

    class Config:
        orm_mode = True


def geo_data_to_geojson(geo_data) -> GeoDataGeoJSONResponse:
    return GeoDataGeoJSONResponse(
        id=geo_data.id,
        name=geo_data.name,
        geometry=Geometry(
            type=geo_data.geometry["type"],
            coordinates=geo_data.geometry["coordinates"],
        ),
        properties=geo_data.properties or {},
    )


def geo_data_to_feature_collection(geo_data_list) -> GeoDataFeatureCollection:
    if not geo_data_list:
        raise ValueError("The geo_data_list is empty.")
    features = [geo_data_to_geojson(geo_data) for geo_data in geo_data_list]
    return GeoDataFeatureCollection(features=features)


