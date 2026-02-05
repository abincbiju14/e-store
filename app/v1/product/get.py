from fastapi import HTTPException
from app.models.product import Product
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.error.logger import logger


def get_product(product_id: int):
    db = SessionLocal()
    try:
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            logger.error(
                f"Product retrieval failed: Product with ID {product_id} not found"
            )
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    finally:
        db.close()
