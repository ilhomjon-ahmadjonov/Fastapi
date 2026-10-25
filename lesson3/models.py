from database import Base
from sqlalchemy import Column,Integer,String,DECIMAL,Text,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(primary_key=True)
    username = Column(String(50),nullable=False)
    first_name = Column(String(30))


    comments = relationship('Comment', back_populates='user')

class Book(Base):
    __tablename__ = 'books'

    id = Column(primary_key=True)
    title = Column(String(50),nullable=False)
    desc = Column(String(30))

    comments = relationship('Camment', back_populates='book')

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer,primary_key=True)
    comment = Column(String(30), nullable=False)

    book_id = Column(Integer,ForeignKey('books.id'))
    user_id = Column(Integer,ForeignKey('users.id'))

    book = relationship('Book',back_populates='comments')
    user = relationship('User',back_populates='comments')