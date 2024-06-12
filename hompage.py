import streamlit as st
import globalData as gData

def app():

    # Custom CSS to align elements at the bottom
    st.markdown("""
        <style>
        .bottom-align {
            display: flex;
            justify-content: flex-start;
            align-items: flex-end;
        }
        .bottom-align > div {
            flex: 1;
        }
        </style>
    """, unsafe_allow_html=True)

    image_url = "https://i.imgur.com/7cBH3fu.png "
    st.image(image_url)
    # 페이지 레이아웃 설정
    col1, col2 = st.columns([3, 1])


    # Custom container for bottom alignment
    with col1:
        st.markdown('<div class="bottom-align">', unsafe_allow_html=True)
        userName = st.text_input("이름을 입력해주세요.", key="name_input", help="여기에 이름을 입력하세요.")
        st.markdown('</div>', unsafe_allow_html=True)
        gData.set_name(userName)

    # Check if userName is empty or null
    if userName:
        button_disabled = False
    else:
        button_disabled = True
        

    with col2:
        st.markdown('<div class="bottom-align">', unsafe_allow_html=True)
        button_clicked = st.button("재료 입력하러 가기", disabled = button_disabled)
        st.markdown('</div>', unsafe_allow_html=True)

    # 버튼이 클릭되었을 때 동작
    if button_clicked:
        st.session_state.page = 'test'
        