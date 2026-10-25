from fastapi import FastAPI
from database import Base,engine
from models import Book
from router import router as book_router

app = FastAPI()
app.include_router(book_router,prefix='/books')

Base.metadata.create_all(bind=engine)