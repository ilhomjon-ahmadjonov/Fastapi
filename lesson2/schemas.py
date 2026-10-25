from pydantic import BaseModel,Field,ConfigDict,RootModel
from typing import Optional,List
from decimal import Decimal

class BookCreateSchema(BaseModel):
    title: str = Field(max_length=120)
    desc: Optional[str] = None
    price: Decimal = Field(gte=0, decimal_places=2,max_digits=12)

class BookOutSchema(BaseModel):
    id: int
    title: str
    desc: Optional[str] = None
    price: Decimal = Field(gte=0,decimal_places=2,max_digits=12)


    model_config = ConfigDict(from_attributes=True)

class BookSchema(RootModel):
   
   root: List[BookOutSchema]

    
class BookUpdateSchema(BaseModel):
    title: str = Field(max_length=120)
    desc: Optional[str] = None
    price: Decimal = Field(gte=0, decimal_places=2,max_digits=12)