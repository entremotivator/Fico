import streamlit as st

st.set_page_config(page_title="Visit MyFICO", layout="centered")

st.title("🔐 Visit MyFICO Credit Site")

st.markdown("""
Welcome! To view your official credit score and detailed credit report, click below to visit the official MyFICO website in a new tab.
""")

# Open MyFICO in new tab
st.markdown(
    """
    <a href="https://www.myfico.com/" target="_blank">
        <button style="padding: 0.75em 1.5em; font-size: 16px; background-color: #00468b; color: white; border: none; border-radius: 6px; cursor: pointer;">
            Go to MyFICO Website
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

st.caption("This button opens the official MyFICO site in a new browser tab.")
