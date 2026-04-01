import streamlit as st
import time
import random
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(page_title="Digital Twin Dashboard", layout="wide")
st.markdown(
    "<h1 style='text-align: center; color: #FF5733;'>🌡️ Digital Twin Temperature Dashboard</h1>",
    unsafe_allow_html=True
)

# Function to simulate sensor data
def get_sensor_data():
    return {"temperature": random.randint(60, 100)}

# Store history
history = []
placeholder = st.empty()

while True:
    data = get_sensor_data()
    temp = data["temperature"]
    history.append({"temperature": temp})
    df = pd.DataFrame(history)

    with placeholder.container():
        # Current temperature display
        st.markdown(
            f"<h2 style='color: {'red' if temp>80 else 'green'};'>Current Temperature: {temp} °C</h2>",
            unsafe_allow_html=True
        )

        # Alert logic
        if temp > 80:
            st.error("⚠️ ALERT: Temperature too high!")
        else:
            st.success("✅ Status: OK")

        # Line chart of temperature history
        st.subheader("📈 Temperature Trend")
        fig = px.line(df, y="temperature", title="Temperature Over Time",
                      line_shape="spline", markers=True,
                      color_discrete_sequence=["#FF5733"])
        st.plotly_chart(fig, use_container_width=True)

        

    time.sleep(2)  # refresh every 2 seconds
