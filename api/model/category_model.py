
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

from app.database import Based
from .base_model import baseModel

class CategoryModel(Based, baseModel):
    __tablename__ = "category"
    
    category_name = Column(String(128))
    category_desc = Column(String(512))
    
    # products = relationship("productModel", backref="categoryModel", lazy=False, cascade=("all, delete"))
    
    
    @property
    def categoryName(self):
        return self.category_name

    @categoryName.setter
    def categoryName(self, category_name):
        pass

    def set_categoryName(self, category_name):
        self.categoryName = category_name
     
       
        
    def __init__(self, schema):
        for key, value in schema.items():
            if hasattr(self, key):
                if getattr(self, key) != value:
                    setattr(self, key, value)    