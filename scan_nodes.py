nodes = [
 {"hostname": "node1", "status": "online", "latency_ms": 12},
 {"hostname": "node2", "status": "offline", "latency_ms": 0},
 {"hostname": "node3", "status": "online", "latency_ms": 150}
]
for node in nodes :
    hostname = node["hostname"]
    status = node["status"]
    latency_ms = node["latency_ms"]
    
    if status == "online":
        print(f"{hostname} [CRITICAL] {hostname} is OFFLINE! {latency_ms} ms.")
    elif status == "offline":
        print(f"{hostname} is offline.")
    elif status == "online" and latency_ms > 100:
        print(f"{hostname} is [WARNING] {hostname} High Latency: {latency_ms} ms.")
    else:
        print(f"{hostname} has an unknown status.")