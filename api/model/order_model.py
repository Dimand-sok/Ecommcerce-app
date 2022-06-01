
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from app.database import Based
from .base_model import baseModel

class orderModel(Based, baseModel):
    __tablename__ = "order"
    
    order_date = Column(DateTime,default=func.now())
    require_date = Column(DateTime,default=func.now())
    
    #one-to-many
    order_details = relationship("order_detailModel", backref="orderModel", lazy=False, cascade="all, delete")
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    
    shipvia = Column(String(64))
    ship_address = Column(String(128))
    ship_ciy = Column(String(128))
    ship_district = Column (String(128))
    ship_commune = Column (String(128))