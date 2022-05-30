
from sqlalchemy import Column, String, Integer
from app.database import Based

class cityModel(Based):
    __tablename__ = "city"
    
    city_name = Column(String(64))
    country_id = Column(Integer(16))