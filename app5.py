import streamlit as st
import time  # time.sleep ke liye

# Image
st.image("flower.jpg", caption="A very beautiful flower")

# Audio
st.audio("audio.mp3")

# Video
st.video("video.mp4")

# File uploader
uploaded_file = st.file_uploader("Upload a photo")

# Color picker
color = st.color_picker("Choose your favourite color")

# Text input
email = st.text_input("Email address")

# Date input
date = st.date_input("Travelling date")

# Time input
school_time = st.time_input("School time")

# Text area
message = st.text_area("Enter your message")

# Balloons animation
st.balloons()

# Sleep for 10 seconds
time.sleep(10)
