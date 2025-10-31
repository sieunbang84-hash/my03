import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="주민등록 인구 및 세대 현황", layout="wide")

st.title("📈 주민등록 인구 및 세대 현황 (2025년 9월)")
st.write("행정구역별 인구와 세대 현황 데이터를 Plotly로 시각화합니다.")

# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type=["csv"])

if uploaded_file is not None:
    # CSV 읽기 (자동 인코딩 감지)
    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(uploaded_file, encoding="euc-kr")

    # 수치형 데이터 전처리
    for col in df.columns:
        if "인구수" in col or "세대수" in col:
            df[col] = df[col].astype(str).str.replace(",", "").astype(float)

    # 행정구역명 정리
    df["행정구역"] = df["행정구역"].str.replace(r"\(.*\)", "", regex=True).str.strip()

    st.subheader("데이터 미리보기")
    st.dataframe(df.head())

    # --------------------
    # 시각화 1: 지역별 총인구수
    # --------------------
    st.subheader("📍 행정구역별 총인구수")
    fig_pop = px.bar(
        df.sort_values(by=df.columns[1], ascending=False).head(20),
        x="행정구역",
        y=df.columns[1],
        title="상위 20개 행정구역 총인구수",
        color="행정구역"
    )
    st.plotly_chart(fig_pop, use_container_width=True)

    # --------------------
    # 시각화 2: 남녀 인구 비율 비교
    # --------------------
    st.subheader("👫 남녀 인구 비교")
    gender_cols = [col for col in df.columns if "남자 인구수" in col or "여자 인구수" in col]
    if len(gender_cols) == 2:
        df_gender = df.melt(id_vars=["행정구역"], value_vars=gender_cols, var_name="성별", value_name="인구수")
        fig_gender = px.bar(
            df_gender,
            x="행정구역",
            y="인구수",
            color="성별",
            title="행정구역별 남녀 인구 비교",
            barmode="group"
        )
        st.plotly_chart(fig_gender, use_container_width=True)

    # --------------------
    # 시각화 3: 총인구수 vs 세대수
    # --------------------
    st.subheader("🏠 총인구수 대비 세대수 관계")
    fig_scatter = px.scatter(
        df,
        x=df.columns[2],  # 세대수
        y=df.columns[1],  # 총인구수
        hover_name="행정구역",
        title="세대수와 총인구수의 상관관계"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

else:
    st.info("좌측 상단에서 CSV 파일을 업로드해주세요.")

st.caption("데이터 출처: 행정안전부 주민등록 인구 및 세대 현황 (2025년 9월 기준)")
