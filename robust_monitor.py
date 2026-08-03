import requests

endpoints = [
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/invalid-endpoint",
    "https://this-site-is-fake-12345.com"
]

for endpoint in endpoints:
    try:
        response = requests.get(endpoint, timeout=5)
        if response.status_code == 200:
            print(f"[🟢 UP] {endpoint} is healthy.")
        else:
            print(f"[🔴 DOWN] {endpoint} returned status {response.status_code}\n")
    
    except requests.exceptions.RequestException as e:
        print(f"[CRITICAL] Failed to reach {endpoint}. Reason: {e}")



