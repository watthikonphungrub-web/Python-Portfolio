import requests

# ยิง GET Request ไปขอข้อมูลจาก API
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# ตรวจสอบว่าสำเร็จหรือไม่
if response.status_code == 200: 
    data = response.json()
    print("✅ Connected to JSONPlaceholder API Successfully!")

    name = data.get("name")
    email = data.get("email")
    print(f"User Name: {name}")
    print(f"User Email: {email}")

else:
    print(f"❌ [ERROR] Cannot connect to API {response.status_code}")
