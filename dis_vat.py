import streamlit as fr
fr.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")
price = fr.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0, value=0.0)
dis = fr.number_input("กรอกเปอร์เซ็นส่วนลด (%):", min_value=0.0, max_value=100.0, value=0.0)
f_dis = price * (dis / 100)
f_price = price - f_dis
vat = f_price * 0.07
net = f_price + vat
fr.write(f"• ส่วนลด ({dis:.0f}%): **{f_dis:.2f}** บาท")
fr.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
fr.title(f"• ราคาสุทธิ: {net:.2f} บาท")
fr.divider()
fr.write("นายอนาวิล คำมะนิจ เลขที่ 31 ม.4/5")
