from pydantic import BaseModel
from typing import List, Optional


class Comment(BaseModel):
    text: Optional[str] = None


class Blog(BaseModel):
    title: str
    comment: Optional[List[Comment]]
    is_active: bool


obj_1 = Blog(
    title="Our first blog",
    comment=[
        {"text": "My comment"},
        {"text": "Your comment"},
    ],
    is_active=True,
)

print(obj_1)
