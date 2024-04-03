from sqlalchemy import Column, Integer, Float, DECIMAL,  ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class ProductMaterial(Base):
    __tablename__ = 'product_materials'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    material_id = Column(Integer, ForeignKey('materials.id'))
    quantity = Column(Float)

    product = relationship("Product")
    material = relationship("Material")



class Warehouse(Base):
    __tablename__ = 'warehouses'
    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey('materials.id'))
    reminder = Column(Float)
    price = Column(DECIMAL)

    product = relationship("Product")
   



