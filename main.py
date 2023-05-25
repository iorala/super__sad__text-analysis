# benötigte Module importieren
from flask import Flask, redirect, render_template, request, flash, session
import os
from collections import defaultdict
import pandas as pd
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'


# Komponenten laden

# Custom Funktionen für die Benutzeroberfläche
from Komponenten.UI.ui_funktionen import bs_tabelle_aus_df, upload_verzeichnis_erstellen

# Datenimport
from Komponenten.Import.Import_and_Control import DataImport, DataControl


# Textanalyse
from Komponenten.Textanalyse.Corpus import Corpus
from Komponenten.Textanalyse.Sentiment import Sentiments
# Visualisierung
from Komponenten.Visualisierung.DataVisualiser import DataVisualiser

# Export
from Komponenten.Export.Export import Export
from Komponenten.Export.Image_data import ImageData
from Komponenten.Export.PNG_Exporter import PNGExporter


# name der Applikation
app = Flask("super__sad__text_analysis")
app.secret_key = b'03dbdf2044be76908d840d4fa4de082d111708ce8ba4d2794ee9be0f4af45622'
UPLOAD_FOLDER = 'uploads/'
upload_verzeichnis_erstellen(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
        if 'csv_datei' not in request.files:
            flash('Keine Datei erhalten')
            return redirect(request.url)
        csv_datei = request.files['csv_datei']
        # wenn keine Datei ausgewählt wird, wir ein leerer string generiert
        if csv_datei.filename == '':
            flash('Keine Datei ausgewählt')
            return redirect(request.url)
        # Datei speichern
        dateiname = secure_filename(csv_datei.filename)
        csv_datei.save(os.path.join(app.config['UPLOAD_FOLDER'], dateiname))
        data_importer = DataImport()
        data_importer.import_data(os.path.join(app.config['UPLOAD_FOLDER'], dateiname))
        csv_tabelle = bs_tabelle_aus_df(data_importer.get_dataframe().head())
        return render_template("import_anzeigen.html", titel=titel, csv_tabelle=csv_tabelle)
    return("Keine Formular erhalten")


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
