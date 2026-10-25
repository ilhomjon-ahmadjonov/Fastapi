from fastapi import APIRouter
from .views import get_product_count,get_products

router = APIRouter()

@router.get('/count')
def soni():
    return get_product_count()

@router.get('/list')
def product_list():
    return get_products()