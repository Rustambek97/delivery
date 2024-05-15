from fastapi import APIRouter, status

from models import User
from schemas import SignUpModel
from database import session, engine
from fastapi.exceptions import HTTPException
session = session(bind=engine)

user_router = APIRouter(prefix="/user")

@user_router.get("/")
async def user_profile():
    return {"user":"Bu userning profile sahifasi"}

@user_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(u: SignUpModel):
    db_username = session.query(User).filter(User.username == u.username).first()

    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    new_user = User(
        ism = u.ism,
        familiya = u.familiya,
        email = u.email,
        tel = u.tel,
        adress = u.adress,
        username = u.username,
        password = u.password
    )
    session.add(new_user)
    session.commit()

    return {"user":new_user}

