from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class userResponse(BaseModel):
    name: str
    age: int
    isAdult: bool