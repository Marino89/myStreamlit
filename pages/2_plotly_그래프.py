#%%
# !터미널 - streamlit run .\realtime_OceanData_Analysis_using_API_v2.py --server.port 8080
#%%
# 라이브러리 불러오기
import urllib.request
import json
import pandas as pd
# import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta
# import time

# %%

# %%
# 인증키와 주소
key = 'sr459ziApoSMy4hv1yD3Mw=='
td_busan = 'DT_0002'
ob_busan = 'TW_0086'

# td_url = f'http://www.khoa.go.kr/api/oceangrid/tideCurPre/search.do?ServiceKey={key}&ObsCode={td_busan}&Date={str_date}&ResultType=json'

# # 수온관측 API URL
# ob_url = f'http://www.khoa.go.kr/api/oceangrid/tideObsTemp/search.do?ServiceKey={key}&ObsCode={td_busan}&Date={str_date}&ResultType=json'
# %%
# 조위관측소 실측 & 예측 (날짜검색 기준 1시간 간격)
st.set_page_config(page_title="부산의 실시간 조위 및 수온", page_icon="📈")

@st.cache_data
def get_data(url):
        df = pd.DataFrame()
        if url == 'td_url':
            

            for i in range(10, -1, -1):
                # now = datetime.now()-i
                # str_date = now.strftime('%Y%m%d'))
                str_date = datetime.strftime(datetime.now() - timedelta(i), '%Y%m%d')

                url = f'http://www.khoa.go.kr/api/oceangrid/tideCurPre/search.do?ServiceKey={key}&ObsCode={td_busan}&Date={str_date}&ResultType=json'
                # 데이터 가져오기
                response = urllib.request.urlopen(url)
                json_str = response.read().decode('utf-8')
                # JSON -> Dict으로 변환
                json_object = json.loads(json_str)

                #Dict -> 데이터프레임으로 변환
                data = pd.json_normalize(json_object['result']['data'])
                df = df._append(data) 
        elif url == 'ob_url':
            
            for i in range(10, -1, -1):
                # now = datetime.now()-i
                # str_date = now.strftime('%Y%m%d'))
                str_date = datetime.strftime(datetime.now() - timedelta(i), '%Y%m%d')
                url = f'http://www.khoa.go.kr/api/oceangrid/tideObsTemp/search.do?ServiceKey={key}&ObsCode={td_busan}&Date={str_date}&ResultType=json'

                # 데이터 가져오기
                response = urllib.request.urlopen(url)
                json_str = response.read().decode('utf-8')
                # JSON -> Dict으로 변환
                json_object = json.loads(json_str)

                #Dict -> 데이터프레임으로 변환
                data = pd.json_normalize(json_object['result']['data'])
                df = df._append(data)  
        return df


# %%
td_df= get_data('td_url')
# td_df.columns=['time', '실측조위','예측조위']
ob_df= get_data('ob_url')

# 데이터 타입 변환
td_df['record_time'] = pd.to_datetime(td_df['record_time'], format='%Y-%m-%d %H:%M')
td_df['pre_value'] = td_df['pre_value'].astype(float)
td_df['real_value'] = td_df['real_value'].astype(float)
# %%

# %%
ob_df['record_time'] = pd.to_datetime(ob_df['record_time'], format='%Y-%m-%d %H:%M:%S')
ob_df['water_temp'] = ob_df['water_temp'].astype(float)

#Savitzky-Golay 필터 적용
window_length = 51  # 필터 윈도우 크기 (홀수)
polyorder = 4       # 다항식 차수
ob_df['temp_mod'] = savgol_filter(ob_df['water_temp'], window_length,polyorder)
ob_df.columns=['일시', 'water_temp', u'수온(\u00B0C)']
# %%
# def app():
    
#     # st.set_page_config(layout="wide")
#     col1, col2 = st.columns(2)
#     st.title('부산의 현재 조위와 수온')

#     # matplotlib으로 그래프 시각화
#     fig1, ax = plt.subplots()
#     ax.plot(td_df['record_time'], td_df['pre_value'], 'b-', label='predicted')
#     ax.plot(td_df['record_time'], td_df['real_value'], 'r-',label='real time')
#     ax.set_xlabel('time')
#     ax.set_ylabel('tidal height(cm)')
#     plt.title('Tide Level at Busan')
#     plt.xticks(rotation=45)
#     ax.legend()
    
#     # Savitzky-Golay 필터 적용
#     window_length = 51  # 필터 윈도우 크기 (홀수)
#     polyorder = 4       # 다항식 차수
#     ob_df['temp_mod'] = savgol_filter(ob_df['water_temp'], window_length, polyorder)
    
#     # Matplotlib을 사용하여 그래프를 생성합니다.
#     fig2, ax = plt.subplots()
#     ax.plot(ob_df['record_time'], ob_df['water_temp'], 'b-', label='original')
#     ax.plot(ob_df['record_time'], ob_df['temp_mod'], 'r-', label='Savitzky-Golay mod')
#     ax.set_xlabel('time')
#     ax.set_ylabel(u'Temp (\u00B0C)')
#     #ax.set_title('부산의 현재 수온')
#     ax.legend()
#     plt.xticks(rotation=45)
#     # Streamlit을 사용하여 그래프를 표시합니다.
#     col1 = st.pyplot(fig1)
#     col2 = st.pyplot(fig2)



st.markdown("# 부산 실시간 조위 및 수온")
st.sidebar.header("부산 실시간 조위 및 수온")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# chart = st.line_chart(last_rows)

fig1 = px.line(td_df, x='record_time', y="real_value")
fig2 = px.line(ob_df, x='일시', y="수온(\u00B0C)")

tab1, tab2 = st.tabs(["부산 조위", "부산 수온"])
with tab1:
    st.plotly_chart(fig1, theme="streamlit")
with tab2:
    st.plotly_chart(fig2, theme=None)

# st.button("Re-run")
