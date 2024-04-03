from sqlalchemy import  Column,  Integer, String

from src.storage.dbconfig import Base


class Material(Base):
    __tablename__ = "material"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
   



