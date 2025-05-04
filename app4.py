import streamlit as st

if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button("increase counter"):
    st.session_state.count += 1

st.write("counter value:", st.session_state.count)
