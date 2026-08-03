import subprocess
servers = ["8.8.8.8", "1.1.1.1", "192.0.2.1"]
for ip in servers:
    result = subprocess.run(["ping", "-c", "1", "-w", "2", ip], capture_output=True, text=True, timeout=10)
    if result.returncode == 0:
        print(f"{ip} is connected.")
    else:
        print(f"{ip} is not connected.")

