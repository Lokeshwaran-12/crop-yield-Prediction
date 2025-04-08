import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Set page configuration
st.set_page_config(page_title="Agricultural Assistant", page_icon="🌱", layout="wide")

# Helper function to provide information about crops
def get_crop_info(crop_name):
    """Return basic information about the recommended crop"""
    crop_info = {
        "rice": "Rice requires plenty of water and warm conditions. Best suited for humid regions with temperatures between 20-40°C.",
        "wheat": "Wheat grows well in moderately cool climates with about 30-100 cm of annual rainfall.",
        "maize": "Maize (corn) needs lots of sunlight and warm soil. Requires moderate rainfall and well-drained soil.",
        "chickpea": "Chickpeas thrive in cool, dry climates and can tolerate drought conditions.",
        "kidney beans": "Kidney beans prefer warm temperatures and moderate rainfall, with well-drained soil.",
        "pigeonpeas": "Pigeon peas are drought-resistant and grow well in semi-arid regions.",
        "mothbeans": "Moth beans are extremely drought-resistant and suitable for arid regions.",
        "mungbean": "Mung beans grow best in warm climates with moderate rainfall.",
        "blackgram": "Black gram requires warm, humid conditions and moderate rainfall.",
        "lentil": "Lentils prefer cool growing seasons and moderate rainfall.",
        "pomegranate": "Pomegranate trees thrive in semi-arid to arid climates with hot summers.",
        "banana": "Bananas need tropical conditions with high humidity and rainfall.",
        "mango": "Mangoes grow best in tropical climates with a distinct dry season.",
        "grapes": "Grapes prefer temperate climates with warm, dry summers and mild winters.",
        "watermelon": "Watermelons need lots of sun and warm soil, with moderate water.",
        "muskmelon": "Muskmelons require warm temperatures and well-drained soil.",
        "apple": "Apples grow best in temperate climates with cold winters and moderate summers.",
        "orange": "Oranges thrive in subtropical climates with mild winters.",
        "papaya": "Papayas need tropical or subtropical conditions with no frost.",
        "coconut": "Coconuts require tropical climates with high humidity and rainfall.",
        "cotton": "Cotton grows best in warm climates with moderate rainfall.",
        "jute": "Jute requires high rainfall and humid conditions.",
        "coffee": "Coffee grows best in tropical highlands with moderate temperatures."
    }
    
    return crop_info.get(crop_name.lower(), "Information not available for this crop.")

# Create sidebar for navigation
st.sidebar.title("🌾 Agricultural Assistant")
page = st.sidebar.radio("Choose a Tool:", ["Crop Recommendation", "Crop Production Prediction"])

# Crop Recommendation Page
if page == "Crop Recommendation":
    # Load crop recommendation model
    try:
        model = joblib.load("/Users/lokeshwarans/Downloads/science/crop_recommendation_rf_model.pkl")
    except:
        st.warning("⚠️ Model file not found. Please ensure the path is correct or upload your model file.")
        model = None

    # UI for crop recommendation
    st.title("🌾 Intelligent Crop Recommendation System")
    st.subheader("Get the best crop suggestion for your field!")

    # Create two columns for input fields
    col1, col2 = st.columns(2)

    with col1:
        st.write("### 📋 Soil Nutrients")
        n = st.number_input("Nitrogen (N)", min_value=0.0, max_value=140.0, value=50.0, 
                           help="Amount of nitrogen in the soil (mg/kg)")
        p = st.number_input("Phosphorus (P)", min_value=0.0, max_value=145.0, value=50.0,
                           help="Amount of phosphorus in the soil (mg/kg)")
        k = st.number_input("Potassium (K)", min_value=0.0, max_value=205.0, value=50.0,
                           help="Amount of potassium in the soil (mg/kg)")
        ph = st.number_input("pH Level", min_value=3.0, max_value=10.0, value=6.5,
                            help="pH level of the soil")

    with col2:
        st.write("### 📋 Environmental Conditions")
        temp = st.number_input("Temperature (°C)", min_value=10.0, max_value=50.0, value=25.0,
                              help="Average temperature in Celsius")
        humidity = st.number_input("Humidity (%)", min_value=10.0, max_value=100.0, value=60.0,
                                  help="Relative humidity percentage")
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=100.0,
                                  help="Annual rainfall in millimeters")

    # Prediction
    if st.button("🔍 Recommend Crop", use_container_width=True):
        if model:
            input_data = pd.DataFrame([[n, p, k, temp, humidity, ph, rainfall]], 
                                    columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

            prediction = model.predict(input_data)[0]
            proba = model.predict_proba(input_data)[0]
            label_list = model.classes_

            # Create results container
            st.write("---")
            st.success(f"✅ Recommended Crop: **{prediction.upper()}**")

            # Display top 3 probable crops
            top_indices = np.argsort(proba)[::-1][:3]
            
            st.write("### 🔢 Top 3 Predictions with Probability:")
            
            # Display as progress bars
            for idx in top_indices:
                crop_name = label_list[idx]
                probability = proba[idx]
                st.write(f"**{crop_name.upper()}** ({probability*100:.2f}%)")
                st.progress(probability)
            
            # Additional information about the recommended crop
            st.write("### 📝 Crop Information")
            st.info(get_crop_info(prediction))
        else:
            st.error("Cannot make prediction without model. Please check model path.")

# Crop Production Prediction Page
else:
    # Load crop production model
    try:
        model = joblib.load("crop_producation_rf_model.pkl")
    except:
        st.warning("⚠️ Model file not found. Please ensure the path is correct or upload your model file.")
        model = None

    # UI for crop production prediction
    st.title("🌾 Crop Production Prediction")
    st.subheader("Predict crop yield (in tonnes) based on agricultural inputs")

    # Create input form with columns
    with st.form("prediction_form"):
        st.write("### 📋 Enter Crop Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            state = st.text_input("State Name")
            district = st.text_input("District Name")
            year = st.number_input("Crop Year", min_value=2000, max_value=2050, value=2023)
        
        with col2:
            season = st.selectbox("Season", ["Kharif", "Rabi", "Whole Year", "Summer", "Winter"], 
                                 help="Growing season for the crop")
            crop = st.text_input("Crop Name (e.g., Rice, Wheat, Maize)")
            area = st.number_input("Area in hectares", min_value=0.1, step=0.1, value=1.0)

        submit = st.form_submit_button("🔍 Predict Production", use_container_width=True)

    # When form is submitted
    if submit:
        if model:
            # Format user input as DataFrame
            user_input = pd.DataFrame([{
                'State_Name': state,
                'District_Name': district,
                'Crop_Year': year,
                'Season': season,
                'Crop': crop,
                'Area': area
            }])

            try:
                # Predict
                prediction = model.predict(user_input)
                
                # Create results container
                st.write("---")
                st.success(f"✅ Predicted Crop Production: **{prediction[0]:.2f} tonnes**")
                
                # Calculate and display yield per hectare
                yield_per_hectare = prediction[0] / area
                st.info(f"📊 Yield Efficiency: **{yield_per_hectare:.2f} tonnes per hectare**")
                
                # Display a visualization of the prediction
                st.write("### Production Scale:")
                st.progress(min(prediction[0]/100, 1.0))  # Scale to max 100 tonnes for visualization
                
                # Compare with average yield
                st.write("### 📈 Production Analysis")
                st.write(f"Your predicted yield of **{yield_per_hectare:.2f} tonnes/hectare** for {crop} can be compared with typical yields for this crop in your region.")
                
            except Exception as e:
                st.error(f"⚠️ Prediction failed: {e}")
        else:
            st.error("Cannot make prediction without model. Please check model path.")