from .products import router as products_router
from .categories import router as category_router
from .cart import router as cart_router

__all__ = ["products_router", "category_router", "cart_router"]