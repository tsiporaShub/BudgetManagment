from pydantic import BaseModel, constr, conint


class User(BaseModel):
    id: int
    name: constr(min_length=3, max_length=15)
    password: constr(min_length=6, max_length=10)
    email: constr(pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    age: conint(gt=0)
    city: str
