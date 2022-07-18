
from sqlalchemy import Column, String, Integer, Boolean, Float, Table, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Based
from .base_model import baseModel

class productModel(Based, baseModel):
    __tablename__ = "product"
    
    product_id = Column(String(32), nullable=False)
    product_name = Column(String(64), nullable=False)
    description = Column(String(512))
    short_descripton = Column(String(256))
    regular_price = Column(Float)
    sale_price = Column(Float)
    price = Column(Float)
    image_id = Column(Integer)
    product_url = Column(String(128))
    category_id = Column(Integer, ForeignKey("category.id"))
    
    #many-to-many relationship with supplier
    suppliers = relationship("supplierModel", secondary="product_supplier_table")
    
    #Product variations
    product_reviews = relationship('previewModel', backref='productModel',lazy=True, cascade='all, delete')
    product_variations = relationship('pVariationModel', backref='productModel',lazy=True, cascade='all, delete')
        
    association_table = Table(
        "product_supplier",
        Based.metadata,
        Column("productid", ForeignKey("product.id")),
        Column("suplier_id", ForeignKey("supplier.id"))
    )     
    
    
    