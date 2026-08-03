import requests
import datetime
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
            from datetime import datetime
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_message = f"[🔴 DOWN] {endpoint} returned status {response.status_code} at {now}\n"

    except requests.exceptions.RequestException as e:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"[CRITICAL] Failed to reach {endpoint} at {now}. Reason: {e}\n"
        print(error_message)
with open("endpoint_status.log", "a") as log_file:
    log_file.write(error_message)
