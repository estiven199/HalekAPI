from typing import Optional, List, Dict
from pydantic import BaseModel


class Vacancy(BaseModel):
    VacancyId: Optional[str]
    PositionName: str
    CompanyName: str
    Salary: str
    Currency: str
    VacancyLink: str
    RequiredSkills: List[Dict[str, str]]


class VacancyUpdate(BaseModel):
    VacancyId: Optional[str]
    PositionName: Optional[str]
    CompanyName: Optional[str]
    Salary: Optional[str]
    Currency: Optional[str]
    VacancyLink: Optional[str]
    RequiredSkills: Optional[List[Dict[str, str]]]
