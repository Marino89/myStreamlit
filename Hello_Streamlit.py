
import urllib.request
import json
import pandas as pd
# import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Hello",
    page_icon=":wave:",
)

st.write("# Streamlit 맛보기 😋")

image_bundle = ['./pages/img/img_matplotlib.png', './pages/img/img_plotly.png']
st.image(image_bundle, width=100, caption=" ")
st.markdown(
    """
    Streamlit이란 python만으로 웹 어플리케이션을 구성할 수 있는 python 패키지로써, 웹 어플리케이션, 대시보드의 프로토타입을 개발하기에 적합함
    - matpoltlib, plotly와 같은 다양한 데이터 시각화 패키지와 호환을 지원
    
    ### 설치
    - anaconda, venv 환경에서 아래와 같이 간단한 커맨드로 설치 가능
    ```
    pip install streamlit
    ```
    ```
    stream hello
    ```
    
    ### Git, GitHub 활용하여 배포하기
    - Streamlit을 활용하여 만든 웹 어플리케이션을 Git, GitHub를 통해 배포 가능
    ```
    git init "원격저장소를 생성"
    git config --global user.email "본인 이메일 계정"
    git config --global user.name "본인 GitHub 이름"
    git remote add origin (본인 GitHub 주소)
    git status "원격저장소에 올라갈 파일의 상태를 확인"
    git add "파일을 깃허브에 업로드"
    git commit "commit 메시지입력"
    ```
"""
)

st.image("./pages/img/img_github.png", caption=" ")
