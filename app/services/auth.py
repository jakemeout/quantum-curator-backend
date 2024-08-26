from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.models.user import User
from app.schemas.user import UserCreate
from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from app.core.security import verify_password, get_password_hash, create_access_token
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from app.core.config import settings

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False
    if not verify_password(password, user.password_hash): # type: ignore
        return False
    return user

def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, password_hash=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def generate_password_reset_token(email: str) -> str:
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    return serializer.dumps(email, salt=settings.SECRET_KEY)

def verify_password_reset_token(token: str, expiration: int = 3600) -> str:
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    try:
        email = serializer.loads(token, salt=settings.SECRET_KEY, max_age=expiration)
    except (SignatureExpired, BadSignature):
        return None # type: ignore
    return email