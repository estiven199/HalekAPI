import jwt
from os import getenv
from models.auth import keys
from datetime import datetime, timedelta

def expire_date(days: int):
    return datetime.now() + timedelta(days)


def write_token(data: keys):
    return jwt.encode(payload={**data, "exp": expire_date(10)}, key=getenv("SECRET"), algorithm="HS256")