import pandas as pd
from flask import Blueprint, render_template, request, jsonify

from .header import MODEL_COLUMNS, FORMAT_COLUMNS
from .models import MODEL, preprocessing_user_input

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template(
        "index.html",
        **FORMAT_COLUMNS,
    )


@main.route("/predict", methods=["POST"])
def predict_rpc():
    print("Received data for prediction:", request.get_json())
    input_dict = preprocessing_user_input(request.get_json())
    input_df = pd.DataFrame([input_dict])
    print(len(MODEL_COLUMNS), len(input_df.columns))
    try:
        prediction = MODEL.predict(input_df.values)[0]
        print(f"Prediction: {prediction}")
        return jsonify({"prediction": round(float(prediction), 2)})
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500


@main.route("/result")
def result():
    return render_template(
        "result.html",
        marque="Peugeot",
        modele="208",
        annee=2020,
        kilometrage=30000,
        transmission="Manuelle",
        carburant="Essence",
        prediction=13250,
    )
