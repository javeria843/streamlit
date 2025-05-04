import streamlit as st
st.title("Interactive widgets demo")

age= st.slider("select your age" ,0,100,25)
st.write(f"your age is {age}")
if st.checkbox("Show secret message"):
    st.success("🎉 You found the secret!")

gender= st.radio("choose your gender", ["Male", "female","other"])
st.write("selected" , gender)

hobby=st.selectbox("choosea hobby",["Reading" , "gaming","sports"])
st.write(f"you like:{hobby}")

st.number_input("pick a number",0,10)


