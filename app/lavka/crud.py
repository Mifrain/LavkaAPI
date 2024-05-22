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
    
