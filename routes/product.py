from bson import ObjectId
from fastapi import APIRouter, HTTPException
from pydantic import SecretStr
from starlette import status

from models.product import Product

from config.db import conn

from schemas.product import serializeProduct, serializeProductList

product = APIRouter()


@product.get('/')
async def find_all_products():
    return serializeProductList(conn.local.product.find())


@product.post('/')
async def create_product(product: Product):
    product_dict = dict(product)
    conn.local.product.insert_one(product_dict)
    return serializeProduct(product_dict)


@product.put('/{id}')
async def update_product(id, product: Product):
    product_dict = product.dict(exclude_unset=True)

    result = conn.local.user.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": product_dict},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")

    return serializeProduct(result)


@product.delete('/{id}')
async def delete_prodict(id, product: Product):
    return serializeProduct(conn.local.product.find_one_and_delete({"_id": ObjectId(id)}))
