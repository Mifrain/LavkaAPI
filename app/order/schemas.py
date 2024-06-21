from pydantic import BaseModel
from datetime import datetime
from typing import List

class OrderProductCreate(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderCreate(BaseModel):
    phone_number: str
    delivery_date: datetime
    delivery_address: str
    total_price: float
    products: List[OrderProductCreate]

class OrderProductRead(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderRead(BaseModel):
    id: int
    phone_number: str
    delivery_date: datetime
    delivery_address: str
    total_price: float
    status: str
    products: List[OrderProductRead]

    class Config:
        orm_mode = True
