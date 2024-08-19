from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from app.db.session import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class SearchPattern(Base):
    __tablename__ = "search_patterns"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    search_term = Column(String, index=True)
    frequency = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="search_patterns")
