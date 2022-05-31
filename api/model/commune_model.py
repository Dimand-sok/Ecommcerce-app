
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from api.model.base_model import baseModel

from app.database import Based

class communeModel(Based, baseModel):
    __tablename__ = "commune"
    
    commune_name = Column(String(64))
    district = relationship('district', backref='district.id', lazy=True, cascade="all, delete")