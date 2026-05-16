from fastapi import FastAPI
from pydantic import BaseModel
from backend.services.predict import predict_role

app = FastAPI()

class SkillInput(BaseModel):
    skills: list[str]

@app.get("/")
def home():
    return {"message": "AI Career Copilot API"}

@app.post("/predict")
def predict(data: SkillInput):

    role = predict_role(data.skills)

    return {"prediction": role}