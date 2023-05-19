# benötigte Module importieren
from flask import Flask, redirect
from flask import render_template
from flask import request
from collections import defaultdict

# name der Applikation
app = Flask("super__sad__text_analysis")

# Globale Variablen und Funktionen
variable = "Inhalt"

#GUI entwickeln:
#
# - Mit Sessions arbeiten (nicht-Permanent)
# - Testen ob mit Sessions Objekte von einer App-Route an eine andere Weitergegeben werden können
# - Keine Unittests
# - Bootstrap



# @app.name_der_Funktion()
#
#def funktion():
#   return "x"

#
# Webseiten
#

@app.route('/test/<variable>')
# For testing
def hello_world(variable):
    return variable


# Main: Upload Page:
# FORM → Request and view upload
@app.route('/')
def home():
    return render_template("main.html")


# - View Upload
#     - Verarbeitet upload
#     - Zeigt Tabelle mit dem HEAD der Daten
#     - →Button für Versand an Sentiment Analysis
@app.route('/import_anzeigen', methods=["GET", "POST"])
def import_anzeigen():
    # Blah blah
    return render_template("import_anzeigen.html")

# - Sentiment Analysis
#     - Führt die Sentiment analyse durch
#     - Zeigt Daten HEAD (gleiche Zeilen) mit dem Sentiment wert
#     - → Button für Visualize
@app.route('/textanalyse', methods=["GET", "POST"])
def name_seite():
    # Blah blah
    return render_template("textanalyse.html")

# - Visualize
#     - Führt die Visualisierung durch
#     - Zeigt die Visualisierung an
#     - → Button für Save
#     - Speichert Visualisierung als PNG
#     - EVTL: hat Korpus eine Funktion speichere als CSV (?)
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
