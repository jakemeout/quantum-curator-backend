from sqlalchemy import Column, Integer, String, DateTime
from app.db.session import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    affiliate_link = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)