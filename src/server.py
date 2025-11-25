from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model
model_path = 'models/breast_cancer_model.pkl'
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print(f"✓ Model loaded from {model_path}")
else:
    print(f"✗ Model not found at {model_path}")
    model = None

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "model_loaded": model is not None}), 200

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    data = request.json.get('features', [])
    features = np.array(data).reshape(1, -1)
    prediction = int(model.predict(features)[0])
    
    return jsonify({"prediction": prediction}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)