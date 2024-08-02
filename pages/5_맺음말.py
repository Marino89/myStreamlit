import streamlit as st

st.set_page_config(
    page_title="Good Job!",
    page_icon="?",
)

st.write("# 수고하였습니다! :wave: ")

st.sidebar.success("Well done!")

style_image2 = """
width: auto;
max-width: 900px;
height: auto;
max-height: 800px;
display: block;
justify-content: center;
border-radius: 30%;
"""

st.markdown("![Foo](https://media.giphy.com/media/kBZBlLVlfECvOQAVno/giphy.gif?cid=790b7611at9x6ki34b0hqxfndjxe7m7vw3cawns5juhrrrv5&ep=v1_gifs_search&rid=giphy.gif&ct=g)")

st.markdown(
    f'<img src="{"https://media.giphy.com/media/kBZBlLVlfECvOQAVno/giphy.gif?cid=790b7611at9x6ki34b0hqxfndjxe7m7vw3cawns5juhrrrv5&ep=v1_gifs_search&rid=giphy.gif&ct=g"}" style="{style_image2}">',
    unsafe_allow_html=True,
)
