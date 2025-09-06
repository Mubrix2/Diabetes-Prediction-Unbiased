from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
import pickle
import pandas as pd
from fastapi.responses import JSONResponse


app = FastAPI()


with open("DiabetesModelNew.pkl", 'rb') as f:
  model = pickle.load(f)

class UserInput(BaseModel):
    
  Gender: Literal[0, 1] = Field(..., ge=0, le=1, description='The gender is encoded to either 0 or 1')
  AGE: int = Field(..., gt=0, lt=120)
  Urea: float | int = Field(..., gt=0)
  Cr: float |int = Field(..., gt=0)
  HbA1c: float | int = Field(..., gt=0)
  Chol: float | int = Field(..., gt=0)
  TG: float | int = Field(..., gt=0)
  HDL: float | int = Field(..., gt=0)
  LDL: float | int = Field(..., gt=0)
  VLDL: float | int = Field(..., gt=0)
  BMI: float | int = Field(..., gt=0)


@app.post('/predict')
def predict(data: UserInput):
  
  input_df = pd.DataFrame([{
    'Gender': data.Gender,
    'AGE': data.AGE,
    'Urea': data.Urea,
    'Cr': data.Cr,
    'HbA1c': data.HbA1c,
    'Chol': data.Chol,
    'TG': data.TG,
    'HDL': data.HDL,
    'LDL': data.LDL,
    'VLDL': data.VLDL,
    'BMI': data.BMI
  }])

  prediction = int(model.predict(input_df)[0])

  return(JSONResponse(
    status_code=200,
    content={
      "message": 'Diabetic' if prediction == 1 else 'Not diabetic' if prediction == 0 else 'Partially diabetic'
    }))
  
  

