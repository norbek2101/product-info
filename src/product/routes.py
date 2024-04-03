from fastapi import Depends, HTTPException, APIRouter

from sqlalchemy.orm import Session

from typing import List

from src.storage.dbconfig import SessionLocal

from src.product import schemas
from src.product import handlers as crud


router = APIRouter(
    tags=['Products'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/products/", response_model=schemas.ProductRead,  tags=["Products"])
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@router.get("/products/", response_model=List[schemas.ProductRead],  tags=["Products"])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@router.get("/products/{product_id}", response_model=schemas.ProductRead,  tags=["Products"])
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/products/{product_id}", response_model=schemas.ProductRead,  tags=["Products"])
def update_product(product_id: int, product_update: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.update_product(db=db, product_id=product_id, product_update=product_update)


@router.patch("/products/{product_id}", response_model=schemas.ProductRead,  tags=["Products"])
def partial_update_product(product_id: int, product_update: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db=db, product_id=product_id, product_update=product_update)


@router.delete("/products/{product_id}", response_model=schemas.ProductRead,  tags=["Products"])
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db=db, product_id=product_id)
