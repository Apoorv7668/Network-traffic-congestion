# Network Traffic Congestion Prediction

This project aims to predict **network traffic congestion** using IP flow data with 87 application-level attributes. It's tailored for a **cybersecurity context**, helping to identify congested network flows which could indicate potential threats such as DoS attacks or abnormal usage patterns.

---

## Problem Statement

The goal is to build a machine learning model that can predict whether a given network traffic flow is **congested** or **not congested**, using behavioral flow-level features. Congested flows often signify abnormal patterns that are useful in cybersecurity monitoring and response.

---

## Dataset

- **Name**: IP Network Traffic Flows Labeled with 87 Apps
- **Source**: [University of Cauca / Kaggle]
- **Samples Used**: 200,000 rows (subset)
- **Labeling**: Congestion was defined based on the 90th percentile of `Flow.Packets.s`.

---

## Exploratory Data Analysis (EDA)

- Dropped identifier columns: `Flow.ID`, `Source.IP`, etc.
- Handled missing values
- Visualized:
  - Packet and byte distribution
  - Congestion by protocol
  - Feature correlation heatmap
- Created `Congested` label from `Flow.Packets.s` threshold

---

## Preprocessing

- Removed leakage (`Flow.Packets.s`) after using it to define label
- Feature selection via Random Forest importance and correlation
- Scaled features using `StandardScaler`
- Removed low-variance and highly correlated redundant features
- Balanced performance evaluation with confusion matrix

---

## Model

- Model: `RandomForestClassifier`
- Accuracy (after removing leakage): **~99.99%**
- Evaluation: Precision, Recall, F1, Confusion Matrix
- Cross-validation (5-fold): Confirmed generalization

---

## Cybersecurity Tie-In

- Analyzed `Protocol` and `Destination.Port` against congestion label
- Insights reflect that certain application ports/protocols tend to show higher congestion, useful for anomaly detection and threat monitoring.

---

## Deployment

- Built a REST API using **FastAPI**
- Exposes:
  - `GET /` → Health check
  - `POST /predict` → Predict congestion from flow features
- Input: List of selected flow features
- Output: Congestion class (0 or 1)

---

## Docker Setup

### Requirements
- Docker
- Python 3.10 (for local testing)

### Build
```bash
docker build -t congestion-api .
```

### Run
```bash
docker run -p 8000:8000 congestion-api
```

### API Test (via Swagger UI)
Navigate to: `http://localhost:8000/docs`

---

## Project Structure

```
.
├── app/
│   └── 3_deploy_api.py         # FastAPI app
├── data/
│   └── Dataset-Unicauca-...csv # Raw dataset
├── notebooks/
│   ├── eda.ipynb               # EDA + training notebook
│   ├── rf_model.pkl            # Trained model
│   ├── scaler.pkl              # Scaler used for training
│   └── features.pkl            # Feature list
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ✅ Future Improvements

- Add real-time streaming support (Kafka)
- Extend model to detect attack patterns (DoS, scanning)
- Monitor via Prometheus/Grafana with live alerts

