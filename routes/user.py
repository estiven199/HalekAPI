import uuid
from bson import ObjectId
from models.user import User, UserUpdate
from models.responses import UserResposive
from utils.functions import VerifyTokenRoute
from schemas.user import userEntity, usersEntity
from config.db import connect_to_database as ctb
from fastapi import APIRouter, Header, HTTPException, status


user_routes = APIRouter(route_class=VerifyTokenRoute)


@user_routes.get('/users/{user_id}', response_model=UserResposive, tags=["Module User"])
async def find_user(user_id: str, Authorization: str = Header(None)):
    db = ctb.connect_to_mongo(Authorization)
    data_user = db.users.find_one({"UserId": user_id})
    if data_user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return {
        "code": 0,
        "message": "success",
        "data": userEntity(data_user)
    }


@user_routes.get('/users', response_model=UserResposive, tags=["Module User"])
async def get_users(Authorization: str = Header(None)):
    db = ctb.connect_to_mongo(Authorization)
    return {
        "code": 0,
        "message": "success",
        "data": {"users": usersEntity(db.users.find())}
    }


@user_routes.post('/users', response_model=UserResposive, tags=["Module User"])
async def create_user(user: User, Authorization: str = Header(None)):
    db = ctb.connect_to_mongo(Authorization)
    new_user = dict(user)
    id = db.users.insert_one(new_user).inserted_id
    user = db.users.update_one({"_id": ObjectId(id)}, {
                               "$set": {"UserId": str(uuid.uuid4())}})
    user = db.users.find_one({"_id": ObjectId(id)})
    return {
        "code": 0,
        "message": "The User has been created",
        "data": userEntity(user)
    }


@user_routes.put("/users/{user_id}", response_model=UserResposive, tags=["Module User"])
async def update_user(user_id: str, user: UserUpdate, Authorization: str = Header(None)):
    db = ctb.connect_to_mongo(Authorization)
    update_data = dict(user)
    data_upate = {k: v for k, v in update_data.items() if v != None}
    db.users.find_one_and_update({
        "UserId": user_id
    }, {
        "$set": data_upate
    })
    return {
        "code": 0,
        "message": "User has been updated successfully",
        "data":  userEntity(db.users.find_one({"UserId": user_id}))
    }


@user_routes.delete("/users/{user_id}", response_model=UserResposive, tags=["Module User"])
async def delete_user(user_id: str, Authorization: str = Header(None)):
    db = ctb.connect_to_mongo(Authorization)
    db.users.find_one_and_delete({
        "UserId": user_id
    })
    return {
        "code": 0,
        "message": "The user has been deleted.",
        "data": {"UserId": user_id}
    }
