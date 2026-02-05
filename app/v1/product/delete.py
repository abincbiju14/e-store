from fastapi import HTTPException
from app.models.product import Product  
from app.schemas.product import ProductCreate



# def create_product(ProductCreate: ProductCreate):
#     new_product = Product(
#         name=ProductCreate.name,
#         base_price=ProductCreate.base_price,
#         sku=ProductCreate.sku,
#         stock=ProductCreate.stock
#     )
#     # Here you would typically add the new_product to the database session and commit
#     return {"message": "Product created successfully", "product": ProductCreate}