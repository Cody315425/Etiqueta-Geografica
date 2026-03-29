from sqlmodel import Field, SQLModel
from typing import Optional

class SignImage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    file_name: str
    description: str = Field(max_length=256)
    latitude: float
    longitude: float