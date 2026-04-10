import streamlit as st
import random
import time

# -------- PAGE CONFIG --------
st.set_page_config(page_title="AI Threat Detection", layout="centered")

st.title("🚀 AI Threat Intelligence System")

# -------- SESSION STATE --------
if "attack" not in st.session_state:
    st.session_state.attack = False

if "running" not in st.session_state:
    st.session_state.running = False

# -------- BUTTONS --------
col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Start Monitoring"):
        st.session_state.running = True

with col2:
    if st.button("🚨 Simulate Attack"):
        st.session_state.attack = True

# -------- STATUS DISPLAY --------
status_box = st.empty()

# -------- MAIN LOGIC --------
if st.session_state.running:

    for i in range(10):  # loop limited to avoid crash

        packets = random.randint(20, 100)
        bytes_data = random.randint(200, 1200)
        duration = random.randint(1, 10)

        # -------- NORMAL FIRST --------
        if i < 3:
            attack_type = "Normal"
            confidence = 10

        # -------- SIMULATED ATTACK --------
        elif st.session_state.attack:
            attack_type = random.choice(["Flood Attack", "DoS Attack", "DDoS Attack"])
            confidence = random.randint(80, 99)

        # -------- NORMAL RANDOM --------
        else:
            attack_type = "Normal"
            confidence = random.randint(10, 30)

        # -------- DISPLAY --------
        if attack_type == "Normal":
            status_box.success(f"✅ Packet {i+1}: NORMAL")
        else:
            status_box.error(f"🚨 Packet {i+1}: {attack_type} DETECTED | Risk: {confidence}%")

        time.sleep(1)

    # Reset attack after showing once
    st.session_state.attack = False
