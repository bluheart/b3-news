from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean

class News(Base):
    __tablename__ = "noticias"

    IdAgencia = Column(Integer, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    dateTime = Column(DateTime(timezone=True), nullable=False)
    headline = Column(String, nullable=False)
    prob = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    treated = Column(Boolean, nullable=False)
