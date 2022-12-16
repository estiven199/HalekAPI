import jwt
from os import getenv
from jwt import exceptions
from models.auth import keys
from datetime import datetime, timedelta
from fastapi import  HTTPException, status


def expire_date(days: int):
    return datetime.now() + timedelta(days)


def write_token(data: keys):
    return jwt.encode(payload={**data, "exp": expire_date(10)}, key=getenv("SECRET"), algorithm="HS256")


def validate_token(token, output=False):
    try:
        if output:
            return jwt.decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        jwt.decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token.",
        )
    except exceptions.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to perform this operation"
        )
