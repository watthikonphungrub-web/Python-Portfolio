import json

# ข้อมูล JSON จำลองสถานะ Services จากเซิร์ฟเวอร์
services_json = '''
[
    {"name": "nginx", "status": "running"},
    {"name": "mysql", "status": "stopped"},
    {"name": "redis", "status": "running"}
]
'''
services_data = json.loads(services_json)
for service in services_data:
    name = service["name"]
    status = service["status"]
    
    if status == "stopped":
        print(f"[ALERT] Service {name} is stopped!")
    elif status == "running":
        print(f"Service {name} is running.")
    else:
        print(f"[ALERT] Service {name} has an unknown status.")
