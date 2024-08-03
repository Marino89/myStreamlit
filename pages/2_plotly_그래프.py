
# !터미널 - streamlit run .\realtime_OceanData_Analysis_using_API_v2.py --server.port 8080

# 라이브러리 불러오기
import urllib.request
import json
import pandas as pd
from scipy.signal import savgol_filter
import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh

# update every 5 mins
st_autorefresh(interval=5 * 60 * 1000, key="dataframerefresh")

# 인증키와 파라미터
key = 'sr459ziApoSMy4hv1yD3Mw=='
td_busan = 'DT_0005' # 부산항신항, 부산 DT_0005
#ob_busan = 'TW_0086'


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
            # 조위관측소 1분 단위 1일 자료
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


td_df= get_data('td_url')
# td_df.columns=['time', '실측조위','예측조위']
ob_df= get_data('ob_url')

# 데이터 타입 변환
td_df['record_time'] = pd.to_datetime(td_df['record_time'], format='%Y-%m-%d %H:%M')
td_df['pre_value'] = td_df['pre_value'].astype(float)
td_df['real_value'] = td_df['real_value'].astype(float)
td_df.columns=['일시', '실측조위(cm)', '예측조위(cm)']

ob_df['record_time'] = pd.to_datetime(ob_df['record_time'], format='%Y-%m-%d %H:%M:%S')
ob_df['water_temp'] = ob_df['water_temp'].astype(float)

#Savitzky-Golay 필터 적용
window_length = 51  # 필터 윈도우 크기 (홀수)
polyorder = 4       # 다항식 차수
ob_df['temp_mod'] = savgol_filter(ob_df['water_temp'], window_length,polyorder)
ob_df.columns=['일시', 'water_temp', u'수온(\u00B0C)']


st.markdown("# 부산 실시간 조위 및 수온")
st.sidebar.header("실시간 조위 및 수온")

st.write(
    """이 그래프는 국립해양조사원 OpenAPI를 이용하여 수집된 과거 10일 전부터 오늘까지의 자료로 시각화하였으며, 
    수온의 경우 센서 잡음처리를 위해 자체적으로 필터링 하였음 """
)


fig1 = px.line(td_df, x='일시', y="실측조위(cm)")
fig2 = px.line(ob_df, x='일시', y="수온(\u00B0C)")

tab1, tab2 = st.tabs(["조위", "수온"])
with tab1:
    st.plotly_chart(fig1, theme="streamlit")
with tab2:
    st.plotly_chart(fig2, theme=None)

st.button("Re-run")
