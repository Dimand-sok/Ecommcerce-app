
from sqlalchemy import Column, String, Integer, ForeignKey

from app.database import Based
from .base_model import baseModel

class previewModel(Based, baseModel):
    __tablename__ = "product_review"
    
    product_id = Column(Integer, ForeignKey('product.id'),nullable = False)
    review_text = Column(String(512))
    review_star = Column(String(32))
    review_dt = Column(String(64))