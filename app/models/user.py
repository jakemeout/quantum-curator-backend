from sqlalchemy import Column, Integer, String, DateTime
from app.db.session import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    search_patterns = relationship("SearchPattern", back_populates="user")
