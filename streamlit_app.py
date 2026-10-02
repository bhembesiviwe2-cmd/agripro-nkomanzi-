import streamlit as st
import requests

st.set_page_config(page_title="AgriPro Mzansi", layout="centered", page_icon="🌱")
st.title("🌱 AgriPro Mzansi - Full Agric")
st.caption("Built in Magudu | 16yo Founder | Crops + Animals")

# LOGIN
st.sidebar.title("🔐 Farmer Login")
if st.sidebar.text_input("Code", type="password", placeholder="NKOMANZI2026")!= "NKOMANZI2026":
    st.warning("Enter: NKOMANZI2026"); st.stop()
st.sidebar.success("Welcome Farmer!")

# --- NEW: AGRIC TYPE SELECTOR ---
st.subheader("👨‍🌾 What type of Farmer are you?")
farming_type = st.radio("Choose your field:", ["🌽 Crop Science", "🐄 Animal Science", "🌾🐄 Mixed Farming (Both)"], horizontal=False)

# Common profile
TOWNS = {"Magudu": (-25.68, 31.56), "Tonga": (-25.67, 31.78), "Malelane": (-25.48, 31.52), "Komatipoort": (-25.43, 31.95), "Mbombela": (-25.47, 30.96), "Pretoria": (-25.74, 28.18), "Durban": (-29.85, 31.02), "Cape Town": (-33.92, 18.42), "Polokwane": (-23.90, 29.44)}
town = st.selectbox("📍 Farm Town:", list(TOWNS.keys()), index=0)
lat, lon = TOWNS[town]

# Weather
try:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=precipitation_sum,temperature_2m_max&timezone=Africa/Johannesburg"
    d = requests.get(url, timeout=10).json()["daily"]
    rain = d["precipitation_sum"][:5]; tmax = d["temperature_2m_max"][:5]
except:
    rain=[0,5,12,0,2]; tmax=[30,28,27,31,30]

# --- BRANCH BASED ON TYPE ---
if farming_type == "🌽 Crop Science":
    crop = st.selectbox("Your Main Crop", ["Maize", "Tomatoes", "Cabbage", "Beans", "Groundnuts", "Sugarcane", "Bananas", "Spinach"])
    st.subheader(f"🌽 Crop Science Dashboard: {crop} in {town}")

    # Personalized alerts for crops
    st.subheader(f"🚨 Pest Alert FOR {crop} in {town}")
    if town in ["Magudu","Tonga","Malelane","Komatipoort"] and crop=="Maize":
        st.error("🔴 HIGH: Fall Armyworm - Nkomazi hotspot! Check daily. Chemical: Ampligo R250 TWK")
    if sum(rain)>20:
        st.warning(f"🟠 MEDIUM: Fungus (Blight/Mildew) - {sum(rain)}mm rain in {town}. Use Mancozeb R180")
    if max(rain)>30:
        st.error(f"🌊 FLOOD ALERT {max(rain)}mm - Don't plant lowland!")
    if rain[1]>8:
        st.error(f"🚚 Market Alert: DON'T harvest for market tomorrow - {rain[1]}mm rain, no buyers!")

    # Crop clinic
    st.divider()
    st.subheader("🔬 Crop Clinic")
    photo = st.file_uploader("📸 Upload sick crop", type=["jpg","png","jpeg"], key="crop")
    if photo: st.image(photo)
    symp = st.multiselect("Symptoms:", ["Yellow leaves","Black spots","White powder","Holes/worms","Curling","Wilting","Rotting"])
    if st.button("Diagnose Crop"):
        if "Holes/worms" in symp: st.error("Fall Armyworm! Ampligo/Karate R250 - Spray NOW!")
        elif "White powder" in symp: st.warning("Powdery Mildew - Mancozeb R180")
        elif "Black spots" in symp: st.warning("Leaf Blight - Copper spray R200")
        else: st.info("Add more symptoms")

    # Soil
    st.divider()
    st.subheader("🧪 Soil Health")
    w = st.slider("Water times/week?",1,14,7, key="w1")
    if w>7: st.error("🚨 Acid risk! Reduce to 3x + add lime/ash")
    else: st.success("✅ Water OK")

