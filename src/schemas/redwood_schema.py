from pydantic import BaseModel


class PaginatorInfo(BaseModel):
    currentPage: int
    lastPage: int
    lastDate: str
    uuid: str
