from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import xgboost as xgb
import joblib

app = Flask(__name__)

# Load pre-trained models (assuming you saved them as .pkl files)
model = joblib.load('xgboost_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    features = [float(x) for x in request.form.values()]
    final_features = np.array(features).reshape(1, -1)
    scaled_features = scaler.transform(final_features)
    prediction = model.predict(scaled_features)
    
    return jsonify({'prediction': round(prediction[0], 2)})

if __name__ == "__main__":
    app.run(debug=True)
