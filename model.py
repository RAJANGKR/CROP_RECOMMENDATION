import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

class CropPredictor:
    def __init__(self):
        self.crop_model = None
        self.yield_model = None
        self.price_model = None
        self.label_encoder = None
        self.scaler = None
        self.is_trained = False
    
    def load_and_train(self, excel_file="Updated_Crop_Yield_Prediction.xlsx"):
        """Load data and train all models"""
        try:
            # Load data
            crop_data = pd.read_excel(excel_file)
            
            # Prepare features
            X = crop_data[['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity',
                          'pH_Value', 'Rainfall']]
            
            y_crop = crop_data['Crop']
            y_yield = crop_data['Yield']
            y_price = crop_data['Price']
            
            # Encode crop labels
            self.label_encoder = LabelEncoder()
            y_crop_encoded = self.label_encoder.fit_transform(y_crop)
            
            # Train crop classification model
            self.scaler = StandardScaler()
            X_train, X_test, y_train, y_test = train_test_split(X, y_crop_encoded, test_size=0.2, random_state=42)
            
            X_train_scaled = self.scaler.fit_transform(X_train)
            X_test_scaled = self.scaler.transform(X_test)
            
            self.crop_model = RandomForestClassifier(random_state=42)
            self.crop_model.fit(X_train_scaled, y_train)
            
            # Train yield prediction model
            X_train_y, X_test_y, y_train_y, y_test_y = train_test_split(X, y_yield, test_size=0.2, random_state=42)
            self.yield_model = RandomForestRegressor(random_state=42)
            self.yield_model.fit(X_train_y, y_train_y)
            
            # Train price prediction model
            X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X, y_price, test_size=0.2, random_state=42)
            self.price_model = RandomForestRegressor(random_state=42)
            self.price_model.fit(X_train_p, y_train_p)
            
            self.is_trained = True
            print("All models trained successfully!")
            
        except Exception as e:
            print(f"Error training models: {e}")
            raise e
    
    def predict_crop(self, data):
        """Predict crop, yield, price, and revenue based on input data"""
        if not self.is_trained:
            raise Exception("Models not trained yet. Call load_and_train() first.")
        
        # Convert input to DataFrame
        input_df = pd.DataFrame([data])
        input_scaled = self.scaler.transform(input_df)
        
        # Predict crop
        crop_encoded = self.crop_model.predict(input_scaled)
        crop_name = self.label_encoder.inverse_transform(crop_encoded)[0]
        
        # Predict yield and price
        predicted_yield = self.yield_model.predict(input_df)[0]
        predicted_price = self.price_model.predict(input_df)[0]
        
        # Calculate expected revenue (per 100 acres, so divide by 100 for per acre)
        expected_revenue = 0.01 * predicted_yield * predicted_price
        
        return {
            'crop': crop_name,
            'yield': round(predicted_yield, 2),
            'price': round(predicted_price, 2),
            'revenue': round(expected_revenue, 2)
        }

# Global predictor instance
predictor = CropPredictor()

def initialize_models():
    """Initialize and train all models"""
    predictor.load_and_train()

def predict_crop(data):
    """Wrapper function for crop prediction"""
    return predictor.predict_crop(data)
