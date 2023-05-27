import os
import csv
import pandas as pd
from Import_Constants import Import_Constants

class DataImport:
    def __init__(self):
        self.file_name = ""
        self.file_format = ""
        self.file_size = 0
        Constants = Import_Constants()
        self.status = Constants.NOT_STARTED


    def import_data(self, file_name):
        if self.check_file_exists(file_name):
            self.file_name = file_name
            self.file_format = self.get_file_format(file_name)
            self.file_size = self.get_file_size(file_name)
            self.display_file_info()
            if DataControl.check_column_count(file_name):
                self.status = Import_Constants.SUCCESS
                #self.get_rows()
            else:
                self.status = Import_Constants.COLUMN_ERROR
        else:
            self.status = Import_Constants.FILE_NOT_FOUND

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

    def get_rows(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = []
            for row in reader:
                rows.append(row)
            return rows

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
