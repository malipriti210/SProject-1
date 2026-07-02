import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Real Estate Price Estimation System",
    page_icon="🏠",
    layout="wide"
)

# -------------------------------
# Load Model
# -------------------------------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
.main{
    background-color:#f5f7fa;
}
h1{
    color:#0E76A8;
    text-align:center;
}
.stButton>button{
    width:100%;
    background-color:#0E76A8;
    color:white;
    font-size:18px;
    border-radius:10px;
}
.stButton>button:hover{
    background-color:#05445E;
    color:white;
}
.result{
    background-color:#d4edda;
    padding:20px;
    border-radius:10px;
    text-align:center;
    font-size:30px;
    color:#155724;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("📌 Project Information")
st.sidebar.write("### Real Estate Price Estimation System")
st.sidebar.write("**Algorithm:** Linear Regression")
st.sidebar.write("**Dataset:** California Housing Dataset")
st.sidebar.write("**Language:** Python")
st.sidebar.write("**Framework:** Streamlit")
st.sidebar.write("**Library:** Scikit-Learn")

# -------------------------------
# Title
# -------------------------------
st.title("🏠 Real Estate Price Estimation System")

st.write("""
Estimate the property price using Machine Learning.

Fill in the property details below and click **Predict Price**.
""")

# -------------------------------
# Input Fields
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    med_inc = st.number_input(
        "Median Income",
        min_value=0.0,
        value=4.5,
        step=0.1
    )

    house_age = st.number_input(
        "House Age",
        min_value=1,
        value=30
    )

    ave_rooms = st.number_input(
        "Average Rooms",
        min_value=1.0,
        value=5.0,
        step=0.1
    )

    ave_bedrooms = st.number_input(
        "Average Bedrooms",
        min_value=0.1,
        value=1.0,
        step=0.1
    )

with col2:
    population = st.number_input(
        "Population",
        min_value=1,
        value=1000
    )

    ave_occup = st.number_input(
        "Average Occupancy",
        min_value=0.1,
        value=3.0,
        step=0.1
    )

    latitude = st.number_input(
        "Latitude",
        value=37.88
    )

    longitude = st.number_input(
        "Longitude",
        value=-122.23
    )

# -------------------------------
# Prediction
# -------------------------------
if st.button("🔍 Predict Price"):

    input_df = pd.DataFrame({
        "MedInc": [med_inc],
        "HouseAge": [house_age],
        "AveRooms": [ave_rooms],
        "AveBedrms": [ave_bedrooms],
        "Population": [population],
        "AveOccup": [ave_occup],
        "Latitude": [latitude],
        "Longitude": [longitude]
    })

    try:
        prediction = model.predict(input_df)

        # Convert from $100,000 units to USD
        estimated_price = prediction[0] * 100000

        st.success("Prediction Successful!")

        st.markdown(
            f"""
            <div class="result">
                🏠 Estimated Property Price<br><br>
                💲 ${estimated_price:,.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error("Prediction Failed")
        st.write(e)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Developed using Python, Scikit-Learn and Streamlit")
