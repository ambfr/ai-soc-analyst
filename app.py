import streamlit as st

st.set_page_config(
    page_title="AI SOC Analyst",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI SOC Analyst")
st.subheader("LLM-powered log analysis & threat explanation engine")

st.markdown("""
Upload system or network logs and let an AI SOC analyst:
- Detect suspicious activity
- Identify possible attacks
- Explain risks in plain English
- Suggest mitigation steps
""")

st.divider()

uploaded_file = st.file_uploader(
    "Upload a log file",
    type=["log", "txt"]
)

if uploaded_file:
    logs = uploaded_file.read().decode("utf-8")

    st.success("Log file uploaded successfully!")

    with st.expander("📄 View Raw Logs"):
        st.text(logs)

    if st.button("🔍 Analyze Logs"):
        st.info("Analysis engine coming next... 🚀")
