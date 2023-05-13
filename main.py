# benötigte Module importieren
from flask import Flask, redirect
from flask import render_template
from flask import request
from collections import defaultdict

# name der Applikation
app = Flask("super__sad__text_analysis")

# Globale Variablen und Funktionen
variable = "Inhalt"


# @app.name_der_Funktion()
#
#def funktion():
#   return "x"

#
# Webseiten
#

# Homepage
@app.route('/')
def home():
    return render_template("main.html")

# andere Seite
@app.route('/name_seite', methods=["GET", "POST"])
# - Streckenübersicht
# - Filtermöglichkeiten für Suche (Ersetzt separate Suchseite)
def name_seite():
    # Blah blah
    return render_template("name_seite.html")

# Test-Seite -> gibt einfach Variablen aus
@app.route('/test')
# For testing
def hello_world(variable):

    return variable

#
# App Ausführen
#
if __name__ == "__main__":
    app.run(debug=True, port=5000)
