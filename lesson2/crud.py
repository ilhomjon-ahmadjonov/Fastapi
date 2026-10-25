from sqlalchemy.orm import Session
from models import Book
from schemas import BookCreateSchema,BookOutSchema,BookSchema,BookUpdateSchema
from fastapi import status
from fastapi .exceptions import HTTPException
from typing import List

def create_book(db: Session, data: BookCreateSchema):


    book = Book(title=data.title,desc=data.desc,price=data.price)

    db.add(book)
    db.commit()
    db.refresh(book)

    return {
        "msg": "Book created",
        "book": BookOutSchema(**data.model_dump())
    }

def detail_book(book_id: int,db: Session):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(detail='book not found',status_code=404)
    return{
        "book": BookOutSchema.model_validate(book)
    }

def list_book(db:Session):
    books = db.query(Book).all()
    return {
        "book": BookSchema.model_validate(books)
    }

def delete_book(book_id:int,db:Session):
    book = db.query(Book).filter(book_id == Book.id).first()

    db.delete(book)
    db.commit()
    
    return{
        "msg": "Ochirildi"
        }

def update_book(book_id:int,data:BookUpdateSchema,db:Session):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return{"msg":"Kitob topilmadi"}

    for i,j in data.model_dump(exclude_unset=True).items:
        setattr(book,i,j)

    db.commit()
    db.refresh(book)

    return {
        "msg": "ozgartirildi",
        "book": BookOutSchema.model_validate(book)
    }

   
   