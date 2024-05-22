from fastapi import APIRouter

from ..crud import ProductsCRUD
from .. import schemas

router = APIRouter(tags=["Products"], prefix='/product')


@router.get('/', response_model=list[schemas.SProducts])
async def get_products():
    return await ProductsCRUD.get_products()

@router.get('/{product_id}/', response_model=schemas.SProducts)
async def get_product(product_id: int):
    return await ProductsCRUD.get_product(product_id=product_id)

@router.post('/')
async def add_product(product_in: schemas.SProducts):
    return await ProductsCRUD.create_product(product_in=product_in)
