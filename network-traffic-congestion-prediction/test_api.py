import requests

sample_input = {
    "data": [12.5, 7.4, 0.02, 5.6, 0.01, 0.03, 0.005, 64240, 1.23, 0.006,
             0.001, 0.007, 32, 0.009, 2, 5, 0.01, 0.02, 0.025, 1460]
}

response = requests.post("http://127.0.0.1:8000/predict", json=sample_input)
print(response.json())
