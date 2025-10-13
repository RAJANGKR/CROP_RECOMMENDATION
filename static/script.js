// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('cropForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const submitBtn = document.getElementById('submitBtn');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const error = document.getElementById('error');
    
    submitBtn.disabled = true;
    submitBtn.textContent = 'Analyzing...';
    loading.style.display = 'block';
    results.style.display = 'none';
    error.style.display = 'none';
    
    const formData = {
        Nitrogen: parseFloat(document.getElementById('nitrogen').value),
        Phosphorus: parseFloat(document.getElementById('phosphorus').value),
        Potassium: parseFloat(document.getElementById('potassium').value),
        Temperature: parseFloat(document.getElementById('temperature').value),
        Humidity: parseFloat(document.getElementById('humidity').value),
        pH_Value: parseFloat(document.getElementById('ph_value').value),
        Rainfall: parseFloat(document.getElementById('rainfall').value)
    };
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('crop').textContent = data.prediction.crop;
            document.getElementById('yield').textContent = data.prediction.yield + ' quintals / 100 acres';
            document.getElementById('price').textContent = '₹' + data.prediction.price + ' /quintal';
            document.getElementById('revenue').textContent = '₹' + data.prediction.revenue + ' /acre';
            
            results.style.display = 'block';
        } else {
            throw new Error(data.error || 'Prediction failed');
        }
        
    } catch (err) {
        error.textContent = 'Error: ' + err.message;
        error.style.display = 'block';
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Get Recommendation';
        loading.style.display = 'none';
    }
    });
});