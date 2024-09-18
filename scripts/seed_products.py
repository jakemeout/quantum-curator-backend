from app.db.session import SessionLocal
from app.services.product_generation import add_product  # Assuming you put the add_product function in services/product.py
import os
import sys

# Get the absolute path of the project's root directory
project_root = os.path.dirname(os.path.abspath(__file__))

# Add the project root to the Python path
sys.path.append(project_root)


def seed_products():
    db = SessionLocal()

    # Add some example products
    add_product(db, name="Product 1", description="Description for product 1", price=100, affiliate_link="http://example.com/product1")
    add_product(db, name="Product 2", description="Description for product 2", price=200, affiliate_link="http://example.com/product2")
    add_product(db, name="Product 3", description="Description for product 3", price=300, affiliate_link="http://example.com/product3")

    db.close()

if __name__ == "__main__":
    seed_products()