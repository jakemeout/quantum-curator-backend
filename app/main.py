from fastapi import FastAPI
from app.routes import auth, products, favorites, search
from app.core.config import settings

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(favorites.router, prefix="/favorites", tags=["favorites"])
app.include_router(search.router, prefix="/search", tags=["search"])