from sqlalchemy import  Column,  Integer, String

from src.storage.dbconfig import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    code = Column(String, index=True)
   



