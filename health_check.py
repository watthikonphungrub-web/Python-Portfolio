hostname = "web-port-01"
total_mem_gb = 16
used_mem_gb = 8
mem_usage_pct = (used_mem_gb / total_mem_gb) * 100
print(f"Memory usage for {hostname}: {mem_usage_pct:.2f}%")