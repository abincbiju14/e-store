from fastapi import APIRouter
from app.schemas.customer import Customer as CustomerSchema
from app.v1.customer.create import create_customer, login_customer
from app.v1.customer.get import get_customer
from fastapi import Depends
from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=CustomerSchema.CustomerResponse)
def create(customer: CustomerSchema.CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(customer, db)


# @router.delete("/{customer_id}")
# def delete(customer_id: int):
#     return delete_customer(customer_id)


@router.get("/{customer_id}")
def get(customer_id: int, db: Session = Depends(get_db)):
    return get_customer(customer_id, db)


# @router.put("/{customer_id}")
# def update(customer_id: int, customer: CustomerCreate, db: Session = Depends(get_db)):
#     return update_customer(customer_id, customer, db)


@router.post("/customerAuth", response_model=CustomerSchema.CustomerLoginResponse)
def login(CustomerLogin: CustomerSchema.CustomerLogin, db: Session = Depends(get_db)):
    return login_customer(CustomerLogin, db)
