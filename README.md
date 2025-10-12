# 🌱 Crop Yield and Revenue Prediction System

A machine learning web application that predicts the best crop to grow based on soil and climate conditions, along with expected yield, price, and revenue calculations.

## 📋 Project Overview

This project uses machine learning algorithms to help farmers make informed decisions about crop selection by analyzing:
- **Soil nutrients** (Nitrogen, Phosphorus, Potassium, pH)
- **Climate conditions** (Temperature, Humidity, Rainfall)
- **Economic factors** (Yield prediction, Price estimation, Revenue calculation)

## 🔄 Migration: Streamlit → Flask

This project was **converted from Streamlit to Flask** to provide more control over the web interface and better deployment options.

### What Changed:

#### **Before (Streamlit):**
- Single `crop_app.py` file with embedded UI
- Streamlit's built-in widgets and layout
- Limited customization options
- Automatic UI generation

#### **After (Flask):**
- **Separated concerns** into multiple files
- **Custom HTML/CSS/JavaScript** frontend
- **RESTful API** backend
- **Better performance** and scalability

## 📁 Project Structure

```
CROP_RECOMMENDATION/
├── app.py                          # Flask backend server
├── model.py                        # ML logic and model training
├── templates/
│   └── index.html                  # Frontend HTML interface
├── static/
│   ├── style.css                   # CSS styling
│   └── script.js                   # JavaScript functionality
├── requirements.txt                # Python dependencies
├── Updated_Crop_Yield_Prediction.xlsx  # Training data
└── README.md                       # This file
```

## 🚀 How to Run

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone or download the project**
2. **Navigate to the project directory:**
   ```bash
   cd CROP_RECOMMENDATION
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

## 🛠️ Technical Details

### Backend (Flask)
- **Framework:** Flask with CORS support
- **API Endpoint:** `POST /predict`
- **Data Format:** JSON input/output
- **ML Models:** Random Forest (Classifier + Regressors)

### Frontend (HTML/CSS/JavaScript)
- **Responsive Design:** Works on desktop and mobile
- **AJAX Requests:** No page reloads
- **Modern UI:** Clean, professional interface
- **Real-time Feedback:** Loading states and error handling

### Machine Learning
- **Algorithm:** Random Forest
- **Features:** 7 input parameters
- **Outputs:** Crop recommendation, yield, price, revenue
- **Data Source:** Excel file with agricultural data

## 📊 Input Parameters

| Parameter | Range | Description |
|-----------|-------|-------------|
| Nitrogen | 0-1000 | Soil nitrogen content |
| Phosphorus | 0-1000 | Soil phosphorus content |
| Potassium | 0-1000 | Soil potassium content |
| Temperature | -50 to 60°C | Average temperature |
| Humidity | 0-100% | Relative humidity |
| pH Value | 0-14 | Soil acidity/alkalinity |
| Rainfall | 0-500 mm | Annual rainfall |

## 📈 Output Results

- **Recommended Crop:** Best crop for given conditions
- **Expected Yield:** Predicted yield in quintals per 100 acres
- **Expected Price:** Market price in ₹/quintal
- **Expected Revenue:** Revenue per acre in ₹

## 🔧 Key Improvements from Streamlit

### 1. **Better Architecture**
- **Separation of Concerns:** ML logic, backend, and frontend
- **Modular Design:** Easy to maintain and extend
- **API-First:** Can be integrated with other applications

### 2. **Enhanced User Experience**
- **Custom UI:** Professional, modern interface
- **Better Performance:** Faster loading and responses
- **Mobile Responsive:** Works on all devices
- **Real-time Updates:** No page refreshes needed

### 3. **Developer Benefits**
- **Full Control:** Complete customization of UI/UX
- **Better Debugging:** Clear separation of frontend/backend
- **Scalability:** Easy to add new features
- **Deployment:** Better options for production deployment

### 4. **Technical Advantages**
- **RESTful API:** Standard web service architecture
- **CORS Support:** Cross-origin requests handled
- **Error Handling:** Comprehensive error management
- **Loading States:** Better user feedback

## 🎯 Features

- ✅ **Smart Crop Recommendation**
- ✅ **Yield Prediction**
- ✅ **Price Estimation**
- ✅ **Revenue Calculation**
- ✅ **Real-time Analysis**
- ✅ **Mobile Responsive**
- ✅ **Error Handling**
- ✅ **Loading Indicators**

## 🔍 API Documentation

### POST /predict

**Request Body:**
```json
{
  "Nitrogen": 40.0,
  "Phosphorus": 50.0,
  "Potassium": 60.0,
  "Temperature": 33.0,
  "Humidity": 60.0,
  "pH_Value": 7.0,
  "Rainfall": 200.0
}
```

**Response:**
```json
{
  "success": true,
  "prediction": {
    "crop": "Rice",
    "yield": 45.2,
    "price": 1800.5,
    "revenue": 814.5
  }
}
```

## 🚀 Deployment Options

### Local Development
```bash
python app.py
```

### Production Deployment
- **Heroku:** Easy deployment with Procfile
- **AWS:** EC2, Elastic Beanstalk
- **Google Cloud:** App Engine, Cloud Run
- **Docker:** Containerized deployment

## 📝 Dependencies

```
flask==2.3.3
flask-cors==4.0.0
pandas==2.0.3
scikit-learn==1.3.0
openpyxl==3.1.2
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Data Source:** Agricultural yield prediction dataset
- **ML Framework:** Scikit-learn
- **Web Framework:** Flask
- **Frontend:** HTML5, CSS3, JavaScript ES6+

---

**Note:** This project was successfully migrated from Streamlit to Flask, providing better performance, customization, and deployment options while maintaining all original functionality.
