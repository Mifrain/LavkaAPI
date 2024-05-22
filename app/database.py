from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import settings

engine = create_async_engine(settings.DB_URI)

#Async maker
async_session = async_sessionmaker(engine, expire_on_commit=False)

# For migrations
class Base(DeclarativeBase):
    pass