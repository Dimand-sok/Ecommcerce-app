
from sqlalchemy import Column, String
from app.database import Based

class countryModel(Based):
    __tablename__ = "country"
    
    country_name = Column(String(64))