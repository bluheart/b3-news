from pydantic import BaseModel
from typing import List

class CreateNews(BaseModel):
    IdAgencia: int
    dateTime: str
    headline: str
    id: int
