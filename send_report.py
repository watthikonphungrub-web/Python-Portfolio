import requests
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_URL = os.getenv("DISCORD_URL")

file_path = "total_sales_report.xlsx"

with open(file_path, "rb") as file:
    files = {"file": (file_path, file)}
    response = requests.post(DISCORD_URL,files=files)
    
    if response.status_code == 200:
        print(f"File '{file_path}' sent to Discord successfully.")
    else:
        print(f"Failed to send file '{file_path}' to Discord. Status code: {response.status_code}")