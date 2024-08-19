from sqlalchemy.orm import Session
from app.models.product import Product

def add_product(db: Session, name: str, description: str, price: int, affiliate_link: str):
    new_product = Product(
        name=name,
        description=description,
        price=price,
        affiliate_link=affiliate_link
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product