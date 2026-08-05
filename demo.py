import pandas as pd

# สร้างข้อมูล demo
bkk = pd.DataFrame({
    "Date": ["2026-08-01", "2026-08-01", "2026-08-02"],
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Price": [25000, 500, 1200],
    "Quantity": [1, 2, 1]
})

cnx = pd.DataFrame({
    "Date": ["2026-08-01", "2026-08-01", "2026-08-02"],
    "Product": ["Monitor", "Mouse", "Headset"],
    "Price": [4500, 500, 1500],
    "Quantity": [1, 3, 2]
})

pkt = pd.DataFrame({
    "Date": ["2026-08-01", "2026-08-02", None],
    "Product": ["Laptop", "Mouse", None],
    "Price": [25000, 500, None],
    "Quantity": [2, 1, None]
})

# เซฟออกเป็นไฟล์ CSV ให้ทันทีในโฟลเดอร์เดียวกัน
bkk.to_csv("sales_bangkok.csv", index=False)
cnx.to_csv("sales_chiangmai.csv", index=False)
pkt.to_csv("sales_phuket.csv", index=False)

print("✨ สร้างไฟล์ CSV ทั้ง 3 ไฟล์ในเครื่องให้แล้วเรียบร้อยครับ!")