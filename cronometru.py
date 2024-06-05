import streamlit as st
import time
import json
import os

# Set the page title and icon
st.set_page_config(page_title="Cronometru", page_icon="⏱️")

st.title("Cronometru")

# File to store the timer state
TIMER_FILE = "timer_state.json"

# Load the timer state from the file
if os.path.exists(TIMER_FILE):
    with open(TIMER_FILE, "r") as f:
        timer_state = json.load(f)
else:
    timer_state = {"start_time": 0, "elapsed_time": 0, "running": False}

# Initialize session state variables from the timer state
if 'start_time' not in st.session_state:
    st.session_state.start_time = timer_state["start_time"]
    st.session_state.elapsed_time = timer_state["elapsed_time"]
    st.session_state.running = timer_state["running"]

# Define functions to handle button clicks
def start_timer():
    if not st.session_state.running:
        st.session_state.start_time = time.time() - st.session_state.elapsed_time
        st.session_state.running = True
        save_timer_state()

def stop_timer():
    if st.session_state.running:
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
        st.session_state.running = False
        save_timer_state()

def reset_timer():
    st.session_state.start_time = 0
    st.session_state.elapsed_time = 0
    st.session_state.running = False
    save_timer_state()

def save_timer_state():
    timer_state = {
        "start_time": st.session_state.start_time,
        "elapsed_time": st.session_state.elapsed_time,
        "running": st.session_state.running
    }
    with open(TIMER_FILE, "w") as f:
        json.dump(timer_state, f)

# Display start, reset, and stop buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button('Start'):
        start_timer()
with col2:
    if st.button('RESET', key='reset', help='Resetează cronometru', button_type='primary'):
        reset_timer()
with col3:
    if st.button('Stop'):
        stop_timer()

# Update the elapsed time
if st.session_state.running:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time

# Format the elapsed time
elapsed_time = st.session_state.elapsed_time
hours, rem = divmod(elapsed_time, 3600)
minutes, seconds = divmod(rem, 60)
time_str = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))

st.header(time_str)

# Refresh the timer every second if running
if st.session_state.running:
    time.sleep(1)
    st.experimental_rerun()


# streamlit run cronometru.py