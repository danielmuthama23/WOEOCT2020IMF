import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load model and important features
model = joblib.load("model/gdp_forecast_model.pkl")
top_features = joblib.load("model/top_features.pkl")

# Continent encoding configuration
CONTINENT_ORDER = [
    "Continent_", "Continent_Africa", "Continent_Asia",
    "Continent_Europe", "Continent_North America",
    "Continent_Oceania", "Continent_South America"
]

@app.route("/", methods=["POST"])
def predict_gdp():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ["continent", "population"] + top_features
        if not all(field in data for field in required_fields):
            return jsonify({
                "error": f"Missing required fields. Required: {required_fields}",
                "received": list(data.keys())
            }), 400

        # One-hot encode continent
        continent = f"Continent_{data['continent'].strip()}"
        if continent not in CONTINENT_ORDER:
            return jsonify({"error": f"Invalid continent '{data['continent']}'. Valid options: {[c.replace('Continent_', '') for c in CONTINENT_ORDER[1:]]}"}), 400
            
        continent_vector = [0] * len(CONTINENT_ORDER)
        continent_vector[CONTINENT_ORDER.index(continent)] = 1

        # Prepare feature vector
        numeric_features = [float(data[feat]) for feat in top_features]
        full_features = numeric_features + continent_vector

        # Make prediction
        prediction = model.predict([full_features])[0]
        
        return jsonify({
            "gdp_prediction": round(float(prediction), 2),
            "features_used": top_features,
            "continent_encoding": continent
        })
        
    except Exception as e:
        return jsonify({
            "error": "Server error",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)