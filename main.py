my_app/
├─ main.py
└─ pages/
   ├─ 1_📍_총인구수_시각화.py
   ├─ 2_👫_남녀_인구_비교.py
   ├─ 3_🏠_세대수_대비_총인구수.py
import streamlit as st

st.set_page_config(page_title="데이터 분석 앱", page_icon="📊")

st.title("📊 데이터 분석 앱에 오신 걸 환영합니다!")
st.write("왼쪽 메뉴에서 페이지를 선택하세요.")
