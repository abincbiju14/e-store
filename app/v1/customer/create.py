from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from app.models.customer import Customer as CustomerModel
from app.schemas.customer import Customer as CustomerSchema
from app.error.logger import logger
from app.core.auth import Auth


def create_customer(
    customer: CustomerSchema.CustomerCreate,
    db: Session,
):
    new_customer = CustomerModel(
        first_name=customer.first_name,
        last_name=customer.last_name,
        email=customer.email,
        phone_number=customer.phone_number,
        password=Auth.hash_password(customer.password),
        # password=customer.password,
    )
    existing_customer = (
        db.query(CustomerModel).filter(CustomerModel.email == customer.email).first()
    )
    if existing_customer:
        logger.error(
            f"Customer creation failed: Customer with email {customer.email} already exists"
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Customer with this email already exists",
        )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


def login_customer(data: CustomerSchema.CustomerLogin, db: Session):
    customer = db.query(CustomerModel).filter(CustomerModel.email == data.email).first()

    if not customer or not Auth.verify_password(data.password, customer.password):
        logger.error("Invalid credentials")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = Auth.create_access_token({"sub": str(customer.id)})
    return {"access_token": token, "token_type": "bearer"}
