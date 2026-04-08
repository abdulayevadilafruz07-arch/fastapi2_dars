from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from products.schemas import ProductCreate, ProductsOut
from products.crud import create_product

from fastapi import APIRouter
router = APIRouter(prefix='/products')

@router.get("/")
async def products_list():
    return {"message": 'olma, anor'}

@router.get("/test")
async def products_list():
    return {"products": 'test'}



@router.post("/create", response_model=ProductsOut)
async def create(data: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, data)

