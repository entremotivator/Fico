import streamlit as st
import requests

st.set_page_config(page_title="Credit AI Builder", layout="centered")

st.title("🤖 Credit AI Builder")

st.markdown("""
Fill out your profile and upload a credit report if available.  
Ask your credit-related question and our system will process it via AI + team review.

---
""")

# --- FORM SECTION ---
with st.form("credit_form"):
    st.subheader("📇 Customer Profile")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    zip_code = st.text_input("ZIP Code")
    dob = st.date_input("Date of Birth")

    st.subheader("💬 Credit Question or Concern")
    question = st.text_area("Write your credit-related question")

    st.subheader("📎 Upload Credit Report (PDF)")
    pdf_file = st.file_uploader("Optional: Upload a credit report PDF", type=["pdf"])

    submitted = st.form_submit_button("Submit to Credit AI")

    if submitted:
        if not name or not email or not phone or not question:
            st.error("Please complete all required fields (Name, Email, Phone, Question).")
        else:
            try:
                webhook_url = "https://your-n8n-instance.com/webhook/credit-check-form"  # 🔁 Replace with your actual webhook URL

                files = {"file": (pdf_file.name, pdf_file, "application/pdf")} if pdf_file else None

                data = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "zip_code": zip_code,
                    "dob": str(dob),
                    "question": question
                }

                if files:
                    response = requests.post(webhook_url, data=data, files=files)
                else:
                    response = requests.post(webhook_url, json=data)

                if response.status_code == 200:
                    st.success("✅ Your info and question were submitted successfully!")
                else:
                    st.error("⚠️ Submission failed. Please try again later.")
            except Exception as e:
                st.error(f"❌ Error submitting form: {e}")

# --- EXTERNAL LINK SECTION ---
st.markdown("---")
st.subheader("📄 Want to check your official credit report?")

st.markdown(
    """
    <a href="https://www.myfico.com/" target="_blank">
        <button style="padding: 0.75em 1.5em; font-size: 16px; background-color: #00468b; color: white; border: none; border-radius: 6px; cursor: pointer;">
            Get Your Credit Report on MyFICO
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

st.caption("This opens the official MyFICO site in a new browser tab.")
