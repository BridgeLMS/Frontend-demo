import requests

BASE_URL = "https://learning-management-api-ce2b.onrender.com/api"

def signup_user():
    """Signs up a new user."""
    url = f"{BASE_URL}/auth/signup"
    user_data = {
        "username": "Johnath",
        "email": "johnath@example.com",
        "password": "Johnath1234565",
        "role": "Learner",
        "phone": "0544122645555",
        "bio": "Maths & English Student"
    }
    try:
        response = requests.post(url, json=user_data)
        response.raise_for_status()  # Raise an exception for bad status codes
        print("Signup successful!")
        print(response.json())
        return True
    except requests.exceptions.RequestException as e:
        print(f"Signup failed: {e}")
        if e.response:
            print(f"Response: {e.response.json()}")
        return False

def login_user():
    """Logs in the user."""
    url = f"{BASE_URL}/auth/login"
    login_data = {
        "email": "johnath@example.com",
        "password": "Johnath1234565"
    }
    try:
        response = requests.post(url, json=login_data)
        response.raise_for_status()
        print("Login successful!")
        print(response.json())
        return True
    except requests.exceptions.RequestException as e:
        print(f"Login failed: {e}")
        if e.response:
            print(f"Response: {e.response.json()}")
        return False

if __name__ == "__main__":
    if signup_user():
        login_user()