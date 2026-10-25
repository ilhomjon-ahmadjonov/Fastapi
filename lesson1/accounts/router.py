from fastapi import APIRouter
from .views import get_accounts_count, get_accounts


router = APIRouter()

@router.get('/count')
def count():
    return get_accounts_count()

@router.get('/list')
def accounts_list():

    return get_accounts()
