from sqlalchemy import Column,String, Integer, Boolean

from app.database import Based
from .base_model import baseModel


class userModel(Based,baseModel):
    __tablename__ = "user"
    
    user_id = Column(String(32), nullable=False)
    __user_name = Column(String(64), nullable=False)
    __email_address = Column(String(128), nullable=False)
    __password = Column(String(32), nullable=False)
    first_name = Column(String(32))
    last_name = Column(String(32))
    gender = Column(String(16))
    photo = Column(String(128))
    address = Column(String(64))
    country = Column(String(64))
    city = Column(String(64))
    district = Column(String(64))
    commune = Column(String(64))
    phone_number = Column(Integer(13))
    active = Column(Boolean)
    
    