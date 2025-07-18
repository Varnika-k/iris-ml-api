from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# --- Load the pre-trained model ---
# This path assumes logistic_regression_iris_model.pkl is in the same directory as app.py
try:
    model = joblib.load('logistic_regression_iris_model.pkl')
    # Also load target names for human-readable output
    # (Assuming you know the order from your training script, e.g., Setosa, Versicolor, Virginica)
    iris_target_names = ['setosa', 'versicolor', 'virginica']
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None # Indicate model loading failed

@app.route('/')
def home():
    return "ML Model Prediction API is running. Send POST requests to /predict."

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded. Check server logs."}), 500

    try:
        # Get data from request
        data = request.get_json(force=True) # force=True to handle cases where Content-Type might not be exactly 'application/json'
        features = data['features'] # Expects a list of 4 numbers, e.g., [5.1, 3.5, 1.4, 0.2]

        # Convert to numpy array for prediction
        input_array = np.array([features])

        # Make prediction
        prediction_index = model.predict(input_array)[0]
        predicted_class_name = iris_target_names[prediction_index]

        return jsonify({
            "input_features": features,
            "predicted_class_index": int(prediction_index), # Convert to int for JSON serialization
            "predicted_class_name": predicted_class_name
        })
    except KeyError:
        return jsonify({"error": "Invalid input format. Expected JSON with a 'features' key containing a list of 4 numbers."}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

if __name__ == '__main__':
    # Use 0.0.0.0 to make it accessible externally when deployed
    # Port 5000 is default for Flask, but cloud services might use different ports (e.g., 8080)
    # Use PORT environment variable when deploying
    app.run(host='0.0.0.0', port=5000)
