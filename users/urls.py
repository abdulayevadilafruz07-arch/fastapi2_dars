from fastapi import APIRouter

router = APIRouter(prefix='/auth')

@router.get('/')
async def sign_up():
    return {"message":"Ro'yxatdan o'tish💻 "}


@router.get('/login')
async def login():
    return {"message":" Login📲 "}


