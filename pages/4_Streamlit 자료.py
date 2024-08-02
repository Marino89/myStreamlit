import streamlit as st

st.set_page_config(
    page_title="Streamlit 관련 사이트",
    page_icon="🙋",
)

st.write("# 더 알고싶다면 📚")

st.sidebar.success("관련 사이트")

st.markdown(
    """
    Streamlit은 파이썬만으로 웹 어플리케이션을 구성할 수 있는 Python 패키지로, 
    웹 어플리케이션, 대시보드 프로토타입을 개발하기에 적합함
    ### Streamlit 기본정보
    - [streamlit.io](https://streamlit.io)
    - 문서자료:[documentation](https://docs.streamlit.io)
    - 커뮤니티에 질문하기 [community
        forums](https://discuss.streamlit.io)
    ### 좀 더 복잡한 데모를 보려면
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)