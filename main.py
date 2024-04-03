from fastapi import FastAPI

#routes
from src.product.routes import router as product_router
from src.material.routes import router as material_router

app = FastAPI()
app.include_router(product_router)
app.include_router(material_router)
