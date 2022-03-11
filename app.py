import requests
import streamlit as st
from streamlit_lottie import st_lottie


# https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":art:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---LOAD ASSETS ---
lottie_coding = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# --- HEADER
with st.container():
    st.subheader("Hai, nama saya heri :wave:")
    st.title("A Data Analyst from Indonesia")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effective in busines ")
    st.write("[Learn more >](https://adfadfadf.com)")

# ---WHAT I DO
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write("""
        Pilihlah kekuatan pahlawan super Anda. 
        - Anda juga bisa mempertimbangkan untuk memberikan lebih dari satu kekuatan kepada pahlawan super
        - Sebagian pahlawan super bahkan tidak memiliki kekuatan supernatural dan mengandalkan berbagai peralatan dan latihan 
        """)
        st.write("[Youtube Channel >](https://adfadfadf.com)")

    with right_column:
        st_lottie(lottie_coding,height=300, key="coding")
        