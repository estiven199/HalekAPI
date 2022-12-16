from fastapi import FastAPI
from dotenv import load_dotenv
from docs import tags_metadata
from routes.auth import auth_routes
from routes.user import user_routes
from routes.vacancy import vacancy_routes
from starlette.responses import RedirectResponse

app = FastAPI(
    title="API HALEK",
    description="""The HALEK API allows you to perform all the operations you do with our web client.

The HALEK API was built on RESTful principles that ensure predictable URLs that make it easy to build applications. This API follows the rules of HTTP, which allows a wide range of HTTP clients to be used to interact with the API.

Each resource is exposed as a URL. The URL of each resource can be obtained by accessing the API Root Endpoint.""",
    version="0.0.1",
    openapi_tags=tags_metadata
)



@app.get('/')
def read_root():
    return RedirectResponse(url="/docs")

app.include_router(auth_routes, prefix="/api") 
app.include_router(user_routes, prefix="/api")
app.include_router(vacancy_routes, prefix="/api")
load_dotenv()   