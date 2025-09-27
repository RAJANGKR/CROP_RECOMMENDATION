import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor


# Load dataset
crop_data = pd.read_excel("Updated_Crop_Yield_Prediction.xlsx")

# Define features and targets
X = crop_data[['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'pH_Value', 'Rainfall']]
y_crop = crop_data['Crop']
y_yield = crop_data['Yield']
y_price = crop_data['Price']

# Encode crop labels
label_encoder = LabelEncoder()
y_crop_encoded = label_encoder.fit_transform(y_crop)

# Scale features for crop classification
scaler = StandardScaler()
X_train, X_test, y_train, y_test = train_test_split(X, y_crop_encoded, test_size=0.2, random_state=42)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train crop classification model
crop_model = RandomForestClassifier(random_state=42)
crop_model.fit(X_train_scaled, y_train)
st.write("✅ Crop Model Trained")

# Train yield prediction model
X_train_y, X_test_y, y_train_y, y_test_y = train_test_split(X, y_yield, test_size=0.2, random_state=42)
yield_model = RandomForestRegressor(random_state=42)
yield_model.fit(X_train_y, y_train_y)
st.write("✅ Yield Model Trained")

# Train price prediction model
X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X, y_price, test_size=0.2, random_state=42)
price_model = RandomForestRegressor(random_state=42)
price_model.fit(X_train_p, y_train_p)
st.write("✅ Price Model Trained")


# Recommendation function
def recommend_crop_with_profit(input_features):
    input_df = pd.DataFrame([input_features])
    input_scaled = scaler.transform(input_df)

    crop_encoded = crop_model.predict(input_scaled)
    crop_name = label_encoder.inverse_transform(crop_encoded)[0]

    predicted_yield = yield_model.predict(input_df)[0]
    predicted_price = price_model.predict(input_df)[0]

    expected_revenue = 0.01 * predicted_yield * predicted_price  # Adjusted per 100 acres

    return crop_name, round(predicted_yield, 2), round(predicted_price, 2), round(expected_revenue, 2)


# Streamlit inputs
st.title("Crop Yield and Revenue Prediction")

nitrogen = st.number_input("Nitrogen", min_value=0.0, max_value=1000.0, value=40.0)
phosphorus = st.number_input("Phosphorus", min_value=0.0, max_value=1000.0, value=50.0)
potassium = st.number_input("Potassium", min_value=0.0, max_value=1000.0, value=60.0)
temperature = st.number_input("Temperature", min_value=-50.0, max_value=60.0, value=33.0)
humidity = st.number_input("Humidity", min_value=0.0, max_value=100.0, value=60.0)
ph_value = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=7.0)
rainfall = st.number_input("Rainfall", min_value=0.0, max_value=500.0, value=200.0)

user_input = {
    "Nitrogen": nitrogen,
    "Phosphorus": phosphorus,
    "Potassium": potassium,
    "Temperature": temperature,
    "Humidity": humidity,
    "pH_Value": ph_value,
    "Rainfall": rainfall
}

if st.button("Get Recommendation"):
    crop, yield_pred, price_pred, revenue = recommend_crop_with_profit(user_input)
    st.write(f"### Recommended Crop: {crop}")
    st.write(f"Expected Yield: {yield_pred} quintals / 100 ACRES")
    st.write(f"Expected Price: {price_pred} Rs/quintal")
    st.write(f"Expected Revenue: {revenue} Rs")
