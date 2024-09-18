import uuid
from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID
from app.db.session import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    affiliate_link = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)