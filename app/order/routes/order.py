from fastapi import APIRouter, HTTPException

from ..crud import OrdersCRUD, OrderProductsCRUD
from ...lavka.crud import ProductsCRUD
from ..schemas import OrderCreate, OrderProductCreate, OrderRead

router = APIRouter(tags=["Orders"], prefix='/orders')

@router.post('/')
async def create_order(order_in: OrderCreate):
    # Convert timezone-aware datetime to naive datetime
    delivery_date_naive = order_in.delivery_date.replace(tzinfo=None)
    order_data = {
        "phone_number": order_in.phone_number,
        "delivery_date": delivery_date_naive,
        "delivery_address": order_in.delivery_address,
        "total_price": order_in.total_price,
        "status": "processing"
    }

    # Создание заказа
    new_order = await OrdersCRUD.create_order(order_data)
    if not new_order:
        raise HTTPException(status_code=400, detail="Failed to create order")

    # Добавление продуктов к заказу
    for product in order_in.products:
        # Проверка, что продукт существует
        existing_product = await ProductsCRUD.get_product(product.product_id)
        if not existing_product:
            raise HTTPException(status_code=404, detail=f"Product with ID {product.product_id} not found")

        order_product_data = {
            "order_id": new_order.id,
            "product_id": product.product_id,
            "quantity": product.quantity,
            "price": product.price
        }
        order_product = await OrderProductsCRUD.create_order_product(order_product_data)
        if not order_product:
            raise HTTPException(status_code=400, detail="Failed to add products to order")

    return new_order

@router.get('/{order_id}', response_model=OrderRead)
async def get_order(order_id: int):
    order = await OrdersCRUD.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order

@router.put('/{order_id}/cancel')
async def cancel_order(order_id: int):
    order = await OrdersCRUD.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    updated_order = await OrdersCRUD.update_order(order_id, {"status": "cancelled"})
    if not updated_order:
        raise HTTPException(status_code=400, detail="Failed to cancel order")

    return updated_order
