from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from models import User
from models import userResponse

app = FastAPI()

currentUser = User(
    name = "Alexandra Vasyukova",
    age = 19
)

def isAdult(age):
    return age >= 18

@app.post("/user", response_model=userResponse)
async def createUser(user: User):
    is_adult = isAdult(user.age)

    user_response = userResponse(
        name = user.name,
        age = user.age,
        is_adult = is_adult
    )

    return user_response


@app.get("/users")
async def getUser():
    users = [
        User(name="Иван Петров", age=25),
        User(name="Мария Иванова", age=17),
        User(name="Петр Сидоров", age=30)
    ]
    return users

class numbers(BaseModel):
    num1: int
    num2: int

@app.post("/calculate")
async def calculate(nums: numbers):
    result = nums.num1 + nums.num2
    return {"result": result}

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    return html