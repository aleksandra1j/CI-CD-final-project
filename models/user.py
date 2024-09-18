import uuid

from pydantic import BaseModel, Field, EmailStr, SecretStr


class User(BaseModel):
    # id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    email: str
    password: SecretStr=None

    class Config:
        populate_by_name = True
