from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
app = FastAPI(title="COMPUTATONALTHINKING")
sentiment_model = pipeline("sentiment-analysis" , model="distilbert-base-uncased-finetuned-sst-2-english")
class TextInput(BaseModel):
    text: str
@app.get("/") 
def home():
    return{
        "message": "Welcome to my work",
        "usage": "Send a POST request to /predict with your text"
    }
@app.get("/health")
def health():
    return {"status": "healthy"}
@app.post("/predict")
def predict(input_data: TextInput):
    if not input_data.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty"
        )
    try:
        result = sentiment_model(input_data.text)

        return {
            "text": input_data.text,
            "sentiment": result[0]["label"],
            "score": result[0]["score"]
        }
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred"
        ) from error 