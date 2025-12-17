import streamlit as st
from analyzer.log_parser import parse_logs, detect_bruteforce
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
    ip_attempts = parse_logs(logs)
    suspicious_ips = detect_bruteforce(ip_attempts)

    if suspicious_ips:
        st.error("⚠️ Suspicious activity detected!")
        for ip, count in suspicious_ips.items():
             st.write(f"🔴 IP `{ip}` had `{count}` failed login attempts")

    else:
            st.success("✅ No suspicious activity detected.")
