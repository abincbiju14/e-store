from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerLogin, CustomerResponse
from app.error.logger import logger
from app.v1.customer.auth import hash_password, create_access_token, verify_password


def create_customer(customer: CustomerCreate, db: Session, response_model=CustomerResponse):
    new_customer = Customer(
        first_name=customer.first_name,
        last_name=customer.last_name,
        email=customer.email,
        phone_number=customer.phone_number,
        password=hash_password(customer.password),
        # password=customer.password,
    )
    existing_customer = (
        db.query(Customer).filter(Customer.email == customer.email).first()
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


def login_customer(data: CustomerLogin, db: Session):
    customer = db.query(Customer).filter(Customer.email == data.email).first()

    if not customer or not verify_password(data.password, customer.password):
        logger.error("Invalid credentials")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(customer.id)})
    return {"access_token": token, "token_type": "bearer"}