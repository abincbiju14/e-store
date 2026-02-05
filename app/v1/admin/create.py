from fastapi import HTTPException, status, Depends
from app.models.admin import Admin as AdminModel
from app.schemas.admin import Admin as AdminSchema
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.error.logger import logger
from app.core.auth import Auth


def create_admin(admin: AdminSchema.AdminCreate, db: Session = Depends(get_db)):
    new_admin = AdminModel(
        first_name=admin.first_name,
        last_name=admin.last_name,
        email=admin.email,
        phone_number=admin.phone_number,
        password=Auth.hash_password(admin.password),
    )

    existing_admin = (
        db.query(AdminModel).filter(AdminModel.email == admin.email).first()
    )
    if existing_admin:
        logger.error(
            f"Admin creation failed: Admin with email {admin.email} already exists"
        )
        raise HTTPException(status_code=400, detail="Admin already exists")

    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin


def login_admin(admin: AdminSchema.AdminLogin, db: Session):
    login = db.query(AdminModel).filter(AdminModel.email == admin.email).first()
    if not login or not Auth.verify_password(admin.password, login.password):
        logger.error("Invalid credentials")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = Auth.create_access_token({"sub": str(login.id)})
    return {"access_token": token, "token_type": "bearer"}
