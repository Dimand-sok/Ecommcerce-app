from sqlalchemy import Column, String, Integer, Boolean, Float

from app.database import Based

class productModel(Based):
    __tablename__ = "product"
    
    product_id = Column(String(32), nullable=False)
    product_name = Column(String(64), nullable=False)
    description = Column(String(512))
    short_descripton = Column(String(256))
    regular_price = Column(Float(16))
    sale_price = Column(Float(16))
    price = Column(Float(16))
    