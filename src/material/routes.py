from fastapi import Depends, HTTPException, APIRouter

from sqlalchemy.orm import Session

from typing import List

from src.storage.dbconfig import SessionLocal

from src.material import schemas
from src.product import handlers as crud


router = APIRouter(
    tags=['Materials'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/materials/product/{product_id}", response_model=schemas.MaterialRead,  tags=["Materials"])
def create_material_for_product(product_id: int, material: schemas.MaterialCreate, db: Session = Depends(get_db)):
    return crud.create_material_for_product(db=db, material=material, product_id=product_id)


@router.get("/materials/", response_model=List[schemas.MaterialRead],  tags=["Materials"])
def read_materials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    materials = crud.get_materials(db, skip=skip, limit=limit)
    return materials

@router.get("/materials/{material_id}", response_model=schemas.MaterialRead,  tags=["Materials"])
def read_material(material_id: int, db: Session = Depends(get_db)):
    db_material = crud.get_material(db, material_id=material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_material


@router.get("/materials/{product_id}", response_model=schemas.MaterialRead,  tags=["Materials"], description="Read all materials of a product")
def read_materials_of_product(product_id: int, db: Session = Depends(get_db)):
    db_material = crud.get_materials_of_product(db, product_id=product_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_material


@router.put("/materials/{material_id}", response_model=schemas.MaterialRead, tags=["Materials"])
def update_material(material_id: int, material_update: schemas.MaterialCreate, db: Session = Depends(get_db)):
    return crud.update_material(db=db, material_id=material_id, material_update=material_update)


@router.patch("/materials/{material_id}", response_model=schemas.MaterialRead, tags=["Materials"])
def partial_update_material(material_id: int, material_update: schemas.MaterialUpdate, db: Session = Depends(get_db)):
    db_material = crud.get_material(db, material_id=material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return crud.update_material(db=db, material_id=material_id, material_update=material_update)


@router.delete("/materials/{material_id}", response_model=schemas.MaterialRead, tags=["Materials"])
def delete_material(material_id: int, db: Session = Depends(get_db)):
    return crud.delete_material(db=db, material_id=material_id)