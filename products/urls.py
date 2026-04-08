from fastapi import APIRouter

router = APIRouter(prefix='/products')

@router.get("/")
async def products_list():
    return {"message": 'olma,anor'}

@router.get("/test")
async def products_list():
    return {"products": 'test'}
