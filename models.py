from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class userResponse(BaseModel):
    name: str
    age: int
    isAdult: bool

class feedback(BaseModel):
    name: str
    message: str

class feedbackResponce(BaseModel):
    message: str