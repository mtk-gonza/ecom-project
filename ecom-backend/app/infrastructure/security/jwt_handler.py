from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.config.settings import settings

def create_access_token(id: int, username: str, roles: list[str], expires_delta: timedelta):
    expire = datetime.utcnow() + expires_delta
    to_encode = {
        'id': id,
        'username': username,
        'roles': roles,
        'exp': expire
    }
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None