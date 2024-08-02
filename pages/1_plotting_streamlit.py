
#%%
import urllib.request
import json
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta
import time
#%%
st.set_page_config(page_title="Plotting Demo", page_icon="?")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)
#%%

key = 'sr459ziApoSMy4hv1yD3Mw=='
td_busan = 'DT_0002'
ob_busan = 'TW_0086'

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
df = pd.DataFrame()
chart = st.line_chart(df)
#%%
# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

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
    new_df = df._append(pd.json_normalize(json_object['result']['data']))
    # df = df._append(data)  

    chart.add_rows(new_df)
    df = new_df
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")