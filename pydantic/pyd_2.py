from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    title: str
    description: Optional[str] = None
    is_active = bool


obj_1 = Blog(title="My first Blog", is_active=True)
print(obj_1)
