import pandas as pd

# ไฟล์ที่ 1: เซลล์ A (มีข้อมูลซ้ำ)
data_a = pd.DataFrame({
    "Date": ["2026-08-01", "2026-08-01", "2026-08-02"],
    "Sales_Name": ["Somchai", "Somchai", "Somchai"],
    "Product": ["Mouse", "Mouse", "Keyboard"],
    "Price": [500, 500, 1200],
    "Quantity": [2, 2, 1]
})

# ไฟล์ที่ 2: เซลล์ B (มีแถวที่ Price เป็นค่าว่าง)
data_b = pd.DataFrame({
    "Date": ["2026-08-01", "2026-08-02", "2026-08-02"],
    "Sales_Name": ["Somsri", "Somsri", "Somsri"],
    "Product": ["Monitor", "Headset", "Unknown"],
    "Price": [4500, 1500, None],
    "Quantity": [1, 2, 1]
})

# ไฟล์ที่ 3: เซลล์ C
data_c = pd.DataFrame({
    "Date": ["2026-08-01", "2026-08-02"],
    "Sales_Name": ["Somsak", "Somsak"],
    "Product": ["Laptop", "Mouse"],
    "Price": [25000, 500],
    "Quantity": [1, 3]
})

data_a.to_csv("daily_report_somchai.csv", index=False)
data_b.to_csv("daily_report_somsri.csv", index=False)
data_c.to_csv("daily_report_somsak.csv", index=False)

print("✨ สร้างไฟล์ข้อมูลสำหรับทดสอบเรียบร้อยแล้ว!")