
from sqlalchemy import Column, String, Integer

from app.database import Based
from .base_model import baseModel



class supplierModel(Based, baseModel):
    __tablename__ = "supplier"
    
    supplier_name = Column(String(128), nullable= False)
    supplier_desc = Column(String(512))
    supplier_contact = Column(String(64))
    supplier_phone = Column(Integer)
    supplier_address = Column(String(512))
    supplier_city = Column(String(64))
    supplier_district = Column(String(64))
    supplier_commune = Column(String(64))
