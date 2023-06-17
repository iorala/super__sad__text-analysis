# super().\__sad__(text_analysis): Ein Datenvisualisierungsprojekt

## Abhängigkeiten 
Die Abhängigkeiten sind in der Datei `requirements.txt` aufgelistet. Die App wurde mit Python 3.11.3 entwickelt.

## Installation
1. Repository klonen
- `git clone https://github.com/iorala/super__sad__text-analysis.git` (erfordert Login mit Benutzername und Passwort, da privates Repository)
- `git clone git@github.com:iorala/super__sad__text-analysis.git` (erfordert SSH-Authentifizierung, da privates Repository)
2. In das Verzeichnis wechseln
- `cd super__sad__text-analysis`
3. Virtuelle Umgebung erstellen
- `python -m venv venv`
4. Virtuelle Umgebung aktivieren
- **Windows:** `venv\Scripts\activate.bat` [cmd] oder `venv\Scripts\Activate.ps1` [powershell]
- **Linux und macOS:** `source venv/bin/activate`
5. Abhängigkeiten installieren
- `pip install -r requirements.txt`
6. App starten
- `python app.py`
7. App im Browser öffnen
- `http://127.0.0.1:5000/`


## Projektstruktur 
- README.Md: diese Datei 
- app.py: Dieses Skript startet die Webapplikation
- pipeline_analysis.py: Dieses Skript enthält die Pipeline für die Datenanalyse
- test.csv: Testdaten 
- test_zuviele_spalten.csv: Fehlerhafte Testdaten, welche nicht gelesen werden können
- static/: Enthält statische Elemente für die Webapplikation (z.B CSS)
- templates/: enthält die Templates für die dynamischen Seiten der Webapplikation
- Komponenten/<NAME_KOMPONENTE>: Enthält die Ordner der einzelnen Komponenten
- Komponenten/Constants.py: Enthält die Konstanten für alle Komponenten
- Komponenten/Messages.py: Enthält die Fehlermeldungen für alle Komponenten
- Test/<NAME_KOMPONENTE>: Enthält die Unit-Test für die Komponenten
- runtime.txt: Enthält die Python Version für das Deployment auf Heroku
- Procfile: Enthält die Befehle für das Deployment auf Heroku
- nltk.txt: Enthält die benötigten NLTK-Module für das Deployment auf Heroku


