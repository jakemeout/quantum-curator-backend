from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    affiliate_link: str

    class Config:
        orm_mode = True