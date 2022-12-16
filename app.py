from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_routes
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get('/')
def read_root():
    return RedirectResponse(url="/docs")

app.include_router(auth_routes, prefix="/api") 
load_dotenv()   