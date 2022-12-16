from utils.functions import write_token
from fastapi import APIRouter, Header, HTTPException, status

auth_routes = APIRouter()

@auth_routes.post("/generate_token", tags=["Module Authentication"])
def generate_token(
        x_token: str = Header(default=None, required=True),
        x_api_key: str = Header(default=None, required=True),
        x_secret_id: str = Header(default=None, required=True)):
 
    if not x_token or not x_api_key or not x_secret_id:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST
            )
    return write_token({
        "x_token": x_token,
        "x_api_key": x_api_key,
        "x_secret_id": x_secret_id}
    )
