# benötigte Module importieren
from flask import Flask, render_template, request, session
import plotly.io as pio

# NLTK-Modul importieren und prüfen ob das 'punkt'-Paket bereits heruntergeladen wurde
import nltk
try:
    # Versuchen Sie, das 'punkt'-Paket zu importieren
    from nltk.tokenize import PunktSentenceTokenizer
except ImportError:
    # Wenn das Modul nicht gefunden wird, puntk herunterladen
    nltk.download('punkt')

# Komponenten laden

# Custom Funktionen für die Benutzeroberfläche
from Komponenten.UI.UI import VerzeichnisErstellen, UISentimentPipeline, UIImportHandler

# Fehlermeldungen laden
from Komponenten.Messages import Messages
from Komponenten.Constants import Constants
# Objekt für die Fehlermeldungen erstellen
messages = Messages()
constants = Constants()

# Visualisierung
from Komponenten.Visualisierung.DataVisualiser import VisualisationHandler

# Globale Variablen und Funktionen
app_titel = "super().__sad__(text_analysis)"
variable = "Inhalt"
UPLOAD_FOLDER = 'uploads/'


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
# Rendert die Hauptseite der Anwendung, auf der Benutzer Texte hochladen können.
def home():
    titel = "Texte hochladen"
    return render_template("main.html", titel=titel)


# - View Upload
#     - Verarbeitet upload
#     - Zeigt Tabelle mit dem HEAD der Daten
#     - →Button für Versand an Sentiment Analysis
@app.route('/import_anzeigen', methods=["GET", "POST"])
# Verarbeitet den hochgeladenen Text und zeigt eine Tabelle mit den importierten Daten an.
def import_anzeigen():
    titel = "Importierte Texte"
    if "upload_datei" not in request.files:
        fehlermeldung = messages.get_message(constants.NO_FILE_UPLOADED)
        return render_template("fehlermeldung.html", fehlermeldung=fehlermeldung,
                               titel="Fehler!")

    if request.method == "POST":
        upload_datei = request.files['upload_datei']
        import_handler = UIImportHandler(UPLOAD_FOLDER, upload_datei)
        import_handler.import_datei()
        if import_handler.status != import_handler.constants.SUCCESS:
            return render_template("fehlermeldung.html", fehlermeldung=import_handler.fehlermeldung, titel="Fehler!")
        else:
            session['dateiname_csv'] = import_handler.dateiname_csv
            return render_template("import_anzeigen.html", titel=titel, csv_tabelle=import_handler.csv_tabelle,
                                   backpage="home")


# - Sentiment Analysis
#     - Führt die Sentiment-Analyse durch (in der ui_pipeline)
#     - Zeigt Daten HEAD (gleiche Zeilen) mit dem Sentiment wert
#     - Auswahl der gewünschten Visualisierung
@app.route('/textanalyse', methods=["GET", "POST"])
# Führt die Sentiment-Analyse für den hochgeladenen Text durch und zeigt eine Tabelle mit den Sentiment-Werten an.
# Bietet auch eine Auswahl für die gewünschte Visualisierung an.
def textanalyse():
    titel = "Sentiment Analyse"
    # Prüfen, ob schon eine Datei hochgeladen wurde (z.b. bei zurück oder direkten Aufruf der Seite)
    if 'dateiname_csv' not in session:
        fehlermeldung = messages.get_message(constants.NO_FILE_UPLOADED)
        return render_template("fehlermeldung.html", fehlermeldung=fehlermeldung, titel="Fehler!")
    else:
        # Analyse in der ui_pipeline durchführen
        ui_pipeline = UISentimentPipeline(app.config['UPLOAD_FOLDER'], session['dateiname_csv'])
        session['sentiment_result_dict'] = ui_pipeline.result_dict
        # Minimales Objekt DataVisualiser erstellen, um die möglichen Diagrammtypen zu erhalten
        diagramm_typen = ["Kuchendiagramm", "Balkendiagramm"]

        return render_template("textanalyse.html", titel=titel, sentiment_tabelle=ui_pipeline.sentiment_tabelle,
                               diagramm_typen=diagramm_typen, backpage="home")


# - Visualize
#     - Führt die Visualisierung durch
#     - Zeigt die Visualisierung an
#     - Visualisierung kann gespeichert werden
#     - Speichert Visualisierung als PNG
#
@app.route('/visualisierung', methods=["GET", "POST"])
# Führt die Visualisierung basierend auf den Sentiment-Daten durch und zeigt das erstellte Diagramm an.
# Bietet die Möglichkeit, die Visualisierung als PNG-Datei zu speichern.
def visualisierung():
    if 'sentiment_result_dict' not in session:
        fehlermeldung = messages.get_message(constants.SENTIMENT_ANALYSE_FAILED)
        return render_template("fehlermeldung.html", fehlermeldung=fehlermeldung, titel="Fehler!",
                               linkziel="import_anzeigen", linktext="Zurück und erneut versuchen")
    else:
        # Daten laden
        sentiment_result = session['sentiment_result_dict']
        chart_type = request.form['chart_type']

        # Visualisierung erstellen
        data_visualisation_handler = VisualisationHandler(sentiment_result)

        if chart_type == "Kuchendiagramm":
            data_visualisation_handler.handle_pie()
            fig_html = pio.to_html(data_visualisation_handler.result.pie, full_html=False, include_plotlyjs='cdn')
            png_datei = data_visualisation_handler.save_pie("static/sentiment_analysis")
        elif chart_type == "Balkendiagramm":
            data_visualisation_handler.handle_bar()
            fig_html = pio.to_html(data_visualisation_handler.result.bar, full_html=False, include_plotlyjs='cdn')
            png_datei = data_visualisation_handler.save_bar("static/sentiment_analysis")
        else:
            fehlermeldung = "Fehler: Diagrammtyp nicht gefunden!"
            return render_template("fehlermeldung.html", fehlermeldung=fehlermeldung, titel="Fehler!")
    return render_template("visualisierung.html", fig_html=fig_html, png_datei=png_datei, backpage="textanalyse")


# App Ausführen. Startet die Flask-Anwendung und macht sie unter localhost:5000 verfügbar.
if __name__ == "__main__":
    app.run(debug=True, port=5000)
