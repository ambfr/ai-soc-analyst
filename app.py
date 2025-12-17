import re
import streamlit as st
from analyzer.llm_analyzer import analyze_threat


def extract_ips(text):
    pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    return list(set(re.findall(pattern, text)))


# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="AI SOC Analyst", layout="centered")

st.title("🛡️ AI SOC Analyst")
st.caption("Hybrid Rule-Based + Local GPT-2 Threat Explanation")

st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload a log file (.log)",
    type=["log", "txt"]
)

st.markdown("---")

if uploaded_file is not None:
    try:
        log_data = uploaded_file.read().decode("utf-8")
    except Exception:
        st.error("Unable to read file. Please upload a valid text-based log file.")
        st.stop()

    if st.button("🔍 Analyze Logs"):
        ips = extract_ips(log_data)

        if not ips:
            st.info("No IP addresses found in the uploaded log file.")
        else:
            st.success(f"Suspicious IPs detected: {ips}")

            with st.spinner("Analyzing threats..."):
                reports = analyze_threat(ips)

            st.markdown("## 📊 Threat Analysis Report")

            for ip, report in reports.items():
                with st.expander(f"🔎 IP: {ip}", expanded=True):
                    st.text(report)
else:
    st.info("Please upload a .log file to begin analysis.")
