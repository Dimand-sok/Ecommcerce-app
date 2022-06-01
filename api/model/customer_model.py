
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.database import Based
from .base_model import baseModel

class customerModel(Based, baseModel):
    __tablename__ = "customer"
       
    customer_name = Column(String(64))
    customer_phone = Column(Integer(13))
    
    #one-to-many
    orders = relationship("orderModel", backref="customerModel", lazy=False, cascade="all, delete")
        
    customer_address = Column(String(128))
    customer_ciy = Column(String(128))
    customer_district = Column (String(128))
    customer_commune = Column (String(128))