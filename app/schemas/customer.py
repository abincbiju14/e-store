from pydantic import BaseModel


class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    password: str


class CustomerResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str


class CustomerGetResponse(BaseModel):
    data: list[CustomerResponse]


class CustomerLogin(BaseModel):
    email: str
    password: str


class CustomerLoginResponse(BaseModel):
    token: str


class Config:
    from_attributes = True