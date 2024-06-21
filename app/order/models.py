from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from datetime import date
from sqlalchemy.orm import relationship
import enum

from app.database import Base

# Enum для статуса заказа
class OrderStatus(enum.Enum):
    processing = "в обработке"
    delivered = "доставлен"
    cancelled = "отменен"

# Заказы оформленные
class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String(20), nullable=False)
    delivery_date = Column(DateTime, nullable=False)
    delivery_address = Column(String, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.processing, nullable=False)
    
    # Связь один-ко-многим с OrderProduct
    products = relationship("OrderProduct", back_populates="order", cascade="all, delete-orphan")


    
    
class OrderProduct(Base):
    __tablename__ = 'order_products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('Products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    
    # Связь с Order
    order = relationship("Order", back_populates="products")
    product = relationship("Products")