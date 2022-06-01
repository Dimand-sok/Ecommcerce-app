
from sqlalchemy import Column, Integer, DateTime, func
# from datetime import datetime


class baseModel():
    id = Column(Integer,primary_key=True,autoincrement=True)
    created_date = Column(DateTime,default=func.now())
    updated_date = Column(DateTime,onupdate=func.now())


    