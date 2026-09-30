import streamlit as st

st.set_page_config(page_title="AgriPro Nkomanzi", layout="centered")
st.title("🌱 AgriPro - Nkomazi Smart Farming App")

st.sidebar.title("🔐 Farmer Login")
code = st.sidebar.text_input("Enter Farmer Code", type="password", placeholder="Type code here")

if code != "NKOMANZI2026":
    st.warning("Please enter Farmer Code in sidebar. Code is: NKOMANZI2026")
    st.info("Tap >> top left to open sidebar and login")
    st.stop()

st.sidebar.success("✅ Logged in!")
st.success("✅ Welcome Farmer! Logged in!")

crop = st.selectbox("Choose Crop", ["Maize", "Beans", "Tomatoes", "Cabbage"])
weather = st.selectbox("Weather", ["Sunny", "Rainy", "Cloudy", "Windy"])
cost = st.number_input("Enter cost (R)", min_value=0)

if st.button("GET ADVICE"):
    profit = cost * 1.5
    st.write(f"### Advice for {crop}")
    st.write(f"Weather: {weather}")
    st.write(f"Your cost: R{cost}")
    st.write(f"Expected selling: R{profit}")
    st.write("Tip: Plant early, water daily, use compost!")
    st.balloons()
