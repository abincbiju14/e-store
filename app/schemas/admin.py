from __future__ import annotations
from pydantic import BaseModel


class Admin:
    class AdminCreate(BaseModel):
        first_name: str
        last_name: str
        email: str
        phone_number: str
        password: str

    class AdminResponse(BaseModel):
        id: int
        first_name: str
        last_name: str
        email: str
        phone_number: str

    class AdminGetResponse(BaseModel):
        data: list[Admin.AdminResponse]

    class AdminLogin(BaseModel):
        email: str
        password: str

    class AdminLoginResponse(BaseModel):
        access_token: str
        token_type: str

    class Config:
        from_attributes = True
