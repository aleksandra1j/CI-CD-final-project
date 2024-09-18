from fastapi import FastAPI


from routes.user import user
from routes.product import product
from routes.category import category

app = FastAPI(title="Makeup/Skincare Online Store", description="This app is for CI/CD purposes")
app.include_router(user, prefix="/users")

app.include_router(product, prefix="/products")

app.include_router(category, prefix="/categories")

