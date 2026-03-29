from sqlmodel import SQLModel, Field

class ImageData(SQLModel):
    description: str = Field(max_length=256)
    latitude: float
    longitude: float