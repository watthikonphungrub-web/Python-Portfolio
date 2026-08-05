import pandas as pd

print("✨ เริ่มรวมไฟล์ CSV ทั้ง 3 ไฟล์เข้าด้วยกัน...")

# อ่านไฟล์ CSV ทั้ง 3 ไฟล์
bkk = pd.read_csv("sales_bangkok.csv")
cnx = pd.read_csv("sales_chiangmai.csv")
pkt = pd.read_csv("sales_phuket.csv")

# รวม DataFrame ทั้ง 3 เข้าด้วยกัน
combined_df = pd.concat([bkk, cnx, pkt],ignore_index=True)
# เซฟออกเป็นไฟล์ Excel ใหม่
combined_df.to_excel("total_sales_report.xlsx", index=False)
print("✨ รวมไฟล์ CSV ทั้ง 3 ไฟล์เรียบร้อยแล้ว! ไฟล์ใหม่ชื่อ 'total_sales_report.xlsx' ถูกสร้างขึ้นในเครื่องของคุณเรียบร้อยครับ")
