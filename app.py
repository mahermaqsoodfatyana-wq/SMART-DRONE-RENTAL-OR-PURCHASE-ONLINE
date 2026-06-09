import streamlit as st

st.set_page_config(
    page_title="ICT in Smart Agriculture",
    page_icon="🚁",
    layout="wide"
)

st.title("🚁 ICT in Smart Agriculture")
st.subheader("Smart Drone Purchase & Rental Platform for Farmers")

st.markdown("""
### About the Project

This platform helps farmers easily:

✅ Purchase agricultural drones online

✅ Rent drones for spraying and monitoring

✅ Compare drone prices and rental charges

✅ Submit booking requests digitally

This demonstrates the use of ICT (Information and Communication Technology)
in modern agriculture.
""")

st.header("Select Service")

service = st.radio(
    "Choose an Option",
    ["Purchase Drone", "Rent a Drone"]
)

if service == "Purchase Drone":

    st.header("🚁 Available Drones for Purchase")

    drone = st.selectbox(
        "Select Drone",
        [
            "Basic Spraying Drone",
            "Advanced Agriculture Drone",
            "Smart AI Drone"
        ]
    )

    prices = {
        "Basic Spraying Drone": 500000,
        "Advanced Agriculture Drone": 1200000,
        "Smart AI Drone": 2000000
    }

    st.success(f"Estimated Price: PKR {prices[drone]:,}")

    if st.button("Purchase Request"):
        st.success("Your drone purchase request has been submitted.")

else:

    st.header("🚁 Drone Rental Service")

    drone = st.selectbox(
        "Select Rental Drone",
        [
            "Basic Spraying Drone",
            "Advanced Agriculture Drone",
            "Smart AI Drone"
        ]
    )

    days = st.number_input(
        "Number of Rental Days",
        min_value=1,
        value=1
    )

    rental_rates = {
        "Basic Spraying Drone": 5000,
        "Advanced Agriculture Drone": 10000,
        "Smart AI Drone": 15000
    }

    total_rent = rental_rates[drone] * days

    st.info(f"Rental Cost: PKR {total_rent:,}")

    if st.button("Book Rental"):
        st.success("Your drone rental request has been submitted.")

st.header("📋 Farmer Information")

name = st.text_input("Farmer Name")
phone = st.text_input("Phone Number")
village = st.text_input("Village / City")

if st.button("Submit Details"):
    st.success("Farmer details submitted successfully.")

st.header("Benefits of Smart Agricultural Drones")

st.markdown("""
- Faster crop spraying
- Reduced labor costs
- Precision agriculture
- Crop health monitoring
- Increased productivity
- Efficient use of fertilizer and pesticides
""")

st.header("👨‍💻 Project Team")

st.markdown("""
**Maqsood Ahmad (25ME142)**

**M. Abdullah (25ME162)**

**M. Haseeb (54)**

**Azmat u Allah (25ME198)**

**Syed Sabih Gillani (25ME226)**
""")

st.success("ICT in Smart Agriculture - Drone Purchase & Rental System")
