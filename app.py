{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "714de9b8-8fff-4c3b-a0a9-225dd30ce94d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: Flask in d:\\anaconda\\lib\\site-packages (3.1.0)\n",
      "Requirement already satisfied: Werkzeug>=3.1 in d:\\anaconda\\lib\\site-packages (from Flask) (3.1.3)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in d:\\anaconda\\lib\\site-packages (from Flask) (3.1.6)\n",
      "Requirement already satisfied: itsdangerous>=2.2 in d:\\anaconda\\lib\\site-packages (from Flask) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in d:\\anaconda\\lib\\site-packages (from Flask) (8.1.8)\n",
      "Requirement already satisfied: blinker>=1.9 in d:\\anaconda\\lib\\site-packages (from Flask) (1.9.0)\n",
      "Requirement already satisfied: colorama in d:\\anaconda\\lib\\site-packages (from click>=8.1.3->Flask) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in d:\\anaconda\\lib\\site-packages (from Jinja2>=3.1.2->Flask) (3.0.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92ecb183-39ea-4f35-8ca1-ca09366c4a26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model loaded successfully!\n",
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on all addresses (0.0.0.0)\n",
      " * Running on http://127.0.0.1:5000\n",
      " * Running on http://192.168.0.101:5000\n",
      "Press CTRL+C to quit\n",
      "192.168.0.101 - - [18/Jul/2025 23:41:08] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [18/Jul/2025 23:41:41] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# --- Load the pre-trained model ---\n",
    "# This path assumes model.pkl is in the same directory as app.py\n",
    "try:\n",
    "    model = joblib.load('logistic_regression_iris_model.pkl')\n",
    "    # Also load target names for human-readable output\n",
    "    # (Assuming you know the order from your training script, e.g., Setosa, Versicolor, Virginica)\n",
    "    iris_target_names = ['setosa', 'versicolor', 'virginica']\n",
    "    print(\"Model loaded successfully!\")\n",
    "except Exception as e:\n",
    "    print(f\"Error loading model: {e}\")\n",
    "    model = None # Indicate model loading failed\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return \"ML Model Prediction API is running. Send POST requests to /predict.\"\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    if model is None:\n",
    "        return jsonify({\"error\": \"Model not loaded. Check server logs.\"}), 500\n",
    "\n",
    "    try:\n",
    "        # Get data from request\n",
    "        data = request.get_json(force=True) # force=True to handle cases where Content-Type might not be exactly 'application/json'\n",
    "        features = data['features'] # Expects a list of 4 numbers, e.g., [5.1, 3.5, 1.4, 0.2]\n",
    "\n",
    "        # Convert to numpy array for prediction\n",
    "        input_array = np.array([features])\n",
    "\n",
    "        # Make prediction\n",
    "        prediction_index = model.predict(input_array)[0]\n",
    "        predicted_class_name = iris_target_names[prediction_index]\n",
    "\n",
    "        return jsonify({\n",
    "            \"input_features\": features,\n",
    "            \"predicted_class_index\": int(prediction_index), # Convert to int for JSON serialization\n",
    "            \"predicted_class_name\": predicted_class_name\n",
    "        })\n",
    "    except KeyError:\n",
    "        return jsonify({\"error\": \"Invalid input format. Expected JSON with a 'features' key containing a list of 4 numbers.\"}), 400\n",
    "    except Exception as e:\n",
    "        return jsonify({\"error\": f\"An unexpected error occurred: {e}\"}), 500\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    # Use 0.0.0.0 to make it accessible externally when deployed\n",
    "    # Port 5000 is default for Flask, but cloud services might use different ports (e.g., 8080)\n",
    "    # Use PORT environment variable when deploying\n",
    "    app.run(host='0.0.0.0', port=5000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e3b1dee-ceb2-4b7c-be6d-ed029704f257",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
