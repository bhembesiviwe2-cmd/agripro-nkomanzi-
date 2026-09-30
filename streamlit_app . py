import streamlit as st
st.set_page_config(page_title="AgriPro - Nkomazi", page_icon="🌱", layout="centered")
st.sidebar.title("🔐 Farmer Login")
password = st.sidebar.text_input("Enter Farmer Code", type="password")
if password != "NKOMAZI2026":
    st.title("🌱 AgriPro")
    st.subheader("Nkomazi Smart Farming App")
    st.info("Welcome! Enter code on left. Built by Nhanyane Secondary.")
    st.stop()
st.title("🌱 AgriPro")
st.success("✅ Logged in!")
crop = st.selectbox("Select Crop", ["beans", "maize", "tomatoes", "cabbage", "spinach", "sugarcane"])
weather = st.selectbox("Weather", ["sunny", "rainy", "cloudy", "dry", "very hot"])
cost = st.number_input("Seed Cost (R)", value=50)
if st.button("GET ADVICE", type="primary", use_container_width=True):
    if weather in ["dry", "very hot"]:
        st.success(f"Don't plant {crop} now. Wait for rain.")
    else:
        st.success(f"Perfect for {crop}! Plant now.")
st.caption("© 2026 Nhanyane Secondary School Learner Project")
