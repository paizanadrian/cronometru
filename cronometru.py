import streamlit as st
import time

# Set the page title and icon
st.set_page_config(page_title="Cronometru", page_icon="⏱️")

st.title("Cronometru")

# Initialize session state variables
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
    st.session_state.elapsed_time = 0
    st.session_state.running = False

# Define functions to handle button clicks
def start_timer():
    if not st.session_state.running:
        st.session_state.start_time = time.time() - st.session_state.elapsed_time
        st.session_state.running = True

def stop_timer():
    if st.session_state.running:
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
        st.session_state.running = False

# Display start and stop buttons
col1, col2 = st.columns(2)
with col1:
    if st.button('Start'):
        start_timer()
with col2:
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
