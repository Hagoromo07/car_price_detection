import joblib
import pandas as pd

from .header import MODEL_COLUMNS


def get_model():
    """
    Load the pre-trained model from the specified path.
    """
    model_path = "/app/models/random_forest1.pkl"
    return joblib.load(model_path)


def preprocessing_user_input(data):
    """
    Preprocess user input data to match the model's expected format.
    This includes creating a dictionary with default values and updating it
    with user-provided values.
    """
    selected_features = (
        extract_list("comfort_convenience", data)
        + extract_list("entertainment_media", data)
        + extract_list("extras", data)
        + extract_list("safety_security", data)
    )

    input_dict = MODEL_COLUMNS.copy()

    if user_model := data.get("make_model", ""):
        input_dict[user_model] = 1

    if user_body_type := data.get("body_type", ""):
        input_dict[user_body_type] = 1

    if user_fuel := data.get("fuel", ""):
        input_dict[user_fuel] = 1

    if user_type := data.get("type", ""):
        input_dict[user_type] = 1

    if user_paint_type := data.get("pain_type", ""):
        input_dict[user_paint_type] = 1

    if user_upholstery_type := data.get("upholstery_type", ""):
        input_dict[user_upholstery_type] = 1

    if user_gearing_type := data.get("gearing_type", ""):
        input_dict[user_gearing_type] = 1

    if user_drive_chain := data.get("drive_chain", ""):
        input_dict[user_drive_chain] = 1

    input_dict.update(
        {
            "km": float(data.get("km", 0)),
            "Gears": data.get("gears"),
            "age": float(data.get("age", 0)),
            "Displacement_cc": float(data.get("displacement_cc", 0)),
            "Weight_kg": float(data.get("weight_kg", 0)),
            "cons_comb": float(data.get("cons_comb", 0)),
        }
    )

    for feature in selected_features:
        input_dict[feature] = 1 if feature in input_dict else 0

    return input_dict


def build_df_():
    """
    Build a DataFrame from the preprocessed user input.
    """
    link = "https://docs.google.com/spreadsheets/d/1QWr-Z3BuB3381rryerMpiJAFHVy2iSJb3J-CJcqRCyo/export?format=csv"
    return pd.read_csv(link)


def _convert_to_list(column_name):
    """
    Convert a DataFrame column to a list.
    """
    result = []
    df = build_df_()
    for line in df[column_name]:
        result += line.split(",")

    return [x.strip() for x in list(set(result))]


def df_to_unique_list(column_name):
    """
    Convert a DataFrame column to a list.
    """
    df = build_df_()
    return df[column_name].unique().tolist()


def extract_list(key, data):
    val = data.get(key, [])
    return val if isinstance(val, list) else [val]


def build():
    return CONFORM


df = build_df_()
MODEL = get_model()
