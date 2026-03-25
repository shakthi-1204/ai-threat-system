import streamlit as st
import random
import time
import pandas as pd
from model import predict
from utils import speak_alert

st.set_page_config(layout="wide")

st.markdown("""
<style>
body { background-color: #0e1117; color: white; }
.card { background-color: #1c1f26; padding: 20px; border-radius: 12px; text-align: center; }
.alert { animation: blink 1s infinite; color: red; font-size: 24px; }
@keyframes blink { 50% { opacity: 0; } }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🛡️ Control Panel")
menu = st.sidebar.radio("Navigation", ["Dashboard", "Live Monitoring", "Prediction", "Analysis"])

st.title("🛡️ AI Threat Intelligence System")

run = st.toggle("▶ Start Live Detection")

if menu == "Dashboard":
    placeholder = st.empty()

    if run:
        while True:
            packets = random.randint(10, 100)
            bytes_data = random.randint(100, 1200)
            duration = random.randint(1, 10)

            attack, risk = predict(packets, bytes_data, duration)

            with placeholder.container():
                col1, col2, col3, col4 = st.columns(4)

                col1.markdown(f'<div class="card">Attack<br><h2>{attack}</h2></div>', unsafe_allow_html=True)
                col2.markdown(f'<div class="card">Risk %<br><h2>{risk}</h2></div>', unsafe_allow_html=True)
                col3.markdown(f'<div class="card">Packets<br><h2>{packets}</h2></div>', unsafe_allow_html=True)
                col4.markdown(f'<div class="card">Bytes<br><h2>{bytes_data}</h2></div>', unsafe_allow_html=True)

                chart_data = pd.DataFrame({
                    "Packets": [random.randint(10,100) for _ in range(30)],
                    "Bytes": [random.randint(100,1200) for _ in range(30)]
                })
                st.line_chart(chart_data)

                if attack != "Normal":
                    st.markdown(f'<div class="alert">🚨 {attack} DETECTED!</div>', unsafe_allow_html=True)
                    speak_alert(attack)
                else:
                    st.success("✅ System Safe")

            time.sleep(2)

elif menu == "Live Monitoring":
    st.write("Logs loading...")

elif menu == "Prediction":
    st.write("Future risk coming soon...")

elif menu == "Analysis":
    st.write("AI explains threats...")