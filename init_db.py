from database import Base, engine
from models import User, Products, Deliver, Zakaz

Base.metadata.create_all(engine)