elif farming_type == "🐄 Animal Science":
    animal = st.selectbox("Your Main Animal", ["Cattle", "Goats", "Sheep", "Chickens (Layers/Broilers)", "Pigs", "Ducks"])
    st.subheader(f"🐄 Animal Science Dashboard: {animal} in {town}")

    # Personalized alerts for animals
    st.subheader(f"🚨 Disease Alert FOR {animal} in {town}")
    if town in ["Magudu","Tonga","Malelane","Komatipoort"]:
        st.error("🔴 HIGH RISK ZONE: Lumpy Skin Disease & Foot & Mouth - Border area! Vaccinate! Call State Vet Tonga!")
    if sum(rain)>20:
        st.warning(f"🟠 Worms & Foot Rot risk - {sum(rain)}mm wet ground in {town}. Keep kraal dry!")
    if max(tmax)>33:
        st.warning(f"🔥 Heat stress {max(tmax)}°C in {town} - Give {animal} shade & extra water!")

    # Animal clinic
    st.divider()
    st.subheader("🔬 Animal Clinic")
    photo2 = st.file_uploader("📸 Upload sick animal", type=["jpg","png","jpeg"], key="animal")
    if photo2: st.image(photo2)
    symp2 = st.multiselect("Symptoms:", ["Lumps on skin","Coughing","Diarrhea","Not eating","Limping","Eyes watery","White spots mouth","Feathers falling"])
    if st.button("Diagnose Animal"):
        if "Lumps on skin" in symp2: st.error("🚨 LUMPY SKIN DISEASE! Isolate! Call Vet URGENT!")
        elif "White spots mouth" in symp2: st.error("🚨 FOOT & MOUTH! Report to State Vet ASAP! Very contagious!")
        elif "Coughing" in symp2: st.warning(f"{animal} flu/infection - Terramycin + vet check")
        elif "Diarrhea" in symp2: st.warning("Worms/coccidiosis - Deworm, clean water")
        else: st.info("Isolate, give water, call vet")

    # Animal specific
    st.divider()
    st.subheader("🥛 Production Tip")
    if animal=="Cattle": st.info("Rainy week? Don't let cattle graze wet grass - causes bloat!")
    if animal.startswith("Chickens"): st.info(f"Wet weather {sum(rain)}mm in {town} - Keep chicken house dry, add sawdust to prevent disease")

else: # Mixed
    st.subheader(f"🌾🐄 Mixed Farming Dashboard: {town}")
    st.info("You do both! App will give you BOTH crop + animal alerts!")
    col1,col2 = st.columns(2)
    with col1:
        st.write("**🌽 Crop Alert**")
        if max(rain)>15: st.warning(f"Fungus risk {sum(rain)}mm")
        else: st.success("Crops OK")
    with col2:
        st.write("**🐄 Animal Alert**")
        if town in ["Magudu","Tonga"]: st.error("Lumpy Skin risk - vaccinate!")
        else: st.success("Animals OK")

    st.divider()
    st.write("🔬 Use clinic below - choose what's sick")
    sick_what = st.selectbox("What's sick today?", ["Crop", "Animal"])
    if sick_what=="Crop":
        symp = st.multiselect("Crop Symptoms:", ["Holes/worms","Yellow leaves","White powder"])
        if st.button("Diagnose"): st.warning("Check Fall Armyworm if holes - Ampligo R250")
    else:
        symp2 = st.multiselect("Animal Symptoms:", ["Lumps","Coughing","Diarrhea"])
        if st.button("Diagnose Animal 2"): st.error("If lumps = Lumpy Skin, call vet!")

# COMMON: Weather + Market + Profit
st.divider()
st.subheader(f"🌦️ {town} Weather: {rain}")
if rain[1]>8: st.error(f"🚚 Tomorrow {rain[1]}mm - Market bad!")
else: st.success(f"✅ Market good tomorrow - {rain[1]}mm")

st.divider()
st.subheader("💰 Profit Calc")
c1,c2 = st.columns(2)
with c1: cost = st.number_input("Cost R", value=100)
with c2: income = st.number_input("Income R", value=300)
if st.button("Calc", type="primary"):
    if income-cost>0: st.balloons(); st.success(f"PROFIT R{income-cost}")
    else: st.error(f"LOSS R{income-cost}")

st.caption(f"AgriPro Mzansi | {farming_type} Mode | {town} | 16yo Founder Magudu"
