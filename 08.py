import streamlit as st


col1, col2 = st.columns([1, 2])  

with col1:
    st.image("Logo.png", width=150) 

with col2:
    st.write("""
    매니저
    밤오반과에네르기파(Makise)
    
    부매니저
    호요인쿄우마(Okabe)
    페이리스냥냥(Shinomiya)
    
    개설일2025-05-16
    """)

if "posts" not in st.session_state:
    st.session_state.posts = []  
if "comments" not in st.session_state:
    st.session_state.comments = {} 
    

menu = st.sidebar.radio("메뉴", ["전체글", "글쓰기"])

st.title("용문고등학교 마이너 갤러리")

if menu == "글쓰기":
    st.subheader("글쓰기")
    nickname = st.text_input("닉네임")
    password = st.text_input("비밀번호", type="password")
    title = st.text_input("제목")
    content = st.text_area("내용")

    if st.button("등록"):
        if nickname and password and title and content:
            post = {"nickname": nickname, "title": title, "content": content}
            st.session_state.posts.append(post)
            st.success("게시글이 작성되었습니다!")
        else:
            st.error("모든 항목을 입력해주세요.")

elif menu == "전체글":
    st.subheader("전체글")
    if not st.session_state.posts:
        st.write("작성된 글이 없습니다.")
    else:
        for i, post in enumerate(st.session_state.posts):
            with st.expander(f"{post['title']} - {post['nickname']}"):
                st.divider()
                st.write(post["content"])
                st.divider()
                st.write("전체 댓글")
                st.divider()
                if i in st.session_state.comments and st.session_state.comments[i]:
                    for c in st.session_state.comments[i]:
                        st.write(f"- {c['nickname']}: {c['content']}")
                else:
                    st.write("댓글이 없습니다.")
                st.divider()    
                st.write("댓글 작성")
                c_nick = st.text_input("닉네임", key=f"nick_{i}")
                c_pwd = st.text_input("비밀번호", type="password", key=f"pwd_{i}")
                c_text = st.text_input("댓글 내용", key=f"text_{i}")

                if st.button("댓글 작성", key=f"submit_{i}"):
                    if c_nick and c_pwd and c_text:
                        comment = {"nickname": c_nick, "content": c_text}
                        if i not in st.session_state.comments:
                            st.session_state.comments[i] = []
                        st.session_state.comments[i].append(comment)
                        st.success("댓글이 작성되었습니다!")
                    else:
                        st.error("모든 항목을 입력해주세요.")
