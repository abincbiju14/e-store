from fastapi import APIRouter
from app.schemas.customer import CustomerCreate, CustomerLogin, CustomerResponse
from app.v1.customer.create import create_customer, login_customer
from app.v1.customer.get import get_customer
from fastapi import Depends
from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model= CustomerResponse)
def create(customer: CustomerCreate, db: Session = Depends(get_db)):
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


@router.post("/customerAuth")
def login(CustomerLogin: CustomerLogin, db: Session = Depends(get_db)):
    return login_customer(CustomerLogin, db)




