import pandas as pd
import numpy as np
from flask import Blueprint, render_template
from flask import render_template

data_link = "https://docs.google.com/spreadsheets/d/1QWr-Z3BuB3381rryerMpiJAFHVy2iSJb3J-CJcqRCyo/export?format=csv"
main = Blueprint("main", __name__)


def _convert_to_list(df, column_name):
    """
    Convert a DataFrame column to a list.
    """
    result = []
    for line in df[column_name]:
        result += line.split(",")

    return [x.strip() for x in list(set(result))]


def df_to_unique_list(df, column_name):
    """
    Convert a DataFrame column to a list.
    """
    return df[column_name].unique().tolist()


@main.route("/")
def index():
    df                  = pd.read_csv(data_link)
    comfort_convenience = _convert_to_list(df, "Comfort_Convenience")
    entertainment_media = _convert_to_list(df, "Entertainment_Media")
    extras              = _convert_to_list(df, "Extras")
    safety_security     = _convert_to_list(df, "Safety_Security")
    fuel                = df_to_unique_list(df, "Fuel")
    type                = df_to_unique_list(df, "Type")
    body_type           = df_to_unique_list(df, "body_type")
    make_model          = df_to_unique_list(df, "make_model")
    pain_type           = df_to_unique_list(df, "Paint_Type")
    upholstery_type     = df_to_unique_list(df, "Upholstery_type")
    gearing_type        = df_to_unique_list(df, "Gearing_Type")
    displacement_cc     = 0  # upper than 0
    weight_kg           = 0  # upper than 0
    drive_chain         = df_to_unique_list(df, "Drive_chain")
    cons_comb           = df_to_unique_list(df, "cons_comb")
    age                 = 0  # upper than 0
    gears               = df_to_unique_list(df, "Gears")
    km                  = 0  # upper than 0
    return render_template(
        "index.html",
        comfort_convenience=comfort_convenience,
        entertainment_media=entertainment_media,
        extras=extras,
        safety_security=safety_security,
        fuel=fuel,
        type=type,
        body_type=body_type,
        make_model=make_model,
        pain_type=pain_type,
        upholstery_type=upholstery_type,
        gearing_type=gearing_type,
        displacement_cc=displacement_cc,
        weight_kg=weight_kg,
        drive_chain=drive_chain,
        cons_comb=cons_comb,
        age=age,
        gears=gears,
        km=km,
    )


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
