from typing import Optional, List, Dict
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    UserId: Optional[str]
    FirstName: str
    LastName: str
    Email: EmailStr
    YearsPreviousExperience: str
    Skills: List[Dict[str, str]]

class UserUpdate(BaseModel):
    UserId: Optional[str]
    FirstName:  Optional[str]
    LastName:  Optional[str]
    Email:   Optional[EmailStr]
    YearsPreviousExperience: Optional[str]
    Skills: Optional[List[Dict[str, str]]  ]