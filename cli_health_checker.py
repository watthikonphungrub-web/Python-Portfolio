servers = [
{
    "hostname": "app-01",
    "ip_address": "192.168.1.10",
    "cpu_usage_percent": 90.0,
    "ram_usage_percent": 85.0,
    "disk_free_gb": 3.0,
    "status": "200 OK"
}    
        ]
def check_server_health(server):
    hostname = server.get("hostname", "Unknown Hostname")
    ip_address = server.get("ip_address", "Unknown IP Address")
    cpu_usage_percent = server.get("cpu_usage_percent", 0.0)
    ram_usage_percent = server.get("ram_usage_percent", 0.0)
    disk_free_gb = server.get("disk_free_gb", 0.0)
    status = server.get("status", "Unknown Status")

    print(f"Checking health for {hostname} ({ip_address})")
    
    if cpu_usage_percent > 85:
        cpu_stat = "CRITICAL"
    else:
         cpu_stat = "OK"

    if ram_usage_percent > 80:
        ram_stat = "CRITICAL"
    else:
        ram_stat = "OK"

    if disk_free_gb < 5:
        disk_stat = "CRITICAL"
    else:
        disk_stat = "OK"    
    return f"CPU: {cpu_stat} ({cpu_usage_percent}%), RAM: {ram_stat} ({ram_usage_percent}%), Disk: {disk_stat} ({disk_free_gb} GB)"

for server in servers:
        health_status = check_server_health(server)
        print(f"Health status for {server['hostname']}: {health_status}") 
