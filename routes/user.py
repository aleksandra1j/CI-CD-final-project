from bson import ObjectId
from fastapi import APIRouter, HTTPException
from pydantic import SecretStr
from starlette import status

from models.user import User

from config.db import conn

from schemas.user import serializeDict, serializeList

user = APIRouter()


@user.get('/')
async def find_all_users():
    return serializeList(conn.local.user.find())


@user.post('/')
async def create_user(user: User):
    user_dict = dict(user)
    if isinstance(user_dict.get("password"), SecretStr):
        user_dict["password"] = user_dict["password"].get_secret_value()
    conn.local.user.insert_one(user_dict)
    return serializeDict(user_dict)


@user.put('/{id}')
async def update_user(id, user: User):
    user_dict = user.dict(exclude_unset=True)

    if 'password' in user_dict:
        user_dict['password'] = user_dict['password'].get_secret_value()

    result = conn.local.user.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": user_dict},
        return_document=True
    )

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return serializeDict(result)


@user.delete('/{id}')
async def delete_user(id, user: User):
    return serializeDict(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
