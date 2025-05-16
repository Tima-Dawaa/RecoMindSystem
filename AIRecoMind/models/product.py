from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: str
    name: str
    type: str
    appearance: str
    color: str
    department: str 
    gender: str
    details: str