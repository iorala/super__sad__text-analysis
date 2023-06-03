class Messages:
    def __init__(self):
        self.messages = {
            0: "Prozess erfolgreich abgeschlossen",
            1: " nicht abgeschlossen",
            2: "Fehler: File konnte nicht gefunden werden oder falscher Dateipfad.",
            3: "Fehler: Mehrere Spalten in der Datei vorhanden. Es ist nur eine Spalte mit Inputs erlaubt.",
            4: "Fehler: Nicht-zeichenketten Werte in der CSV-Datei gefunden."
        }

    def get_message(self,code):
        return self.messages[code]
