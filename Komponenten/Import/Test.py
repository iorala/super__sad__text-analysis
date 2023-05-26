#Test1
import os
import csv

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
        file_format = file_name.split(".")[-1]
        return file_format

    def get_file_size(self, file_name):
        file_size = os.path.getsize(file_name)
        return file_size

    def display_file_info(self):
        print("Dateiname:", self.file_name)
        print("Dateiformat:", self.file_format)
        print("Dateigröße:", self.file_size, "Bytes")

    def import_success_message(self):
        print("Datenimport erfolgreich.")

    def import_error_message(self):
        print("Fehler: Datei nicht gefunden oder falscher Dateipfad.")

    def column_error_message(self):
        print("Fehler: Mehrere Spalten in der CSV-Datei gefunden. Es ist nur eine Spalte erlaubt.")

    def display_data(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0])


class DataControl:
    @staticmethod
    def check_column_count(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if len(header) == 1:
                for row in reader:
                    if len(row) > 1:
                        return False
                return True
            else:
                return False

# Verwendung der Klassen, Import der Datei und Datenkontrolle
file_name = "ImportSAD.csv"

data_importer = DataImport()
data_importer.import_data(file_name)

if DataControl.check_column_count(file_name):
    print("Datenkontrolle erfolgreich. Es wurde nur eine Spalte gefunden.")
else:
    print("Fehler: Mehrere Spalten in der CSV-Datei gefunden.")


#Test2    
import os
import csv

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
        file_format = file_name.split(".")[-1]
        return file_format

    def get_file_size(self, file_name):
        file_size = os.path.getsize(file_name)
        return file_size

    def display_file_info(self):
        print("Dateiname:", self.file_name)
        print("Dateiformat:", self.file_format)
        print("Dateigröße:", self.file_size, "Bytes")

    def import_success_message(self):
        print("Datenimport erfolgreich.")

    def import_error_message(self):
        print("Fehler: Datei nicht gefunden oder falscher Dateipfad.")

    def column_error_message(self):
        print("Fehler: Mehrere Spalten in der CSV-Datei gefunden. Es ist nur eine Spalte erlaubt.")

    def display_data(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0])


class DataControl:
    @staticmethod
    def check_column_count(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if len(header) == 1:
                for row in reader:
                    if len(row) > 1:
                        return False
                return True
            else:
                return False

# Verwendung der Klassen, Import der Datei und Datenkontrolle
file_name = "ImportSAD2.csv"

data_importer = DataImport()
data_importer.import_data(file_name)

if DataControl.check_column_count(file_name):
    print("Datenkontrolle erfolgreich. Es wurde nur eine Spalte gefunden.")
else:
    print("Fehler: Mehrere Spalten in der CSV-Datei gefunden.")


#Test3

import os
import csv

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
        file_format = file_name.split(".")[-1]
        return file_format

    def get_file_size(self, file_name):
        file_size = os.path.getsize(file_name)
        return file_size

    def display_file_info(self):
        print("Dateiname:", self.file_name)
        print("Dateiformat:", self.file_format)
        print("Dateigröße:", self.file_size, "Bytes")

    def import_success_message(self):
        print("Datenimport erfolgreich.")

    def import_error_message(self):
        print("Fehler: Datei nicht gefunden oder falscher Dateipfad.")

    def column_error_message(self):
        print("Fehler: Mehrere Spalten in der CSV-Datei gefunden. Es ist nur eine Spalte erlaubt.")

    def display_data(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0])


class DataControl:
    @staticmethod
    def check_column_count(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if len(header) == 1:
                for row in reader:
                    if len(row) > 1:
                        return False
                return True
            else:
                return False

# Verwendung der Klassen, Import der Datei und Datenkontrolle
file_name = "ImportSAD3.csv"

data_importer = DataImport()
data_importer.import_data(file_name)

if DataControl.check_column_count(file_name):
    print("Datenkontrolle erfolgreich. Es wurde nur eine Spalte gefunden.")
else:
    print("Fehler: Mehrere Spalten in der CSV-Datei gefunden.")
