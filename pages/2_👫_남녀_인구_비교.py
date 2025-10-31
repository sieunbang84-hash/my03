import streamlit as st
import pandas as pd
import plotly.express as px

st.title("👫 남녀 인구 비교")

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

        gender_cols = [col for col in df.columns if "남자 인구수" in col or "여자 인구수" in col]
        if len(gender_cols) == 2:
            df_gender = df.melt(id_vars=["행정구역"], value_vars=gender_cols, var_name="성별", value_name="인구수")
            fig = px.bar(
                df_gender,
                x="행정구역",
                y="인구수",
                color="성별",
                barmode="group",
                title="행정구역별 남녀 인구 비교"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("남자 인구수 / 여자 인구수 컬럼을 찾을 수 없습니다.")

    except Exception as e:
        st.error(f"파일을 불러오는 중 오류 발생: {e}")
else:
    st.info("좌측 사이드바에서 CSV 파일을 업로드하세요.")
