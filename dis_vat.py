import streamlit as fr
fr.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")
price = fr.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
dis = fr.number_input("กรอกเปอร์เซ็นส่วนลด (%):", min_value=0.0 , value=0.0)
vat = price * 0.07
f_dis = price (dis/100)
net = price - (f_dis + vat)
f_price = price - f_dis
fr.header(f"• ส่วนลด (1%): **{f_dis:.2f}** บาท")
fr.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
fr.title(f"• ราคาสุทธิ: {net:.2f} บาท")
fr.divider()
fr.write("นายอนาวิล คำมะนิจ เลขที่ 31  ม.4/5")
