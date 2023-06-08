class Messages:
    def __init__(self):
        self.messages = {
            0: "Prozess erfolgreich abgeschlossen",
            1: "Import nicht abgeschlossen",
            2: "Datei konnte nicht gefunden werden oder falscher Dateipfad.",
            3: "Mehrere Spalten in der Datei vorhanden. Es ist nur eine Spalte mit Inputs erlaubt.",
            4: "Nicht-Zeichenketten Werte in der CSV-Datei gefunden.",
            5: "Falsches Dateiformat. Es sind nur CSV-Dateien erlaubt."
        }

    def get_message(self,code):
        return self.messages[code]
