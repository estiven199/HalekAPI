from typing import  Dict
from pydantic import BaseModel


class UserResposive(BaseModel):
    code: int
    message: str
    data: Dict


class VacancyResposive(BaseModel):
    code: int
    message: str
    data: Dict
