from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# IMPORT ALL MODELS HERE
from app.models.customer import Customer
from app.models.product import Product