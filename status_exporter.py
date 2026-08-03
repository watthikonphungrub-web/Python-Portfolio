import json

cluster_data_json = '''
{
    "environment": "production",
    "services": [
        {"name": "web-gateway", "status": "running", "port": 80},
        {"name": "auth-service", "status": "stopped", "port": 4000},
        {"name": "payment-api", "status": "running", "port": 5000},
        {"name": "database-cluster", "status": "stopped", "port": 5432}
    ]
}
'''
cluster_data = json.loads(cluster_data_json)

print("=== PRODUCTION CLUSTER HEALTH REPORT ===")

failed_services = []

for service in cluster_data["services"]:
    name = service.get("name")
    status = service.get("status")
    port = service.get("port")

    if status == "stopped":
        failed_services.append(name)
        print(f"[ALERT] CRITICAL {name} is stopped on port {port}!")
    elif status == "running":
        print(f"[OK] {name} is listening on port {port}.")
    else:
        print(f"[ALERT] Service {name} has an unknown status on port {port}.")
with open("alert_summary.json","w") as f:
    json.dump({"failed_services": failed_services}, f)

