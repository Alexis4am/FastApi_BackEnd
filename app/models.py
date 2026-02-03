from sqlalchemy import Column, String
from database import Base

class Persona(Base):
    __tablename__ = "personas"

    # En tu captura, cedula es Primary Key
    cedula = Column(String, primary_key=True, index=True) 
    nombre = Column(String)
    direccion = Column(String)