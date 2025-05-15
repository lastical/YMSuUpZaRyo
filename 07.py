import streamlit as st


if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

if not st.session_state.button_clicked:
    st.title("""용팡에 오신 것을 환영합니다. 
             접속하기 버튼을 눌러 시작하세요!""")
    if st.button("접속하기"):
        st.session_state.button_clicked = True 

if st.session_state.button_clicked:
    products = [
        {"name": "전화렌지(가칭)", "price": 199900, "image": "GADGET9.png"},
        {"name": "키친 건", "price": 399900, "image": "KITCHEN.png"},
        {"name": "비트 입자포", "price": 129900, "image": "GADGET1.png"},
        {"name": "돼지국밥정식", "price": 12900, "image": "GUK.png"},
        {"name": "페로로 인형", "price": 9900, "image": "PERORO.png"},
    ]

    if "cart" not in st.session_state:
        st.session_state.cart = []

    st.sidebar.image("Logo.png", width=150)
    st.sidebar.write("환영합니다! 쇼핑을 즐기세요.")

    menu = st.sidebar.radio("메뉴 선택", ["상품 목록", "장바구니", "결제"])

    st.title("Yongpang Shopping Mall")

    if menu == "상품 목록":
        st.subheader("상품 목록")
        for product in products:
            st.image(product["image"], width=250)
            st.write(f'{product["name"]} - {product["price"]}원')
            if st.button(f"{product['name']} 장바구니에 추가"):
                st.session_state.cart.append(product)
                st.success(f"{product['name']}을(를) 장바구니에 추가했습니다!")

    elif menu == "장바구니":
        st.subheader("장바구니")
        if st.session_state.cart:
            for item in st.session_state.cart:
                st.image(item["image"], width=100)
                st.write(f'{item["name"]} - {item["price"]}원')
            if st.button("구매하기"):
                st.error("구매하기 버튼은 아직 구현되지 않았습니다.")
                st.write("구매를 위해서 결제 페이지로 이동하세요.")
        else:
            st.write("장바구니가 비어 있어요.")

    elif menu == "결제":
        st.subheader("결제")
        if st.session_state.cart:
            st.write("상품 목록:")
            for item in st.session_state.cart:
                st.image(item["image"], width=100) 
                st.write(f'{item["name"]} - {item["price"]}원')

            name = st.text_input("이름을 입력하세요")
            address = st.text_area("배송 주소를 입력하세요")
            phone = st.text_input("연락처를 입력하세요")

            if st.button("결제 완료"):
                if name and address and phone:
                    st.session_state.cart = [] 
                    st.success(f"결제가 완료되었습니다! 이름: {name} 주소: {address} 연락처: {phone}")
                else:
                    st.error("모든 정보를 입력하세요.")
        else:
            st.warning("결제할 상품이 없습니다. 먼저 장바구니에 추가하세요.")