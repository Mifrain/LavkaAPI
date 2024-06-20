from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select

from app.database import async_session
from .models import *
from .schemas import *


class MarketsCRUD:

    @classmethod
    async def get_markets(cls):
        async with async_session() as session:
            stat = select(Markets).order_by(Markets.id)
            result: Result = await session.execute(stat)
            markets = result.scalars().all()
            return markets

    @classmethod
    async def get_market(cls, market_id: int):
        async with async_session() as session:
            return await session.get(Markets, market_id)

    @classmethod
    async def create_market(cls, market_in: SMarkets):
        async with async_session() as session:
            market = Markets(**market_in.model_dump())  #model_dump - преобразовывает в словарь
            session.add(market)
            await session.commit()
            # return market

    # @classmethod
    # async def delete_market(cls, market_id: int):
    #     async with async_session() as session:
    #         market = select(Markets).filter_by(id=market_id)
    #         session.delete(market)
    #         await session.commit()
    
class ProductsCRUD:
    
    @classmethod
    async def get_products(cls):
        async with async_session() as session:
            stat = select(Products).order_by(Products.id)
            result: Result = await session.execute(stat)
            products = result.scalars().all()
            return products

    @classmethod
    async def get_product(cls, product_id: int):
        async with async_session() as session:
            return await session.get(Products, product_id)

    @classmethod
    async def create_product(cls, product_in: SProducts):
        async with async_session() as session:
            product = Products(**product_in.model_dump())  #model_dump - преобразовывает в словарь
            session.add(product)
            await session.commit()

#



class LavkaCRUD:
    
    # Добавить
    @classmethod
    async def add_product_to_lavka(cls, lavka_in: SLavka):
        async with async_session() as session:
            product = Lavka(**lavka_in.model_dump())  #model_dump - преобразовывает в словарь
            session.add(product)
            await session.commit()
            await session.refresh(product)
            # product.update_expired_date()
            
    
    # Все продукты во всех магазинах        
    @classmethod
    async def get_all_products_from_lavkas(cls):
        async with async_session() as session:
            stat = select(Lavka).order_by(Lavka.id)
            result: Result = await session.execute(stat)
            products = result.scalars().all()
            return products
    
    # Все продукты в 1 магазине
    @classmethod
    async def get_products_from_lavka(cls, market_id: int):
        async with async_session() as session:
            stat = select(Lavka).filter_by(market_id=market_id).order_by(Lavka.id)
            result: Result = await session.execute(stat)
            products = result.scalars().all()
            return products

    # Продукт в 1 магазине
    @classmethod
    async def get_product_from_lavka(cls, product_id: int, market_id: int):
        async with async_session() as session:
            stat = select(Lavka).filter_by(market_id=market_id, product_id=product_id)
            result: Result = await session.execute(stat)
            product = result.scalar_one_or_none()
            return product
    
    # Обновить
    # @classmethod
    # async def update_product_expired_date(cls, lavka_prod: Lavka):
    #     async with async_session() as session:
    #         print(lavka_prod.product)
    #         # lavka_prod.expired_date = lavka_prod.arrived_date + timedelta(days=lavka_prod.product.expiration_days)
    #         # await session.commit()    
            
    
