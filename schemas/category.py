from bson import ObjectId


def serializeCategory(category: dict) -> dict:
    if "_id" in category and isinstance(category["_id"], ObjectId):
        category["_id"] = str(category["_id"])
    return category


def serializeCategoryList(categories: list) -> list:
    return [serializeCategory(category) for category in categories]
