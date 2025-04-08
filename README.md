# 🌾 Hybrid Crop Recommendation and Production Prediction System

An intelligent agriculture system that combines historical data lookup with machine learning to provide accurate crop recommendations and production predictions.

## 📋 Overview

This project addresses two critical agricultural challenges:

- Predicting crop production yields based on regional and seasonal factors
- Recommending optimal crops based on soil and climate conditions

The system employs a hybrid approach, utilizing both historical data matching and machine learning models to ensure maximum accuracy.

## ✨ Features

- Production Prediction: Estimates crop yield in tonnes using Random Forest Regression
- Crop Recommendation: Suggests suitable crops using Random Forest Classification
- Smart Lookup System: Prioritizes historical data matches before ML predictions
- Region-specific insights based on state and district-level data

## 🛠️ Technologies Used

- Python 3.x
- Pandas for data manipulation
- Scikit-learn for machine learning models
- RandomForestRegressor for production prediction
- RandomForestClassifier for crop recommendation

## 📊 Dataset Description

The system utilizes comprehensive agricultural datasets with the following features:

### Production Dataset Columns:

```python
- State_Name: State where cultivation occurs
- District_Name: Specific district location
- Crop_Year: Year of cultivation
- Season: Growing season (Kharif/Rabi/Summer)
- Crop: Type of crop
- Area: Cultivation area in hectares
- Production: Yield in tonnes

```

### Recommendation Dataset Features:

```python
- Soil_Type: Soil classification
- pH: Soil pH level
- Rainfall: Annual rainfall in mm
- Temperature: Average temperature
- Humidity: Relative humidity percentage

```

## ⚙️ How It Works

### Data Preprocessing

1. Data cleaning and normalization
2. Handling missing values and outliers
3. Feature engineering for seasonal patterns
4. Encoding categorical variables

### Smart Lookup Logic

```python
def predict_production(input_parameters):
    # Check historical data first
    historical_match = find_similar_entry(input_parameters)
    
    if historical_match and within_tolerance(historical_match):
        return historical_match.production
    
    # Fallback to ML prediction
    return rf_model.predict(input_parameters)

```

## 📝 Input/Output Example

```python
# Sample Input
input_data = {
    "State_Name": "Karnataka",
    "District_Name": "Mysore",
    "Crop_Year": 2024,
    "Season": "Kharif",
    "Crop": "Rice",
    "Area": 100
}

# Sample Output
{
    "Predicted_Production": 450.75,  # tonnes
    "Recommended_Crops": ["Rice", "Maize", "Groundnut"],
    "Confidence_Score": 0.89
}

```
### Screenshots
<img width="1439" alt="Screenshot 2025-04-08 at 2 52 25 AM" src="https://github.com/user-attachments/assets/2002e181-1862-4b91-804a-912d9b3e83e7" /><img width="1439" alt="Screenshot 2025-04-08 at 2 52 25 AM" src="https://github.com/user-attachments/assets/e95b9188-f279-42a8-8910-6bdbff68c334" />
## 🚀 How to Run

### Installation

```bash
git clone https://github.com/yourusername/crop-prediction-system.git
cd crop-prediction-system
pip install -r requirements.txt

```

### Running the System

```bash
python src/main.py

```

## 📁 Folder Structure

```
crop-prediction-system/
├── data/
│   ├── raw/
│   └── processed/
├── models/
│   ├── production_model.pkl
│   └── recommendation_model.pkl
├── notebooks/
│   └── model_development.ipynb
├── src/
│   ├── preprocessing/
│   ├── models/
│   └── utils/
├── tests/
├── README.md
└── requirements.txt

```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

<aside>
For more information or support, please open an issue on GitHub or contact the maintainers.

</aside>
