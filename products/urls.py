from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from products.schemas import ProductCreate, ProductsOut
from products.crud import create_product, get_products, get_product

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


@router.get("/products", response_model=list[ProductsOut])
async def read_all(db: Session = Depends(get_db)):
    return get_products(db)


@router.get("/products/{product_id}", response_model=ProductsOut)
def read_one(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

