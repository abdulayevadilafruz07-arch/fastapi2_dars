from sqlalchemy.orm import Session
from products.models import Products
from products.schemas import ProductCreate, ProductUpdate

def create_product(db:Session, data: ProductCreate):
    product = Products(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db:Session):
    return db.query(Products).all() #Products.objects == db.query(Products).get(Products_id==pk).first

def get_product(db:Session, product_id: int):
    return db.query(Products).filter(Products.id == product_id).first()
