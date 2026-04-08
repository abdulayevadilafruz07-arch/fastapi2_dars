from fastapi import FastAPI
from products.urls import router as product_router
from users.urls import router as user_router
from database import Base, engine
import products.models


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router=product_router)
app.include_router(router=user_router)


@app.get("/")
async def index():
    return {"message": "World"}

@app.get('/test/')
async def test():
    return {"message": "test"}

