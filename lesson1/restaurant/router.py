from fastapi import APIRouter
from .crud import get_list,get_food

router = APIRouter()

@router.get('/food')
def taomlar():
    return get_food()

@router.get('/list')
def get_lists():
    return get_list()