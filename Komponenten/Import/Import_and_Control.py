import os
import csv
from Komponenten.Constants import Constants


class DataImport:
    def __init__(self):
        self.file_name = ""
        self.file_format = ""
        self.file_size = 0
        self.constants = Constants()
        self.status = self.constants.NOT_STARTED

    # Importiert Daten aus einer Datei und führt verschiedene Überprüfungen
    # und Aktionen basierend auf den importierten Daten durch.
    def import_data(self, file_name):
        if self.check_file_exists(file_name):
            self.file_name = file_name
            self.file_format = self.get_file_format(file_name)
            self.file_size = self.get_file_size(file_name)
            self.display_file_info()
            if self.file_format != "csv":
                self.status = self.constants.FILE_FORMAT_ERROR
                return
            if DataControl.check_column_count(file_name):
                self.status = self.constants.SUCCESS
                # self.get_rows()
            else:
                self.status = self.constants.COLUMN_ERROR
        else:
            self.status = self.constants.FILE_NOT_FOUND

    # Überprüft, ob die angegebene Datei existiert.
    def check_file_exists(self, file_name):
        if os.path.isfile(file_name):
            return True
        else:
            return False

    # Extrahiert das Dateiformat aus dem Dateinamen.
    def get_file_format(self, file_name):
        file_format = file_name.split(".")[-1]
        return file_format

    # Ermittelt die Grösse der Datei in Bytes.
    def get_file_size(self, file_name):
        file_size = os.path.getsize(file_name)
        return file_size

    # Zeigt Informationen über den Dateinamen, das Dateiformat und die Dateigrösse an.
    def display_file_info(self):
        print("File Name:", self.file_name)
        print("File Format:", self.file_format)
        print("File Grösse:", self.file_size, "bytes")

   # Liest die Datenzeilen aus einer CSV-Datei und gibt sie als Liste zurück.
    def get_rows(self):
        with open(self.file_name, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            rows = []
            for row in reader:
                if row:
                    rows.append(row[0])
            return rows


class DataControl:
    # Überprüft die Anzahl der Spalten in der CSV-Datei und gibt True zurück,
    # wenn jede Zeile genau eine Spalte hat, andernfalls False.
    @staticmethod
    def check_column_count(file_name):
        # with open(file_name, 'r', encoding='utf-8') as file: # Expliziter UTF-8 encoding entfernt wegen BOM
        with open(file_name, 'r') as file:

            reader = csv.reader(file, delimiter=";")
            header = next(reader, None)
            if len(header) == 1:
                for row in reader:
                    if len(row) > 1:
                        return False
                return True
            else:
                return False
