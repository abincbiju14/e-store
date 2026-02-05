from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.product import Product
from app.schemas.product import ProductCreate
from app.error.logger import logger


def create_product(product: ProductCreate, db: Session):
    new_product = Product(
        name=product.name,
        base_price=product.base_price,
        sku=product.sku,
        stock=product.stock,
    )
    product = db.query(Product).filter(Product.sku == product.sku).first()
    if product:
        # raise ValueError("Product with this SKU already exists")
        logger.error(
            f"Product creation failed: Product with SKU {product.sku} already exists"
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Product with this SKU already exists",
        )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product
