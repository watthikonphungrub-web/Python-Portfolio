import requests

endpoints = [
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/invalid-endpoint",
]

for endpoint in endpoints:
    response = requests.get(endpoint)

    if response.status_code == 200:
        print(f"[🟢 UP] {endpoint} is healthy.")
    else:
        print(f"[🔴 DOWN] {endpoint} returned status {response.status_code}\n")

        