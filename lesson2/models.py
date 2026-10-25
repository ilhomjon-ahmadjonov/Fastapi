from database import Base
from sqlalchemy import Column,String,DECIMAL,Integer,Text

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer,primary_key=True)
    title = Column(String(50),nullable=False)
    desc = Column(Text)
    price = Column(DECIMAL,nullable=False)




