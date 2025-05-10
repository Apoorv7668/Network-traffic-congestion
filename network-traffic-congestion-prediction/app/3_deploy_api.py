from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import logging
import os

# Enable logging
logging.basicConfig(level=logging.INFO)

# Setup
app = FastAPI()

class TrafficData(BaseModel):
    data: list

# Load model files (from notebooks folder inside Docker)
model = joblib.load("notebooks/rf_model.pkl")
scaler = joblib.load("notebooks/scaler.pkl")
features = joblib.load("notebooks/features.pkl")

@app.get("/")
def root():
    return {"message": "Network Congestion Prediction API is running "}

@app.post("/predict")
def predict_congestion(payload: TrafficData):
    if len(payload.data) != len(features):
        return {"error": f"Expected {len(features)} features, got {len(payload.data)}"}

    logging.info(f"Received data: {payload.data}")

    input_array = np.array(payload.data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)

    return {
        "congested": int(prediction[0]),
        "message": "1 = Congested, 0 = Not Congested"
    }
