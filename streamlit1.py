import streamlit as st
st.title("Giới thiệu bản thân")
name = st.text_input("Họ và tên")
date = st.text_input("Ngày tháng năm sinh")
subject = st.text_input("Môn học yêu thích")
hobby = st.text_input("Sở thích")
submit = st.button("Xác nhận")
if submit:
    st.write(f"Họ và tên: {name}")
    st.write(f"Ngày tháng năm sinh: {date}")
    st.write(f"Môn học yêu thích: {subject}")
    st.write(f"Sở thích: {hobby}")