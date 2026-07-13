from pydantic import BaseModel, Field
from typing import Optional


class CartItemBase(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)


class CartItem(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int
    subtotal: float
    image_url: Optional[str] = Field(None)


class CartResponse(BaseModel):
    items: list[CartItem]
    total: float
    items_count: int
