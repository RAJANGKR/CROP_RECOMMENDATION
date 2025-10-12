from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
from model import initialize_models, predict_crop

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Initialize models when the app starts
print("Initializing models...")
try:
    initialize_models()
    print("Models initialized successfully!")
except Exception as e:
    print(f"Error initializing models: {e}")

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 
                          'Humidity', 'pH_Value', 'Rainfall']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400
        
        # Make prediction
        result = predict_crop(data)
        
        return jsonify({
            'success': True,
            'prediction': result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
