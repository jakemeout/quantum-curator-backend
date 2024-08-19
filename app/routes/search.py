from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.search_pattern import SearchPattern
from app.db.session import SessionLocal
from app.models.search_pattern import SearchPattern as SearchPatternModel
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

@router.post("/", response_model=SearchPattern)
def search_products(search_term: str, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    search_pattern = db.query(SearchPatternModel).filter_by(user_id=current_user.id, search_term=search_term).first()

    if search_pattern:
        search_pattern.frequency += 1
    else:
        search_pattern = SearchPatternModel(user_id=current_user.id, search_term=search_term)
        db.add(search_pattern)

    db.commit()
    return search_pattern

@router.get("/history", response_model=List[SearchPattern])
def get_search_history(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return db.query(SearchPatternModel).filter(SearchPatternModel.user_id == current_user.id).all()

@router.get("/popular", response_model=List[SearchPattern])
def get_popular_searches(limit: int = 10, db: Session = Depends(get_db)):
    return db.query(SearchPatternModel).order_by(SearchPatternModel.frequency.desc()).limit(limit).all()
