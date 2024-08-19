from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.product import Product
from app.db.session import SessionLocal
from app.models.user import User
from app.models.product import Product as ProductModel
from app.models.user import User as UserModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get the current user (mocked for simplicity)
def get_current_user(db: Session = Depends(get_db)):
    user = db.query(UserModel).first()  # Simplified, replace with actual user lookup logic
    return user

@router.post("/add", response_model=Product)
def add_to_favorites(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    current_user.favorites.append(product)
    db.commit()
    return product

@router.get("/", response_model=List[Product])
def get_favorites(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return current_user.favorites

@router.delete("/remove", response_model=Product)
def remove_from_favorites(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    current_user.favorites.remove(product)
    db.commit()
    return product
