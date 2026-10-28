import time
from datetime import datetime

import pandas as pd
import streamlit as st

from sensor_simulator import generate_reading, get_status, reading_to_csv_row

st.set_page_config(page_title="Smart Environmental Monitor", page_icon="🌡️", layout="wide")
st.title("🌡️ Smart Environmental Monitoring System")
st.caption("Beginner-friendly IoT project • Python simulation mode")

st.info(
    "This first version simulates sensor readings so you can test the dashboard without hardware. "
    "It does not measure your room's actual temperature or humidity."
)

with st.sidebar:
    st.header("Settings")
    temp_limit = st.slider("High-temperature alert (°C)", 20, 45, 30)
    humidity_limit = st.slider("High-humidity alert (%)", 40, 95, 75)
    refresh = st.checkbox("Generate a new reading", value=False)
    st.caption("Turn on the checkbox to refresh the simulated reading each time the app reruns.")

if "readings" not in st.session_state:
    st.session_state.readings = []

reading = generate_reading()
reading["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
reading["status"] = get_status(reading["temperature_c"], reading["humidity_pct"], temp_limit, humidity_limit)

st.subheader("Latest simulated reading")
c1, c2, c3 = st.columns(3)
c1.metric("Temperature", f'{reading["temperature_c"]:.1f} °C')
c2.metric("Humidity", f'{reading["humidity_pct"]:.1f} %')
c3.metric("Status", reading["status"])

if reading["status"] == "ALERT":
    st.error("Alert: one or more readings exceed your configured limits.")
else:
    st.success("All readings are within the configured limits.")

if not st.session_state.readings or refresh:
    st.session_state.readings.append(reading)
elif st.session_state.readings:
    # Keep the current display consistent without adding a new history point on every rerun.
    reading = st.session_state.readings[-1]

st.subheader("Reading history")
history = pd.DataFrame(st.session_state.readings)
if not history.empty:
    chart_data = history.set_index("timestamp")[["temperature_c", "humidity_pct"]]
    st.line_chart(chart_data)
    st.dataframe(history, use_container_width=True)

    csv_data = history.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download history as CSV",
        data=csv_data,
        file_name="environment_readings.csv",
        mime="text/csv",
    )
else:
    st.write("No readings yet.")

if st.button("Add another simulated reading"):
    new_reading = generate_reading()
    new_reading["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_reading["status"] = get_status(
        new_reading["temperature_c"], new_reading["humidity_pct"], temp_limit, humidity_limit
    )
    st.session_state.readings.append(new_reading)
    st.rerun()

st.markdown("---")
st.caption("Next upgrade: connect an ESP32 and a DHT22/AM2302 sensor to replace simulated readings with real measurements.")
