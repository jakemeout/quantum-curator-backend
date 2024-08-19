from pydantic import BaseModel

class SearchPattern(BaseModel):
    id: int
    user_id: int
    search_term: str
    frequency: int

    class Config:
        orm_mode = True