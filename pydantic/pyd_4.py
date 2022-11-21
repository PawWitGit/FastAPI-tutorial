import time
from pydantic import BaseModel, Field
from datetime import datetime


class Blog(BaseModel):
    title: str
    created_at: datetime = Field(default=datetime.now())
    is_active: bool


print(Blog(title="Our first blog", is_active=True))
time.sleep(5)
print(Blog(title="Our second blog", is_active=True))
