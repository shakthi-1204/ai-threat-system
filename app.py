import streamlit as st
import random
import time
import pandas as pd
import streamlit.components.v1 as components
from model import predict

st.set_page_config(layout="wide")

# 🔊 Voice function (WORKS ONLINE + MOBILE)
def speak(text):
    components.html(f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{text}");
        window.speechSynthesis.speak(msg);
        </script>
    """)

# -------- STYLE --------
st.markdown("""
<style>
body { background-color: #0e1117; color: white; }
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}
.alert {
    animation: blink 1s infinite;
    color: red;
    font-size: 24px;
    font-weight: bold;
}
@keyframes blink {
    50% { opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# -------- SIDEBAR --------
st.sidebar.title("🛡️ Control Panel")
menu = st.sidebar.radio("Navigation", ["Dashboard", "Live Monitoring", "Prediction", "Analysis"])

st.title("🛡️ AI Threat Intelligence System")

run = st.toggle("▶ Start Live Detection")

# -------- DASHBOARD --------
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

                st.subheader("🌐 Network Map")
                nodes = ["User", "Server", "Firewall", "Database"]
                for _ in range(5):
                    st.write(f"{random.choice(nodes)} ➝ {random.choice(nodes)}")

                # 🔥 ATTACK DETECTION WITH VOICE
                if attack != "Normal":
                    st.markdown(f'<div class="alert">🚨 {attack} DETECTED!</div>', unsafe_allow_html=True)
                    speak("Warning! " + attack + " detected")
                else:
                    st.success("✅ System Safe")

            time.sleep(2)

# -------- LIVE MONITORING --------
elif menu == "Live Monitoring":
    st.subheader("📡 Live Logs")
    for i in range(10):
        st.write(f"Log {i}: {random.randint(10,100)} packets")

# -------- PREDICTION --------
elif menu == "Prediction":
    st.subheader("🔮 Future Threat Prediction")
    future = random.randint(50, 95)
    st.write(f"Predicted Risk: {future}%")

    if future > 75:
        st.warning("⚠️ High probability of attack soon")

# -------- ANALYSIS --------
elif menu == "Analysis":
    st.subheader("🧠 AI Explanation")
    st.write("""
    - High packets → Flood attack  
    - High bytes → Data exfiltration  
    - Short bursts → DoS attack  
    """)
