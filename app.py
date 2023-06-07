# benötigte Module importieren
from flask import Flask, redirect, render_template, request, flash, session
import os
import uuid
import joblib
from collections import defaultdict
import pandas as pd
from werkzeug.utils import secure_filename

# Nachrichten laden
from Messages import Messages

# Komponenten laden

# Custom Funktionen für die Benutzeroberfläche
from Komponenten.UI.ui_funktionen import bs_tabelle_aus_df, upload_verzeichnis_erstellen

# Fehlermeldungen laden
from Messages import Messages

# Datenimport
from Komponenten.Import.Import_and_Control import DataImport, DataControl

# Textanalyse
from Komponenten.Textanalyse.Sentiment import SentimentAnalyse
# Visualisierung
from Komponenten.Visualisierung.DataVisualiser import DataVisualiser

# Export
from Komponenten.Export.Export import Export
from Komponenten.Export.Image_data import ImageData
from Komponenten.Export.PNG_Exporter import PNGExporter

# Punkt-Tokenizer aus dem nltk-Modul importieren, da dieser für die Textanalyse benötigt wird
# wird auf heroku von textblob_de nicht installiert
# https://devcenter.heroku.com/articles/python-nltk
# import nltk
# nltk.download('punkt')


# Globale Variablen und Funktionen
app_titel = "super().__sad__(text_analysis)"
variable = "Inhalt"
UPLOAD_FOLDER = 'uploads/'
## Objekt für die Fehlermeldungen erstellen
meldungen = Messages()

# Applikation initialisieren
app = Flask("super__sad__text_analysis")
app.secret_key = b'03dbdf2044be76908d840d4fa4de082d111708ce8ba4d2794ee9be0f4af45622'

# Verzeichnis zum Speichern der Nutzerdaten
upload_verzeichnis_erstellen(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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
    titel = "Texte hochladen"
    return render_template("main.html", titel=titel)


# - View Upload
#     - Verarbeitet upload
#     - Zeigt Tabelle mit dem HEAD der Daten
#     - →Button für Versand an Sentiment Analysis
@app.route('/import_anzeigen', methods=["GET", "POST"])
def import_anzeigen():
    titel = "Importierte Texte"
    if request.method == "POST":
        print("request.files:", request.files['csv_datei'])
        csv_datei = request.files['csv_datei']
        # wenn keine Datei ausgewählt wird, wir ein leerer string generiert
        if csv_datei.filename == '':
            fehlermeldung = "Bitte eine Datei auswählen"
            return (fehlermeldung)  # Hier muss noch eine Fehlerseite eingefügt werden
        # Datei speichern
        # Dateiname besteht aus eindeutiger ID und dem sicheren Dateinamen (überprüft)
        datei_id_csv = str(uuid.uuid4())
        session['dateiname_csv'] = datei_id_csv + "_" + secure_filename(csv_datei.filename)
        csv_datei.save(os.path.join(app.config['UPLOAD_FOLDER'], session['dateiname_csv']))
        data_importer = DataImport()
        data_importer.import_data(os.path.join(app.config['UPLOAD_FOLDER'], session['dateiname_csv']))
        if data_importer.status != data_importer.constants.SUCCESS:
            fehlermeldung = "Der import ist fehlgeschlagen. "
            fehlermeldung += meldungen.get_message(data_importer.status)
            return fehlermeldung  # Hier muss noch eine Fehlerseite eingefügt werden
        csv_tabelle = bs_tabelle_aus_df(pd.DataFrame(data_importer.get_rows()).head())
        return render_template("import_anzeigen.html", titel=titel, csv_tabelle=csv_tabelle)
    return home()  # Weiterleitung auf hauptseite, wenn über direktlink auf die Seite zugegriffen wird


# - Sentiment Analysis
#     - Führt die Sentiment analyse durch
#     - Zeigt Daten HEAD (gleiche Zeilen) mit dem Sentiment wert
#     - → Button für Visualize
@app.route('/textanalyse', methods=["GET", "POST"])
def textanalyse():
    titel = "Sentiment Analyse"
    if request.method == "POST":
        # Importiere Daten
        data_importer = DataImport()
        data_importer.import_data(os.path.join(app.config['UPLOAD_FOLDER'], session['dateiname_csv']))
        rows = data_importer.get_rows()
        print(rows)

        # Führe Sentiment-Analyse durch
        sentiment_analyse = SentimentAnalyse()
        sentiment_analyse.set_rows(rows)
        sentiment_result = sentiment_analyse.get_sentiments()

        print(sentiment_analyse.sentiments)

        sentiment_tabelle = bs_tabelle_aus_df(
            pd.DataFrame(list(zip(sentiment_analyse.rows, sentiment_analyse.sentiments)),
                         columns=['Text', 'Sentiment']))

        # Minimales Objekt DataVisualiser erstellen um die möglichen Diagrammtypen zu erhalten
        diagramm_typen = DataVisualiser({0: None}).charts.keys()

        return render_template("textanalyse.html", titel=titel, sentiment_tabelle=sentiment_tabelle,
                               diagramm_typen=diagramm_typen)
    return home()  # Weiterleitung auf hauptseite, wenn über direktlink auf die Seite zugegriffen wird


# - Visualize
#     - Führt die Visualisierung durch
#     - Zeigt die Visualisierung an
#     - → Button für Save
#     - Speichert Visualisierung als PNG
#     - Eventuell hat Korpus eine Funktion speichern als CSV (?)
#
@app.route('/visualisierung', methods=["GET", "POST"])
def visualisierung():
    if request.method == "POST":
        # Daten laden
        sentiment_dataframe = joblib.load(os.path.join(app.config['UPLOAD_FOLDER'], session['dateiname_sent']))
        # if request.form['chart_type'] == 'bar':
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
