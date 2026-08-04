import subprocess
import requests
import os
from dotenv import load_dotenv

load_dotenv()



result = subprocess.run(["df", "-h","/"], capture_output=True, text=True)
output = result.stdout.strip().strip()

data_lines = output.split('\n')
data_columns = data_lines[1].split()
used_percentage = data_columns[4]
used_percentage_value = int(used_percentage.strip('%'))

DISCORD_URL = os.getenv("DISCORD_URL")
ALERT_THRESHOLD = 20

if used_percentage_value > ALERT_THRESHOLD:
    message = f"[CRITICAL]: Disk usage is at {used_percentage}."
    payload = {"content": message}
    response = requests.post(DISCORD_URL, json=payload)
    if response.status_code == 204:
        print("Alert sent to Discord successfully.")
    else:
        print(f"Failed to send alert to Discord. Status code: {response.status_code}")
else:
    print(f"[OK]: Disk usage is at {used_percentage}. No alert sent.")



