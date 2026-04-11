import streamlit as st
import random
import time
import pandas as pd

st.set_page_config(layout="wide")

st.title("🚀 AI Threat Intelligence System")

# -------- SESSION STATE --------
if "run" not in st.session_state:
    st.session_state.run = False

if "attack" not in st.session_state:
    st.session_state.attack = False

# -------- BUTTONS (OUTSIDE LOOP) --------
col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Start Monitoring"):
        st.session_state.run = True

with col2:
    if st.button("🚨 Simulate Attack"):
        st.session_state.attack = True

# -------- DASHBOARD --------
if st.session_state.run:

    placeholder = st.empty()

    for i in range(20):   # limited loop (avoid crash)

        packets = random.randint(10, 100)
        bytes_data = random.randint(100, 1200)
        duration = random.randint(1, 10)

        # -------- NORMAL FIRST --------
        if i < 3:
            attack = "Normal"
            risk = random.randint(5, 20)

        # -------- ATTACK --------
        elif st.session_state.attack:
            attack = random.choice(["Flood Attack", "DoS Attack", "DDoS Attack"])
            risk = random.randint(75, 99)

        # -------- NORMAL --------
        else:
            attack = "Normal"
            risk = random.randint(10, 40)

        with placeholder.container():

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Attack", attack)
            col2.metric("Risk %", risk)
            col3.metric("Packets", packets)
            col4.metric("Bytes", bytes_data)

            # -------- GRAPH --------
            chart_data = pd.DataFrame({
                "Packets": [random.randint(10,100) for _ in range(20)],
                "Bytes": [random.randint(100,1200) for _ in range(20)]
            })
            st.line_chart(chart_data)

            # -------- ALERT --------
            if attack != "Normal":
                st.error(f"🚨 {attack} DETECTED!")
            else:
                st.success("✅ System Safe")

        time.sleep(1)

    # reset attack after one cycle
    st.session_state.attack = False
