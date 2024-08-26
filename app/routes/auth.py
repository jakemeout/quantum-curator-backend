from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead, PasswordResetRequest, PasswordReset
from app.services.auth import authenticate_user, create_user, create_access_token, generate_password_reset_token, verify_password_reset_token
from app.db.session import SessionLocal
from app.core.security import get_password_hash
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup", response_model=UserRead)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/password-reset/request")
def request_password_reset(request: PasswordResetRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # Generate a password reset token
    token = generate_password_reset_token(user.email) # type: ignore
    
    # Here you would send an email with the token to the user's email address.
    # For this example, we're just returning the token.
    return {"reset_token": token}

@router.post("/password-reset/reset")
def reset_password(reset: PasswordReset, db: Session = Depends(get_db)):
    email = verify_password_reset_token(reset.token)
    if email is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired token")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # Hash the new password and update the user's record
    user.password_hash = get_password_hash(reset.new_password) # type: ignore
    db.commit()
    
    return {"message": "Password has been reset successfully"}