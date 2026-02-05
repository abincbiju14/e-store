from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt

SECRET_KEY = "aaa"  # move to env later
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


class Auth:

    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # def _normalize_password(self, password: str) -> str:
    #     # bcrypt only uses first 72 bytes
    #     return password.encode("utf-8")[:72].decode("utf-8", errors="ignore")

    @staticmethod
    def hash_password(password):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        normalized = str(password).encode("utf-8")[:72].decode("utf-8", errors="ignore")
        return pwd_context.hash(normalized)

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.verify(password, hashed)

    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update(
            {"exp": expire, "iat": datetime.now(timezone.utc), "type": "access"}
        )
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
