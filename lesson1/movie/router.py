from fastapi import APIRouter
from .crud import get_movie,get_list

router = APIRouter()

@router.get('/movie')
def movies():
    return get_movie()

@router.get('/list')
def movie_list():
    return get_list()
