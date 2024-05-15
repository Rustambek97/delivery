from database import engine,Base,session
from sqlalchemy import Column,Integer,String,Text,ForeignKey,Boolean,DateTime,Float
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    ism=Column(String(30))
    familiya=Column(String(30))
    email=Column(String(128))
    username=Column(String(100),unique=True)
    password=Column(String(128))
    tel=Column(String(15))
    adress=Column(String(300))
    is_staff=Column(Boolean,default=False)
    is_active=Column(Boolean,default=False)
    zakaz = relationship("Zakaz", back_populates="user")

class Zakaz(Base):
    __tablename__="zakaz"
    id=Column(Integer,primary_key=True)

    user_id=Column(Integer,ForeignKey('user.id'))
    user = relationship("User", back_populates="zakaz")

    product_id=Column(Integer,ForeignKey("products.id"))
    products = relationship("Products", back_populates="zakaz")

    deliver_id=Column(Integer,ForeignKey("deliver.id"))
    deliver = relationship("Deliver", back_populates="zakaz")

    zakaz_vaqti=Column(DateTime)
    yetkazish_vaqti=Column(DateTime)
    holat=(
        ("JARAYONDA","jarayonda"),
        ("YO'LDA","yo'lda"),
        ("YETKAZILDI","yetkazildi")
    )
    status=Column(ChoiceType(choices=holat), default="JARAYONDA")
    manzil=Column(String(300))

class Products(Base):
    __tablename__="products"
    id = Column(Integer, primary_key=True)
    narxi=Column(Float)
    paket=Column(String(300))
    manzil=Column(String(300))
    ogirligi=Column(Float)
    saqlash_tartibi=Column(Text)
    zakaz = relationship("Zakaz", back_populates="products")

class Deliver(Base):
    __tablename__="deliver"
    id = Column(Integer, primary_key=True)
    mashina_turi=Column(String(50))
    narxi=Column(Float)
    zakaz = relationship("Zakaz", back_populates="deliver")
