import streamlit as st
import pandas as pd
from PIL import Image

image1 = Image.open("example.jpg") 
st.image(image1, caption="예제 이미지")

st.audio("example.mp3")

st.video("example.mp4")

data = {
    "이름": ["호날두", "메시", "아자르", "김철수"],
    "나이": [30, 55, 35, 23],
    "거주지": ["사우디", "미국", "벨기에", "서울"]
}
df = pd.DataFrame(data)

st.write("데이터 출력:")
st.write(df)

st.write("JSON 출력:")
st.json({
    "이름": "김철수",
    "나이": 25,
    "거주지": "평양"
})

st.write("metric 출력:")
st.metric(label="카이저코퍼레이션", value="78,000원", delta="2.12%")
st.metric(label="하이렌더", value="150,000원", delta="-1.25%")
