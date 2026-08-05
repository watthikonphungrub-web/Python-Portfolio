import requests

webhook_url = "https://httpbin.org/post"

alert_payload = {
    "server_name": "Linux-DB-01",
    "alert_type": "CRITICAL_DISK_SPACE",    
    "details": "Root partition / has reached 85% capacity!",
    "timestamp": "2026-08-04 09:45:00",
}

response = requests.post(webhook_url, json=alert_payload)

print(f"Webhook response status code: {response.status_code}")