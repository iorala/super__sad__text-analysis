# benötigte Module importieren
from flask import Flask, redirect
from flask import render_template
from flask import request
from collections import defaultdict
import pandas as pd

# Komponenten laden

# Custom Funktionen für die Benutzeroberfläche
from Komponenten.UI.ui_funktionen import bs_tabelle_aus_df

# Datenimport

# Textanalyse
from Komponenten.Textanalyse.Corpus import Corpus
from Komponenten.Textanalyse.Sentiment import Sentiments
# Visualisierung
from Komponenten.Visualisierung.DataVisualiser import DataVisualizer

# Export
from Komponenten.Export.Export import Export
from Komponenten.Export.Image_data import ImageData
from Komponenten.Export.PNG_Exporter import PNGExporter



# name der Applikation
app = Flask("super__sad__text_analysis")

# Globale Variablen und Funktionen
app_titel = "super().__sad__(text_analysis)"
variable = "Inhalt"


# GUI entwickeln:
#
# - Mit Sessions arbeiten (nicht-Permanent)
# - Testen, ob mit Sessions Objekte von einer App-Route an eine andere Weitergegeben werden können
# - Keine Unittests
# - Bootstrap

# @app.name_der_Funktion()
#
# def funktion():
#   return "x"

#
# Webseiten
#

@app.route('/test/<eingabe>')
# For testing
def hello_world(eingabe):
    return eingabe


# Main: Upload Page:
# FORM → Request and view upload
@app.route('/')
def home():
    titel = "Textanalyse"
    return render_template("main.html", titel=titel)


# - View Upload
#     - Verarbeitet upload
#     - Zeigt Tabelle mit dem HEAD der Daten
#     - →Button für Versand an Sentiment Analysis
@app.route('/import_anzeigen', methods=["GET", "POST"])
def import_anzeigen():
    titel = "Importierte Text"
    if request.method == "POST":
        csv_datei = request.files['csv_datei']
        csv_inhalt = pd.read_csv(csv_datei, sep=",", names=["Texte"])
        csv_tabelle = bs_tabelle_aus_df(csv_inhalt)
    return render_template("import_anzeigen.html", titel=titel, csv_tabelle=csv_tabelle)


# - Sentiment Analysis
#     - Führt die Sentiment analyse durch
#     - Zeigt Daten HEAD (gleiche Zeilen) mit dem Sentiment wert
#     - → Button für Visualize
@app.route('/textanalyse', methods=["GET", "POST"])
def textanalyse():
    # Blah blah
    return render_template("textanalyse.html")


# - Visualize
#     - Führt die Visualisierung durch
#     - Zeigt die Visualisierung an
#     - → Button für Save
#     - Speichert Visualisierung als PNG
#     - Eventuell hat Korpus eine Funktion speichern als CSV (?)
#
@app.route('/visualisierung', methods=["GET", "POST"])
def visualisierung():
    # Blah blah
    return render_template("visualisierung.html")


# Template
@app.route('/name_seite', methods=["GET", "POST"])
def name_seite():
    # Blah blah
    return render_template("name_seite.html")


#
# App Ausführen
#
if __name__ == "__main__":
    app.run(debug=True, port=5000)
