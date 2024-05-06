from fastapi import APIRouter

zakaz_router = APIRouter(prefix="/zakaz")

@zakaz_router.get("/")
async def user_profile():
    return {"zakaz":"Bu zakazlar sahifasi"}
