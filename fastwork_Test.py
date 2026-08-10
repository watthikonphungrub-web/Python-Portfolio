import glob
import os
import pandas as pd
#ดึงรายชื่อไฟล์ CSV ทั้งหมด
csv_files = glob.glob("daily_report_*.csv")
#สร้าง List มารอรับ DataFrame (วิธีนี้ Clean และนิยมที่สุดใน Pandas)
all_dfs = []
#วนลูปอ่านข้อมูลทีละไฟล์
for file in csv_files:
    df = pd.read_csv(file)
    all_dfs.append(df)
#รวมข้อมูลทุกไฟล์เข้าด้วยกัน (ทำนอกลูป หลังอ่านครบหมดแล้ว)
combined_df = pd.concat(all_dfs, ignore_index=True)


#ทำ data cleaning โดยลบคอลัมน์ที่ไม่จำเป็นออกไป

#ลบข้อมูลซ้ำ
cleaned_df = combined_df.drop_duplicates(
    subset=["Date","Sales_Name","Product"], keep="first"
)

#ลบแถวที่ Price เป็นค่าว่าง (NaN)
cleaned_df = cleaned_df.dropna(subset=["Price"])

#คำนวณคอลัมน์ Total_Sales
cleaned_df["Total_Sales"] = cleaned_df["Price"] * cleaned_df["Quantity"]

#บันทึกผลลัพธ์เป็นไฟล์ Excel
try:
    output_file = "summary_report.xlsx"
    cleaned_df.to_excel(output_file, index=False)
    print(f"✨ รวมไฟล์ CSV ทั้งหมดเรียบร้อยแล้ว! สร้างไฟล์ '{output_file}' สำเร็จครับ")
except Exception as e:
    print(f"❌ เกิดข้อผิดพลาดในการบันทึกไฟล์ Excel: {e}")
