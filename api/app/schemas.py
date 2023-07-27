from pydantic import BaseModel
from typing import List
from datetime import datetime
class CreateNews(BaseModel):
    IdAgencia: int
    dateTime: datetime
    headline: str
    id: int
    prob: float
    status: str
    treated: bool
