from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    sku: str
    base_price: float
    stock:int

class ProductResponse(BaseModel):
    id: int
    name: str
    base_price: float
    stock:int
    sku:str

class ProductGetResponse(BaseModel):
    data : list[ProductResponse]

