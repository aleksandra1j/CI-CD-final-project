from bson import ObjectId

from models.user import User


def serializeDict(user: dict) -> dict:
    if "_id" in user and isinstance(user["_id"], ObjectId):
        user["_id"] = str(user["_id"])
    return {key: value for key, value in user.items() if key != "password"} # Excluding the password field from the output


def serializeList(users: list) -> list:
    return [serializeDict(user) for user in users]
