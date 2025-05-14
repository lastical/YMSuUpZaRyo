import streamlit as st
import random

st.title("가위바위보 게임")
st.write("가위, 바위, 보 중 하나를 선택하세요")

user_choice = st.radio("당신의 선택:", ["가위", "바위", "보"])

if st.button("게임 시작!"):
    choices = ["가위", "바위", "보"]
    ai_choice = random.choice(choices)

    st.write(f"AI의 선택: {ai_choice}")

    if user_choice == ai_choice:
        st.info("비겼습니다")
    elif (user_choice == "가위" and ai_choice == "보") or \
         (user_choice == "바위" and ai_choice == "가위") or \
         (user_choice == "보" and ai_choice == "바위"):
        st.success("당신이 이겼습니다")
    else:
        st.error("AI가 이겼습니다")
