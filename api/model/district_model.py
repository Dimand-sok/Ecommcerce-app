
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Based
from .base_model import baseModel

class districtModel(Based, baseModel):
    __tablename__ = "district"
    
    district_name = Column(String(64))
    city = relationship('city', backref='district', lazy=True, cascade="all, delete")
    commune_id = Column(Integer,ForeignKey('commune.id'), nullable=False )