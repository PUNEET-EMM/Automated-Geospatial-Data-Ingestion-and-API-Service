from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from geoalchemy2.types import Geography
from app.database import Base
from sqlalchemy.dialects.postgresql import JSONB

class GeoData(Base):
    __tablename__ = "geo_data"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    geometry = Column(Geometry("POLYGON", srid=4326))  # Geometry column with SRID 4326 for polygons
    properties = Column(JSONB)  # Store properties as JSONB for efficient querying

    def __repr__(self):
        return f"<GeoData(name={self.name}, geometry={self.geometry}, properties={self.properties})>"


