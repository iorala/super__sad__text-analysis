from Import_and_Control import DataControl, DataImport

# Verwendung der Klassen, Import der Datei und Datenkontrolle
file_name = "ImportSAD3.csv"

data_importer = DataImport()
data_importer.import_data(file_name)

# Datenkontrolle gemäss Kommentar Andreas angepasst
# Kommentar Andreas:
# - check_string_values wird hier nie ausgeführt, sofern check_column_count True ist
# - Wenn du beides möchtes musst du es auseinandernehmen
# - Wenn es voneinander abhängen soll, musst du evtl. die Bedingungen umdrehen
if DataControl.check_column_count(file_name) and DataControl.check_string_values(file_name):
    print("Datenkontrolle erfolgreich.")
    print("Alle Werte sind Zeichenketten.")
else:
    if not DataControl.check_column_count(file_name):
        print("Fehler: Mehrere Spalten in der CSV-Datei gefunden.")
    if not DataControl.check_string_values(file_name):
        print("Fehler: Nicht-zeichenketten Werte in der CSV-Datei gefunden.")
