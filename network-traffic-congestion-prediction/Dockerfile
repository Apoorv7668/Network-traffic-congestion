FROM python:3.10-slim

WORKDIR /app

# Copy API and model files (preserve subfolders)
COPY app/3_deploy_api.py .
COPY notebooks/rf_model.pkl notebooks/
COPY notebooks/scaler.pkl notebooks/
COPY notebooks/features.pkl notebooks/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "3_deploy_api:app", "--host", "0.0.0.0", "--port", "8000"]
