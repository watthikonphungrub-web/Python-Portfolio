hostname = "app-prod-01"
ram_usage_percent = 88.0
disk_free_gb = 4.5
if ram_usage_percent > 80.0: 
    print(f"Warning: RAM usage is high on {hostname}: {ram_usage_percent}%")
elif ram_usage_percent < 80.0:
    print(f"RAM usage is normal on {hostname}: {ram_usage_percent}%")
if disk_free_gb < 5.0:
    print(f"Warning: Disk space is low on {hostname}: {disk_free_gb} GB available")
else:
    print(f"Disk space is normal on {hostname}: {disk_free_gb} GB available")