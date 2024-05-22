from fastapi import APIRouter

from ..crud import LavkaCRUD
from .. import schemas

router = APIRouter(tags=["Lavka"], prefix='/lavka')


@router.get('/all', response_model=list[schemas.SLavka])
async def get_all_products():
    return await LavkaCRUD.get_all_products_from_lavkas()


@router.get('/{market_id}/', response_model=list[schemas.SLavka])
async def get_products(market_id: int):
    return await LavkaCRUD.get_products_from_lavka(market_id=market_id)

@router.get('/')
async def get_product(market_id: int, product_id:int):
    product = await LavkaCRUD.get_product_from_lavka(product_id=product_id, market_id=market_id)
    return product



@router.post('/')
async def add_lavka_product(lavka_in: schemas.SLavka):
    return await LavkaCRUD.add_product_to_lavka(lavka_in=lavka_in)
