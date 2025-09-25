import requests

url = "http://localhost:5000/"
data = {"cpu": 95}   

response = requests.post(url, json=data)

print(f"Sent alert: {data}, Response: {response.status_code} {response.text}")
