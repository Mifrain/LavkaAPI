
from pydantic import BaseModel, ConfigDict


class SMarkets(BaseModel):    
    address: str
    phone: str
    
    # Для ORM
    model_config = ConfigDict(from_attributes=True)
    

class SProducts(BaseModel):
    name: str
    type: str
    expiration_days: int   #Срок годности продукта
    
    # Для ORM
    model_config = ConfigDict(from_attributes=True) 


class SLavka(BaseModel):
    product_id: int
    market_id: int
    amount: int
