import requests

url = "http://localhost:5000/predict_api"
r = requests.post(url, json={'carat': 0.23, 'cut': 1, 'color': 1, 'clarity': 8, 'depth': 61.5, 'table': 55.0, 'volume': 38.2})

print(r.json())