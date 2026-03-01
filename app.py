from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

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