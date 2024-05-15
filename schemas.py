from pydantic import BaseModel

class SignUpModel(BaseModel):
    ism: str
    familiya: str
    email: str
    tel: str
    adress: str
    username: str
    password: str

    class Config:
        orm_mode = True
