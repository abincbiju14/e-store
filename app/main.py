from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base

from app.v1.product.router import router as product_router
from app.v1.customer.router import router as customer_router
from app.v1.admin.router import router as admin_router


app = FastAPI(title="Product Service")

app.include_router(product_router, prefix="/api/v1/product", tags=["Product"])
app.include_router(customer_router, prefix="/api/v1/customer", tags=["Customer"])
app.include_router(admin_router, prefix="/api/v1/admin", tags=["Admin"])


Base.metadata.create_all(bind=engine)


@app.get("/health")
def read_health():
    return {"status": "healthy"}
