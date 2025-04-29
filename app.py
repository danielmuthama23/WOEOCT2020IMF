import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load model and features
model = joblib.load("model/gdp_forecast_model.pkl")
top_features = joblib.load("model/top_features.pkl")

# Define continent encoding
CONTINENT_ORDER = [
    "Continent_", "Continent_Africa", "Continent_Asia",
    "Continent_Europe", "Continent_North America",
    "Continent_Oceania", "Continent_South America"
]

@app.route("/", methods=["POST"])
def predict_gdp():
    try:
        data = request.get_json()

        # Validate input
        required_fields = ["continent", "population"] + top_features
        if not all(field in data for field in required_fields):
            return jsonify({"error": f"Missing fields. Required: {required_fields}"}), 400

        # One-hot encode continent
        continent = f"Continent_{data['continent'].strip()}"
        continent_vector = [0] * len(CONTINENT_ORDER)
        if continent in CONTINENT_ORDER:
            continent_vector[CONTINENT_ORDER.index(continent)] = 1
        else:
            return jsonify({"error": f"Invalid continent '{data['continent']}'"}), 400

        # Prepare feature vector
        numeric_features = [float(data[feat]) for feat in top_features]
        full_input = numeric_features + continent_vector

        prediction = model.predict([full_input])[0]
        return jsonify({
            "gdp_per_capita_prediction": round(float(prediction), 2),
            "features_used": top_features
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
