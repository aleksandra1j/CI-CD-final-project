from bson import ObjectId

from models.product import Product


def serializeProduct(product: dict) -> dict:
    if "_id" in product and isinstance(product["_id"], ObjectId):
        product["_id"] = str(product["_id"])
    return product


def serializeProductList(products: list) -> list:
    return [serializeProduct(product) for product in products]