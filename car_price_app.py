import streamlit as st
import pickle
import pandas as pd
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))
st.title("🚗 Car Price Predictor App")
st.text(
    "This app predicts the estimated selling price "
    "of a used car based on its specifications."
)
year = st.slider(
    "Manufacturing Year",
    min_value=int(df['year'].min()),
    max_value=2026,
    value=2018,
    step=1
)
km_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=int(df['km_driven'].max()),
    value=50000,
    step=1000
)
fuel = st.selectbox(
    "Fuel Type",
    df['fuel'].unique()
)
seller_type = st.selectbox(
    "Seller Type",
    df['seller_type'].unique()
)
transmission = st.radio(
    "Transmission Type",
    df['transmission'].unique(),
    horizontal=True
)
owner = st.selectbox(
    "Number of Previous Owners",
    df['owner'].unique()
)
car_age = 2026 - year
st.write("Car Age:", car_age, "years")
if st.button("PREDICT PRICE"):

    query = pd.DataFrame({
        'year': [year],
        'km_driven': [km_driven],
        'fuel': [fuel],
        'seller_type': [seller_type],
        'transmission': [transmission],
        'owner': [owner],
        'car_age': [car_age]
    })

    op = pipe.predict(query)

    st.subheader(
        f"Estimated Car Price: ₹{int(round(op[0], -2)):,}"
    )
