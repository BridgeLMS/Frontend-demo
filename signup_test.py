import requests
import json

url = "https://learning-management-api-ce2b.onrender.com/auth/signup"

payload = {
    "username": "John",
    "email": "john.math@example.com",
    "password": "John1234565",
    "role": "Learner",
    "phone": "0544122605",
    "bio": "Maths Student"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.status_code)
print(response.json())
