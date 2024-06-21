from fastapi import FastAPI

# Lavka
from app.lavka.routes.market import router as market_router
from app.lavka.routes.product import router as product_router
from app.lavka.routes.lavka import router as lavka_router

# Order
from app.order.routes.order import router as order_router



app = FastAPI()

app.include_router(market_router)
app.include_router(product_router)
app.include_router(lavka_router)

app.include_router(order_router)




