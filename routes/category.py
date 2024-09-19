from fastapi import APIRouter, HTTPException
from models.category import Category
from config.db import category_collection
from schemas.category import serializeCategory, serializeCategoryList
from bson import ObjectId

category = APIRouter()


@category.get('/')
async def get_all_categories():
    categories = category_collection.find()
    return serializeCategoryList(categories)


@category.post('/')
async def create_category(category: Category):
    category_dict = dict(category)
    category_collection.insert_one(category_dict)
    return serializeCategory(category_dict)


@category.put('/{id}')
async def update_category(id: str, category: Category):
    result = category_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": category.dict(exclude_unset=True)},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=404, detail="Category not found")
    return serializeCategory(result)


@category.delete('/{id}')
async def delete_category(id: str):
    return serializeCategory(category_collection.find_one_and_delete({"_id": ObjectId(id)}))
