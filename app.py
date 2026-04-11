import streamlit as st
import random
import time
import pandas as pd

st.set_page_config(layout="wide")

# -------- STYLE --------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

/* Card styling */
.card {
    background-color: black;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    color: white !important;
    box-shadow: 0 0 10px rgba(255,255,255,0.1);
}

/* Force text white */
.card h1, .card h2, .card h3, .card h4, .card p {
    color: white !important;
}

/* Alert */
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

st.title("🚀 AI Threat Intelligence System")

# -------- SESSION STATE --------
if "run" not in st.session_state:
    st.session_state.run = False

if "attack" not in st.session_state:
    st.session_state.attack = False

# -------- BUTTONS --------
colA, colB = st.columns(2)

with colA:
    if st.button("▶️ Start Monitoring"):
        st.session_state.run = True

with colB:
    if st.button("🚨 Simulate Attack"):
        st.session_state.attack = True

# -------- DASHBOARD --------
if menu == "Dashboard":

    placeholder = st.empty()

    if st.session_state.run:

        for i in range(20):

            packets = random.randint(10, 100)
            bytes_data = random.randint(100, 1200)
            duration = random.randint(1, 10)

            # NORMAL FIRST
            if i < 3:
                attack = "Normal"
                risk = random.randint(5, 20)

            # ATTACK MODE
            elif st.session_state.attack:
                attack = random.choice(["Flood Attack", "DoS Attack", "DDoS Attack"])
                risk = random.randint(75, 99)

            else:
                attack = "Normal"
                risk = random.randint(10, 40)

            with placeholder.container():

                col1, col2, col3, col4 = st.columns(4)

                col1.markdown(f'<div class="card"><h4>Attack</h4><h2>{attack}</h2></div>', unsafe_allow_html=True)
                col2.markdown(f'<div class="card"><h4>Risk %</h4><h2>{risk}</h2></div>', unsafe_allow_html=True)
                col3.markdown(f'<div class="card"><h4>Packets</h4><h2>{packets}</h2></div>', unsafe_allow_html=True)
                col4.markdown(f'<div class="card"><h4>Bytes</h4><h2>{bytes_data}</h2></div>', unsafe_allow_html=True)

                # -------- GRAPH --------
                chart_data = pd.DataFrame({
                    "Packets": [random.randint(10,100) for _ in range(30)],
                    "Bytes": [random.randint(100,1200) for _ in range(30)]
                })
                st.line_chart(chart_data)

                # -------- NETWORK MAP --------
                st.subheader("🌐 Network Activity")
                nodes = ["User", "Server", "Firewall", "Database"]
                for _ in range(5):
                    st.write(f"{random.choice(nodes)} ➝ {random.choice(nodes)}")

                # -------- ALERT --------
                if attack != "Normal":
                    st.markdown(f'<div class="alert">🚨 {attack} DETECTED!</div>', unsafe_allow_html=True)
                else:
                    st.success("✅ System Safe")

            time.sleep(1)

        # reset attack
        st.session_state.attack = False

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
