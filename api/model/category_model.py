
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

from app.database import Based
from .base_model import baseModel

class categoryModel(Based, baseModel):
    __tablename__ = "category"
    
    category_name = Column(String(128))
    category_desc = Column(String(512))
    
    products = relationship("productModel", backref="categoryModel", lazy=False, cascade=("all, delete"))