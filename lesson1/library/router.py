from fastapi import APIRouter
from .crud import get_book,get_author

router = APIRouter()

@router.get('/name')
def book_name():
    return get_book()

@router.get('/author')
def get_authors():
    return get_author()