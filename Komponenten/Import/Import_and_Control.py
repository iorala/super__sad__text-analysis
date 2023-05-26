import os
import csv
import pandas as pd

class DataImport:
    def __init__(self):
        self.file_name = ""
        self.file_format = ""
        self.file_size = 0

    def import_data(self, file_name):
        if self.check_file_exists(file_name):
            self.file_name = file_name
            self.file_format = self.get_file_format(file_name)
            self.file_size = self.get_file_size(file_name)
            self.display_file_info()
            if DataControl.check_column_count(file_name):
                self.import_success_message()
                self.display_data()
            else:
                self.column_error_message()
        else:
            self.import_error_message()

    def check_file_exists(self, file_name):
        if os.path.isfile(file_name):
            return True
        else:
            return False

    def get_file_format(self, file_name):
        # Code zum Extrahieren des Dateiformats aus dem Dateinamen
        file_format = file_name.split(".")[-1]
        return file_format

    def get_file_size(self, file_name):
        file_size = os.path.getsize(file_name)
        return file_size

    def display_file_info(self):
        print("File Name:", self.file_name)
        print("File Format:", self.file_format)
        print("File Grösse:", self.file_size, "bytes")

    def import_success_message(self):
        print("Daten Import erfolgreich.")

    def import_error_message(self):
        print("Fehler: File konnte nicht gefunden werden oder falscher Dateipfad.")

    def column_error_message(self):
        print("Fehler: Mehrere Spalten in der Datei vorhanden. Es ist nur eine Spalte mit Inputs erlaubt.")

    def display_data(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                 if row:
                    print(row[0])

    # Für die Webui benötige ich ein Dataframe und kein Print-Funktionen
    def get_dataframe(self):
        return pd.read_csv(self.file_name, header=None)



class DataControl:
    @staticmethod
    def check_column_count(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=";")
            header = next(reader, None)
            if len(header) == 1:
                for row in reader:
                    if len(row) > 1:
                        return False
                return True
            else:
                return False

    @staticmethod
    def check_string_values(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=";")
            header = next(reader, None)
            if len(header) == 1:
                for row in reader:
                    if any(not isinstance(cell, str) for cell in row):
                        return False
                return True
            else:
                return False

# Kommentar Andreas: Bitte kein Beispielcode in den Klassendefinitionen, sonst kann ich diese in der UI nicht laden
# → nach Import_and_Control_demo.py verschoben
