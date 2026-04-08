from sqlalchemy.orm import Session
from products.models import Products
from products.schemas import ProductCreate, ProductUpdate

def create_product(db:Session, data: ProductCreate):
    product = Products(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
