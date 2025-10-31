import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="주민등록 인구 및 세대 현황 시각화", layout="wide")

st.title("📊 주민등록 인구 및 세대 현황 시각화")
st.write("이 대시보드는 주민등록 인구 및 세대 데이터를 기반으로 Plotly를 사용해 시각화합니다.")

# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding="utf-8")
    st.subheader("데이터 미리보기")
    st.dataframe(df.head())

    # 컬럼 확인
    st.write("컬럼 목록:", list(df.columns))

    # 시각화 옵션 선택
    st.sidebar.header("시각화 옵션")
    x_col = st.sidebar.selectbox("X축 컬럼 선택", df.columns)
    y_col = st.sidebar.selectbox("Y축 컬럼 선택", df.columns)
    chart_type = st.sidebar.selectbox("그래프 유형 선택", ["막대그래프", "선그래프", "산점도"])

    st.subheader("시각화 결과")

    if chart_type == "막대그래프":
        fig = px.bar(df, x=x_col, y=y_col, color=x_col, title=f"{x_col}별 {y_col}")
    elif chart_type == "선그래프":
        fig = px.line(df, x=x_col, y=y_col, title=f"{x_col}별 {y_col} 추이")
    else:
        fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("좌측 상단에서 CSV 파일을 업로드해주세요.")

---

### 🪄 실행 방법

1. **requirements.txt** 파일 생성  
   ```
   streamlit
   plotly
   pandas
   ```

2. **로컬 실행**
   ```bash
   streamlit run app.py
   ```

3. **GitHub 업로드**
   - 위 `app.py`와 `requirements.txt`를 깃허브 저장소에 업로드
   - (원하면 Streamlit Cloud에서 배포 가능)
