from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.orm import selectinload


from ..database import async_session
from .models import Order, OrderProduct
from ..lavka.models import Products


class OrdersCRUD:

    @classmethod
    async def get_orders(cls):
        async with async_session() as session:
            stat = select(Order).order_by(Order.id)
            result = await session.execute(stat)
            orders = result.scalars().all()
            return orders

    @classmethod
    async def get_order(cls, order_id: int):
        async with async_session() as session:
            stat = select(Order).where(Order.id == order_id).options(
                selectinload(Order.products).selectinload(OrderProduct.product)
            )
            result = await session.execute(stat)
            order = result.scalars().first()
            return order

    @classmethod
    async def create_order(cls, order_data):
        async with async_session() as session:
            order = Order(**order_data)
            session.add(order)
            await session.commit()
            await session.refresh(order)
            return order

    @classmethod
    async def update_order(cls, order_id: int, update_data):
        async with async_session() as session:
            order = await session.get(Order, order_id)
            if not order:
                return None
            for key, value in update_data.items():
                setattr(order, key, value)
            await session.commit()
            await session.refresh(order)
            return order

    @classmethod
    async def delete_order(cls, order_id: int):
        async with async_session() as session:
            order = await session.get(Order, order_id)
            if not order:
                return None
            await session.delete(order)
            await session.commit()
            return order


class OrderProductsCRUD:

    @classmethod
    async def get_order_products(cls):
        async with async_session() as session:
            stat = select(OrderProduct).order_by(OrderProduct.id)
            result = await session.execute(stat)
            order_products = result.scalars().all()
            return order_products

    @classmethod
    async def get_order_product(cls, order_product_id: int):
        async with async_session() as session:
            return await session.get(OrderProduct, order_product_id)

    @classmethod
    async def create_order_product(cls, order_product_data):
        async with async_session() as session:
            order_product = OrderProduct(**order_product_data)
            session.add(order_product)
            await session.commit()
            await session.refresh(order_product)
            return order_product

    @classmethod
    async def update_order_product(cls, order_product_id: int, update_data):
        async with async_session() as session:
            order_product = await session.get(OrderProduct, order_product_id)
            if not order_product:
                return None
            for key, value in update_data.items():
                setattr(order_product, key, value)
            await session.commit()
            await session.refresh(order_product)
            return order_product

    @classmethod
    async def delete_order_product(cls, order_product_id: int):
        async with async_session() as session:
            order_product = await session.get(OrderProduct, order_product_id)
            if not order_product:
                return None
            await session.delete(order_product)
            await session.commit()
            return order_product
