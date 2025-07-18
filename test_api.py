{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3e6319d5-ad5f-499e-8b73-cbfe56843420",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'input_features': [5.1, 3.5, 1.4, 0.2], 'predicted_class_index': 0, 'predicted_class_name': 'setosa'}\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import json\n",
    "\n",
    "url = 'http://localhost:5000/predict'\n",
    "headers = {'Content-Type': 'application/json'}\n",
    "# Sample input for a Setosa flower\n",
    "data = {'features': [5.1, 3.5, 1.4, 0.2]}\n",
    "\n",
    "try:\n",
    "    response = requests.post(url, headers=headers, data=json.dumps(data))\n",
    "    response.raise_for_status() # Raise an exception for HTTP errors\n",
    "    print(response.json())\n",
    "except requests.exceptions.RequestException as e:\n",
    "    print(f\"Error making request: {e}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "932e2f58-3b28-4564-9a5a-9650d4132921",
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
