from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from models import User
from models import userResponse
from models import feedbackResponce
from models import feedback
from datetime import datetime
from fastapi import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

app = FastAPI()

feedbackStorage = []
feedbackCounter = 0

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()}
    )

@app.post("/feedback", response_model=feedbackResponce)
async def createFeedback(feedback: feedback):
    global feedbackCounter
    
    if not feedback.name.strip():
        raise HTTPException(status_code=400, detail="Имя не может быть пустым")
    
    if not feedback.message.strip():
        raise HTTPException(status_code=400, detail="Сообщение не может быть пустым")
    
    feedbackCounter += 1
    feedback_entry = {
        "id": feedbackCounter,
        "name": feedback.name.strip(),
        "message": feedback.message.strip(),
        "timestamp": datetime.now().isoformat()
    }
    feedbackStorage.append(feedback_entry)
    
    # Возвращаем ответ в точности как в схеме: {"message": "string"}
    return feedbackResponce(
        message=f"Feedback received. Thank you, {feedback.name}."
    )









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