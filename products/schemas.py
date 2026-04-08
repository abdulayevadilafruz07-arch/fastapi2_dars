from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ProductBase(BaseModel):
    title: str = Field(max_length=15)
    desc:str = Optional
    price:float = Field(lt=1_000_000, gt=1)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductsOut(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True