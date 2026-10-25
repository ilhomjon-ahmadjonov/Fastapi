from fastapi import APIRouter, Depends
from crud import create_book, detail_book,list_book,delete_book,update_book,BookUpdateSchema
from database import get_db
from schemas import BookCreateSchema
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/create',status_code=201)
def book_create(data: BookCreateSchema, db: Session = Depends(get_db)):
    return create_book(db,data)

@router.get('/detail/{book_id}', status_code=200)
def book_detail(book_id:int, db: Session = Depends(get_db)):
    return detail_book(book_id,db)

@router.get('/list', status_code=200)
def book_list(db: Session = Depends(get_db)):
    return list_book(db)

@router.delete('/delete{book_id}')
def book_delete(book_id:int,db: Session = Depends(get_db)):
    return delete_book(db)

@router.patch('/update{book_id}')
def book_update(book_id:int,data: BookUpdateSchema, db: Session = Depends(get_db)):
    return update_book(db)