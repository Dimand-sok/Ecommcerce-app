
from sqlalchemy import Column, String, Integer
from app.database import Based

class communeModel(Based):
    __tablename__ = "commune"
    
    commune_name = Column(String(64))
    district_id = Column(Integer(16))