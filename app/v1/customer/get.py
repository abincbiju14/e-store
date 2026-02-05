from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.customer import Customer
from app.error.logger import logger


def get_customer(customer_id: int, db: Session):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        logger.error(
            f"Customer retrieval failed: Customer with ID {customer_id} not found"
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    return customer
