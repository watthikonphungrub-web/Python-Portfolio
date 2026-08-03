def evaluate_cpu(cpu_pct):
    cpu_pct = float(cpu_pct)
    if cpu_pct > 85:
        return "CRITICAL"
    elif cpu_pct > 70:
        return "WARNING"
    else:
     return "OK"
def evaluate_ram(ram_pct):
    ram_pct = float(ram_pct)
    if ram_pct > 90:
        return "CRITICAL"
    elif ram_pct > 75:
        return "WARNING"
    else:
     return "OK"

server = [{"hostname": "app-01", "cpu": 92.0, "ram": 60.0},
    {"hostname": "app-02", "cpu": 45.0, "ram": 80.000}]

for server in server:
    cpu_pct = server["cpu"]
    ram_pct = server["ram"]
    
    cpu_status = evaluate_cpu(cpu_pct)
    ram_status = evaluate_ram(ram_pct)
    
    print(f"{ server['hostname'] } CPU Status: {cpu_status}, RAM Status: {ram_status}")