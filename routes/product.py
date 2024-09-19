from bson import ObjectId
from fastapi import APIRouter, HTTPException
from pydantic import SecretStr
from starlette import status

from models.product import Product

from config.db import product_collection

from schemas.product import serializeProduct, serializeProductList

product = APIRouter()


@product.get('/')
async def find_all_products():
    products = product_collection.find()
    return serializeProductList(products)


@product.post('/')
async def create_product(product: Product):
    product_dict = dict(product)
    product_collection.insert_one(product_dict)
    return serializeProduct(product_dict)


@product.put('/{id}')
async def update_product(id: str, product: Product):
    product_dict = product.dict(exclude_unset=True)
    result = product_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": product_dict},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return serializeProduct(result)


@product.delete('/{id}')
async def delete_product(id: str):
    return serializeProduct(product_collection.find_one_and_delete({"_id": ObjectId(id)}))
