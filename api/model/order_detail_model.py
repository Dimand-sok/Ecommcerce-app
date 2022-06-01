
from sqlalchemy import Column, Integer, Float, ForeignKey
# from sqlalchemy.orm import relationship

from app.database import Based
from .base_model import baseModel

class order_detailModel(Based, baseModel):
    __tablename__ = "orderdetail"
    
    unit_price = Column(Float)
    qty = Column(Float)
    discount = Column(Integer)
    order_id = Column(Integer, ForeignKey("order.id"), nullable=False)