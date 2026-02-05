from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    base_price = Column(Float, nullable=False)
    sku = Column(String, unique=True)
    stock = Column(Integer, default=0, nullable=False)
