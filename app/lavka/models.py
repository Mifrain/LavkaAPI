from sqlalchemy import Column, Integer, String, ForeignKey, Date, Compiled
from datetime import date, timedelta

from app.database import Base, async_session


class Markets(Base):
    __tablename__ = "Markets"
    
    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    
    
    def __init__(self, address, phone):
        self.address, self.phone = address, phone
    
    
    # async def change_address(self, new_address):
    #     async with async_session as session:
    #         self.address = new_address
    #         session.commit()
    
    

class Products(Base):
    __tablename__ = "Products"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    expiration_days = Column(Integer)   #Срок годности продукта
    
    
class Lavka(Base):
    __tablename__ = "Lavka"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("Products.id"))
    market_id = Column(Integer, ForeignKey("Markets.id"))
    product_name = Column(String)
    amount = Column(Integer)
    arrived_date = Column(Date, default=date.today())
    expired_date = Column(Date, default=date.today())
    
    # Украсть Product name и expiration_days
    def __init__(self):
        pass
    
    