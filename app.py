# benötigte Module importieren
from flask import Flask, render_template, request, session
import os
import uuid
import pandas as pd
from werkzeug.utils import secure_filename
import plotly.io as pio

# Komponenten laden

# Custom Funktionen für die Benutzeroberfläche
from Komponenten.UI.UI import VerzeichnisErstellen, UISentimentPipeline, TabelleAusDataframe, UIImportHandler

# Fehlermeldungen laden
from Komponenten.Constants import Constants
from Komponenten.Messages import Messages

# Datenimport
from Komponenten.Import.Import_and_Control import DataImport

# Visualisierung
from Komponenten.Visualisierung.DataVisualiser import VisualisationHandler

# Punkt-Tokenizer aus dem nltk-Modul importieren, da dieser für die Textanalyse benötigt wird
#  auf heroku von textblob_de nicht installiert
# https://devcenter.heroku.com/articles/python-nltk
# import nltk
# nltk.download('punkt')


# Globale Variablen und Funktionen
app_titel = "super().__sad__(text_analysis)"
variable = "Inhalt"
UPLOAD_FOLDER = 'uploads/'
# Objekt für die Fehlermeldungen erstellen
meldungen = Messages()

# Applikation initialisieren
app = Flask("super__sad__text_analysis")
app.secret_key = b'03dbdf2044be76908d840d4fa4de082d111708ce8ba4d2794ee9be0f4af45622'

# Verzeichnis zum Speichern der Nutzerdaten
VerzeichnisErstellen.erstellen(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#
# Webseiten
#

# Home: Text hochladen  :
# - Formular für Upload
# - Erklärt Format
@app.route('/')
def home():
    titel = "Texte hochladen"
    return render_template("main.html", titel=titel)


# - View Upload
#     - Verarbeitet upload
#     - Zeigt Tabelle mit dem HEAD der Daten
#     - →Button für Versand an Sentiment Analysis
# - ToDo: UI Code Reduzieren: CSV-Speichern als Klasse!
# -
@app.route('/import_anzeigen', methods=["GET", "POST"])
def import_anzeigen():
    titel = "Importierte Texte"
    if request.method == "POST":
        upload_datei = request.files['upload_datei']
        import_handler = UIImportHandler(UPLOAD_FOLDER, upload_datei)
        import_handler.import_datei()
        if import_handler.status != import_handler.constants.SUCCESS:
            return render_template("fehlermeldung.html", fehlermeldung=import_handler.fehlermeldung, titel="Fehler!")
        else:
            session['dateiname_csv'] = import_handler.dateiname_csv
            return render_template("import_anzeigen.html", titel=titel, csv_tabelle=import_handler.csv_tabelle)
    return home()  # Weiterleitung auf Hauptseite, wenn über Direktlink auf die Seite zugegriffen wird


# - Sentiment Analysis
#     - Führt die Sentiment-Analyse durch (in der ui_pipeline)
#     - Zeigt Daten HEAD (gleiche Zeilen) mit dem Sentiment wert
#     - Auswahl der gewünschten Visualisierung
# - ToDo: UI Code Reduzieren: CSV-Speichern als Klasse!
@app.route('/textanalyse', methods=["GET", "POST"])
def textanalyse():
    titel = "Sentiment Analyse"
    if request.method == "POST":
        # Analyse in der ui_pipeline durchführen
        ui_pipeline = UISentimentPipeline(app.config['UPLOAD_FOLDER'], session['dateiname_csv'])
        session['sentiment_result_dict'] = ui_pipeline.result_dict
        # Minimales Objekt DataVisualiser erstellen, um die möglichen Diagrammtypen zu erhalten
        diagramm_typen = ["Kuchendiagramm", "Balkendiagramm"]

        return render_template("textanalyse.html", titel=titel, sentiment_tabelle=ui_pipeline.sentiment_tabelle,
                               diagramm_typen=diagramm_typen)
    return home()  # Weiterleitung auf hauptseite, wenn über direktlink auf die Seite zugegriffen wird


# - Visualize
#     - Führt die Visualisierung durch
#     - Zeigt die Visualisierung an
#     - Visualisierung kann gespeichert werden
#     - Speichert Visualisierung als PNG
#
@app.route('/visualisierung', methods=["GET", "POST"])
def visualisierung():
    if request.method == "POST":
        # Daten laden
        sentiment_result = session['sentiment_result_dict']
        chart_type = request.form['chart_type']

        # Visualisierung erstellen
        # data_visualiser = DataVisualiser(sentiment_result)
        data_visualisation_handler = VisualisationHandler(sentiment_result)

        fig = None

        if chart_type == "Kuchendiagramm":
            data_visualisation_handler.handle_pie()
            fig = data_visualisation_handler.result.pie
            png_datei = data_visualisation_handler.save_pie("static/sentiment_analysis")
        if chart_type == "Balkendiagramm":
            data_visualisation_handler.handle_bar()
            fig = data_visualisation_handler.result.bar
            png_datei = data_visualisation_handler.save_bar("static/sentiment_analysis")

        fig_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
    return render_template("visualisierung.html", fig_html=fig_html, png_datei=png_datei)


# App Ausführen
#
if __name__ == "__main__":
    app.run(debug=True, port=5000)
