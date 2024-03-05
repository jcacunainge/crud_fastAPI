# app/models.py
from sqlalchemy import Column, Integer, String
from v1.db.config import Base

# clase 
class Book(Base):
    # nombre de la tabla
    __tablename__ = "book"
    
    # Las columnas de nuestra tabla y el tipo de dato de cada una
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)