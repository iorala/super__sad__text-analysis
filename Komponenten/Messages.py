class Messages:
    # Initialisiert das messages-Dictionary mit den Meldungen für verschiedene Codes.
    def __init__(self):
        self.messages = {
            0: "Prozess erfolgreich abgeschlossen",
            1: "Import nicht abgeschlossen",
            2: "Datei konnte nicht gefunden werden oder falscher Dateipfad.",
            3: "Mehrere Spalten in der Datei vorhanden. Es ist nur eine Spalte mit Inputs erlaubt.",
            4: "Nicht-Zeichenketten Werte in der CSV-Datei gefunden.",
            5: "Falsches Dateiformat. Es sind nur CSV-Dateien erlaubt.",
            6: "Keine Datei hochgeladen: Bitte eine Datei auswählen",
            7: "Sentiment-Analyse fehlgeschlagen, bitte nochmals eine Datei hochladen.",
            8: "Kein Diagramm ausgewählt. Bitte wählen Sie ein Diagramm aus."
        }

    # Gibt die Meldung für einen bestimmten Code zurück, basierend auf dem übergebenen Code-Parameter.
    def get_message(self, code):
        return self.messages[code]
