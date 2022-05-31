
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Based
from .base_model import baseModel

class countryModel(Based, baseModel):
    __tablename__ = "country"
    
    country_name = Column(String(64))
    city = Column(Integer, ForeignKey('city.id'), nullable=False)