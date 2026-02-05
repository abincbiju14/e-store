from fastapi import APIRouter
from app.schemas.admin import Admin as AdminSchema
from app.v1.admin.create import create_admin, login_admin
from app.v1.admin.get import get_admin
from fastapi import Depends
from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=AdminSchema.AdminResponse)
def create(admin: AdminSchema.AdminCreate, db: Session = Depends(get_db)):
    return create_admin(admin, db)


@router.post("/login", response_model=AdminSchema.AdminLoginResponse)
def login(admin: AdminSchema.AdminLogin, db: Session = Depends(get_db)):
    return login_admin(admin, db)


@router.get("/{admin_id}", response_model=AdminSchema.AdminResponse)
def get(admin_id: int, db: Session = Depends(get_db)):
    return get_admin(admin_id, db)
