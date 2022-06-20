
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Based
from .base_model import baseModel

class pVariationModel(Based, baseModel):
    __tablename__ = "product_variation"
    
    product_size = Column(Integer)
    product_color = Column(String(64))
    product_image = Column(String(512))
    product_id = Column(Integer, ForeignKey('product.id'),nullable = False)