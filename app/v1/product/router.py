from fastapi import APIRouter
from app.schemas.product import Product as ProductSchema
from app.v1.product.create import create_product
from app.v1.product.get import get_product
from fastapi import Depends
from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/")
def create(product: ProductSchema.ProductCreate, db: Session = Depends(get_db)):
    return create_product(product, db)


# @router.delete("/{product_id}")
# def delete(product_id: int):
#     return delete_product(product_id)


@router.get("/{product_id}")
def get(product_id: int):
    return get_product(product_id)


@router.put("/{product_id}")
def update(product_id: int, product: ProductSchema.ProductCreate):
    return {"product_id": product_id, "updated_data": product}
