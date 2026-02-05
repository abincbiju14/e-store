from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.admin import Admin as AdminModel
from app.error.logger import logger


def get_admin(admin_id: int, db: Session):
    admin = db.query(AdminModel).filter(AdminModel.id == admin_id).first()
    if not admin:
        logger.error(f"Admin retrieval failed: Admin with ID {admin_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found"
        )
    return admin
