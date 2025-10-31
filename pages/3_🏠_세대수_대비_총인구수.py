import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏠 세대수 대비 총인구수 관계")

uploaded_file = st.sidebar.file_uploader("CSV 파일을 업로드하세요.", type=["csv"])

if uploaded_file is not None:
    try:
        try:
            df = pd.read_csv(uploaded_file, encoding="utf-8")
        except UnicodeDecodeError:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, encoding="euc-kr")

        for col in df.columns:
            if "인구수" in col or "세대수" in col:
                df[col] = df[col].astype(str).str.replace(",", "").astype(float)
        df["행정구역"] = df["행정구역"].str.replace(r"\(.*\)", "", regex=True).str.strip()

        fig = px.scatter(
            df,
            x=df.columns[2],
            y=df.columns[1],
            hover_name="행정구역",
            title="세대수와 총인구수의 상관관계"
        )
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"파일을 불러오는 중 오류 발생: {e}")
else:
    st.info("좌측 사이드바에서 CSV 파일을 업로드하세요.")
