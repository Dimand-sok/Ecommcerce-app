
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from api.model.base_model import baseModel

from app.database import Based

class cityModel(Based, baseModel):
    __tablename__ = "city"
    
    city_name = Column(String(64))
    country = relationship('country', backref='city', lazy=True, cascade="all, delete")
    district_id = Column(Integer, ForeignKey('district.id'), nullable=False)