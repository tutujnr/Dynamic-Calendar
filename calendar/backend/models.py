from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime
