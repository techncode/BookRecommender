from redis_om import HashModel, JsonModel
from redis_om import (
    Field,
    HashModel,
    Migrator
)

class Book(JsonModel):
    isbn: str = Field(index=True)
    title: str  = Field(index = True,full_text_search=True)
    author: str = Field(index = True,full_text_search=True)
    year: int = Field(index = True)
    publisher: str