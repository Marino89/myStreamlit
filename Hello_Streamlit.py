
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon=":wave:",
)

st.write("# Streamlit 맛보기 😋")

# st.sidebar.success("Streamlit 소개")

st.image("./pages/img/img_matplotlib.png", caption=" ")
st.markdown(
    """
    Streamlit은 파이썬만으로 웹 어플리케이션을 구성할 수 있는 Python 패키지로, 
    웹 어플리케이션, 대시보드 프로토타입을 개발하기에 적합함
    
    "![foo](https://www.google.com/imgres?q=matplotlib&imgurl=https%3A%2F%2Fwww.jumpingrivers.com%2Fblog%2Fcustomising-matplotlib%2Fmatplot_title_logo.png&imgrefurl=https%3A%2F%2Fwww.jumpingrivers.com%2Fblog%2Fcustomising-matplotlib%2F&docid=_v9yiDQDVpDv5M&tbnid=xfxE4lTw_4YraM&vet=12ahUKEwj36t6Y3tWHAxXDQPUHHdVVBAsQM3oECCsQAA..i&w=600&h=200&hcb=2&ved=2ahUKEwj36t6Y3tWHAxXDQPUHHdVVBAsQM3oECCsQAA)"
    - matpoltlib, plotly와 같은 다양한 데이터 시각화 패키지와 호환을 지원
    ### 설치 📦
    - anaconda, venv환경에서 아래와 같이 간단한 커맨드로 설치 가능
    ```
    pip install streamlit
    ```
    ```
    stream hello
    ```
    ### Git, GitHub를 활용하여 배포하기
    - Streamlit으로 만든 웹 어플리케이션을 Git 또는 GitHub를 통해 배포 가능
    ```
    git init "원격저장소를 생성"
    git config --global user.email "본인의 이메일계정"
    git config --global user.name "본인 GitHub의 이름"
    git remote add origin (본인의 GitHub 주소)
    git status "원격저장소에 올라갈 파일을 상태 확인"
    git add "파일을 GitHub에 업로드"
    git commit "commit 메시지 입력"
    ```
"""
)

# if __name__=='__main__':
#     test_app()