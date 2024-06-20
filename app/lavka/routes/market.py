from fastapi import APIRouter

from ..crud import MarketsCRUD
from .. import schemas

router = APIRouter(tags=["Markets"], prefix='/market')


@router.get('/', response_model=list[schemas.SMarkets])
async def get_markets():
    return await MarketsCRUD.get_markets()

@router.get('/{market_id}/', response_model=schemas.SMarkets)
async def get_market(market_id: int):
    return await MarketsCRUD.get_market(market_id=market_id)

@router.post('/')
async def add_market(market_in: schemas.SMarkets):
    return await MarketsCRUD.create_market(market_in=market_in)
