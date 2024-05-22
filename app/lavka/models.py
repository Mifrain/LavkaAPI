from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from datetime import date

from app.database import Base, async_session

# Магазины
class Markets(Base):
    __tablename__ = "Markets"
    
    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    
    lavkas = relationship("Lavka", back_populates="markets")
    
    def __init__(self, address, phone):
        self.address = address
        self.phone = phone
    
# Все продукты
class Products(Base):
    __tablename__ = "Products"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    expiration_days = Column(Integer)   # Срок годности продукта
    
    lavkas = relationship("Lavka", back_populates="products")

# Продукты в магазине (Products x Markets)
class Lavka(Base):
    __tablename__ = "Lavka"
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("Products.id"))
    market_id = Column(Integer, ForeignKey("Markets.id"))
    amount = Column(Integer)
    arrived_date = Column(Date, default=date.today)
    expired_date = Column(Date, default=date.today)
    
    products = relationship("Products", back_populates="lavkas")
    markets = relationship("Markets", back_populates="lavkas")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
