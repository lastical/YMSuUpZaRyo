import streamlit as st

st.title("Streamlit 입력 예제")

name = st.text_input("이름을 입력하세요")
st.write("입력된 이름:", name)

age = st.number_input("나이를 입력하세요", min_value=0, max_value=100, step=2)
st.write("입력된 나이:", age)

selected_date = st.date_input("날짜 선택")
st.write("선택한 날짜:", selected_date)

selected_time = st.time_input("시간 선택")
st.write("선택한 시간: ", selected_time)

selected_option = st.selectbox("옵션을 선택하세요", ["옵션 1", "옵션 2", "옵션 3"])
st.write("선택된 옵션:", selected_option)

message = st.text_area("메시지를 입력하세요")
st.write("입력된 메시지:")
st.text(message)  
    
uploaded_file = st.file_uploader("이미지를 업로드하세요")
if uploaded_file is not None:
    st.image(uploaded_file, caption="업로드된 이미지")

color = st.color_picker("색상을 선택하세요", "#00f900")
st.write("선택한 색상:", color)