# import pickle, pandas, flask
import pickle
import pandas as pd
from flask import Flask, request

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

order = [
    "Continent_",
    "Continent_Africa",
    "Continent_Asia",
    "Continent_Europe",
    "Continent_North America",
    "Continent_Oceania",
    "Continent_South America",
]


@app.route("/", methods=["POST"])
def index():
    body = dict(request.get_json())

    features = [
        [
            body["Implied PPP conversion rate"],
            body["Population"],
            body["Year"],
            body["Current account balance"],
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
    ]

    continent = "Continent_" + body["Continent"]

    features[0][order.index(continent) + 4] = True

    result = model.predict(features)

    return str(result[0])


if __name__ == "__main__":
    app.run(debug=True)
