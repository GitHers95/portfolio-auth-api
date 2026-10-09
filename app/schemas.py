from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    is_active: bool
    created_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
# Schéma pour créer un produit (requête)
class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    is_available: bool = True

# Schéma pour lire un produit (réponse)
class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    is_available: bool
    created_at: datetime

    class Config:
        from_attributes = True
