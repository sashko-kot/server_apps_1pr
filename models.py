from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from typing import ClassVar
import re

class User(BaseModel):
    name: str
    age: int

class userResponse(BaseModel):
    name: str
    age: int
    isAdult: bool

class feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    forbiddenWords: ClassVar[List[str]] = ["кринж", "рофл", "вайб"]
    @field_validator('message')
    @classmethod
    def check_message(cls, v:str):
        messageLower = v.lower()
        for word in cls.forbiddenWords:
            pattern = r'\b' + re.escape(word) + r'\b'
            if re.search(pattern, messageLower):
                raise ValueError(f"Использование недопустимых слов")
        return v
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str):
        if not v.strip():
            raise ValueError("Имя не может быть пустым или состоять только из пробелов")
        
        if not re.match(r'^[a-zA-Zа-яА-Я\s-]+$', v):
            raise ValueError("Имя может содержать только буквы, пробелы и дефисы")
        
        return v.strip()

class feedbackResponce(BaseModel):
    message: str