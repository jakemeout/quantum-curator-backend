from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.product import Product
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/today", response_model=List[Product])
def get_today_products(db: Session = Depends(get_db)):
    # Logic to fetch today's products from the database
    products = db.query(Product).all()  # Example logic
    return products