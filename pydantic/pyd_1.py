from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    is_active: bool


obj_1 = Blog(title="My first blog", is_active=True)
# Blog(title='Second One',is_active='yup!')
print(obj_1.title)
