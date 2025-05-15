import streamlit as st


st.sidebar.image("OASIS.png", caption="OASIS")
st.title("환영합니다 오아시스 공식 사이트입니다")

st.write("")
st.write("")


option = st.sidebar.selectbox(
    "변천사", ["창설", "분열", "재결합"]
)
st.write("")
st.write("")

with st.container():
    st.header("Memebers")

#칼럼
    col1, col2 = st.columns(2)


    with col1:
        st.subheader("Vocal")
        st.image("Liam.png", caption="Liam Gallagher", use_container_width=True)
        st.write("Frontman, vocalist")

    with col2:
        st.subheader("Guitar")
        st.image("Noel.png", caption="Noel Gallagher", use_container_width=True)
        st.write("Leader, main songwriter, sub-vocalist, guitarist")


# 탭
st.write("")
st.write("")


st.header("Hit songs")

tab1, tab2 = st.tabs(["WonderWall", "Don't Look Back In Anger"])

with tab1:
    st.video("WonderWall.mp4")
    st.write("you're gonna be the one that saves me")
    st.write("네가 날 구원해 줄 단 한 사람이니까")
    with st.expander("가사"):
        st.write("Today is gonna be the day")
        st.write("that they're gonna throw it back to you")
        st.write("By now you should've somehow")
        st.write("realized what you gotta do")
        st.write("I don't believe that anybody")
        st.write("feels the way I do about you now")
        st.write("And all the roads we have to walk are winding")
        st.write("And all the lights that lead us there are blinding")
        st.write("There are many things that I would like to say to you")
        st.write("But I don't know how")
        st.write("Because maybe")
        st.write("You're gonna be the one that saves me")
        st.write("And after all")
        st.write("You're my wonderwall")

with tab2:
    st.video("Dont Look Back In Anger.mp4")
    st.write("Step outside, 'cause summertime's in bloom")
    st.write("밖으로 나와 봐, 화창한 여름날이야")
    with st.expander("가사"):
        st.write("Slip inside the eye of your mind")
        st.write("Don't you know you might find")
        st.write("A better place to play")
        st.write("You said that you'd never been")
        st.write("But all the things that you see")
        st.write("Slowly fade away")
        st.write("So I start a revolution from my bed")
        st.write("'Cause you said the brains I had went to my head")
        st.write("Step outside, 'cause summertime's in bloom")
        st.write("Stand up beside the fireplace")
        st.write("Take that look from off your face")
        st.write("You ain't ever gonna burn my heart out")
        st.write("And so Sally can wait")
        st.write("She knows it's too late as we're walking on by")
        st.write("Her soul slides away")
        st.write("But don't look back in anger")
        st.write("I heard you say")
        st.write("At least not today")
    
st.write("")
st.write("")

# 익스펜더
with st.expander("Live at Knebworth"):
    st.image("Knebworth.png", caption="Live at knebworth")
    st.write("1996년 8월 10일, 11일 이틀에 걸쳐 영국 잉글랜드 헤리포드셔주 케네스워스에서 열린 공연")
    st.write("더 많은 정보를 원하신다면 나무위키를 방문해주세요")
    st.write("https://namu.wiki/w/오아시스(밴드)")
    
st.write("")
st.write("")

# 페이지 이동 처리
if option == "창설":
    st.image("CHANG.png", caption="홈 페이지 이미지")
    st.write("창설 직후 사진입니다. 이때는 리암과 노엘이 함께 했습니다.")
elif option == "분열":
    st.image("BEADY.png", caption="분열 후 이미지")
    st.write("분열 후 비디아이로 활동하는 리암의 모습입니다")
elif option == "재결합":
    st.image("OASISJAE.png", caption="재결합 후 이미지")
    st.write("재결합 이거 진짜에요? 한국에서도 공연하니까 예매 ㄱㄱ")
    
st.write("")
st.write("")

st.header("마지막으로 이 노래를 듣고 가세요 4분 20초부터가 진짜 개맛도리입니다 아이드라잌투비언더더씨인어옥포퍼시스가든인더쉐읻우두라잌투비언더더시인어옥토퍼시스가든유앤미")
st.subheader("이 노래는 오아시스의 'Whatever'입니다")
st.video("Whatever.mp4")
