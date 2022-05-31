
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from api.model.base_model import baseModel

from app.database import Based

class cityModel(Based, baseModel):
    __tablename__ = "city"
    
    city_name = Column(String(64))
    country_id = Column(Integer, ForeignKey('country.id'), nullable=False)
    districts = relationship('districtModel',backref='cityModel', lazy=True, cascade="all, delete")