
from sqlalchemy import Column, String, Integer
from app.database import Based

class districtModel(Based):
    __tablename__ = "district"
    
    district_name = Column(String(64))
    city_id = Column(Integer(16))