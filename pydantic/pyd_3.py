from pydantic import BaseModel
from enum import Enum


class Languages(str, Enum):
    PY = "Python"
    JAVA = "Java"
    GO = "Go"


class Blog(BaseModel):
    title: str
    language: Languages = Languages.PY
    is_active = bool


obj_1 = Blog(title="My first blog", language="Java", is_active=True)
obj_2 = Blog(title="My first blog", language="C++", is_active=True)
