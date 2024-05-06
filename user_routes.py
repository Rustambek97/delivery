from fastapi import APIRouter

user_router = APIRouter(prefix="/user")

@user_router.get("/")
async def user_profile():
    return {"user":"Bu userning profile sahifasi"}
