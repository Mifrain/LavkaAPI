from fastapi import FastAPI

from app.lavka.routes.market import router as market_router
from app.lavka.routes.product import router as product_router


app = FastAPI()

app.include_router(market_router)
app.include_router(product_router)


