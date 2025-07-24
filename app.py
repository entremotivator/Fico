import streamlit as st

st.set_page_config(page_title="MyFICO Embed", layout="wide")

st.title("MyFICO Website Viewer")

# Embed the MyFICO site in an iframe (may not load due to X-Frame-Options)
myfico_url = "https://www.myfico.com/"
iframe_code = f"""
    <iframe src="{myfico_url}"
            width="100%"
            height="800px"
            style="border:none;">
    </iframe>
"""

st.markdown(iframe_code, unsafe_allow_html=True)

st.warning("Note: If the website doesn't load, it's likely due to iframe restrictions (X-Frame-Options).")
