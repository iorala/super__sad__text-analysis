import unittest
from unittest.mock import patch
from io import StringIO
from Komponenten.Import.Import_and_Control import DataImport, DataControl


class TestDataImport(unittest.TestCase):
    # Die Vorbereitungsfunktion, die vor jedem Testfall ausgeführt wird und eine Instanz der DataImport-Klasse erstellt.
    def setUp(self):
        self.data_import = DataImport()

    # Testet die Funktion check_file_exists der DataImport-Klasse, um zu überprüfen,
    # ob eine Datei existiert. Erwartet, dass die Datei vorhanden ist und assertTrue wird erwartet.
    def test_check_file_exists(self):
        file_name = "importSAD.csv"
        self.assertTrue(self.data_import.check_file_exists(file_name))

    # Testet die Funktion check_file_exists der DataImport-Klasse, um zu überprüfen,
    # ob eine nicht existierende Datei erkannt wird. Erwartet, dass die Datei nicht vorhanden ist
    # und assertFalse wird erwartet.
    def test_check_file_existsnot(self):
        file_name = "filedoesnotexist.csv"
        self.assertFalse(self.data_import.check_file_exists(file_name))

    # Testet die Funktion get_file_format der DataImport-Klasse, um das Dateiformat einer Datei zu extrahieren.
    # Überprüft, ob das erwartete Dateiformat zurückgegeben wird und assertEqual wird erwartet.
    def test_get_file_format(self):
        file_name = "importSAD.csv"
        self.assertEqual(self.data_import.get_file_format(file_name), "csv")

    # Testet die Funktion get_file_size der DataImport-Klasse, um die Grösse einer Datei zu ermitteln.
    # Überprüft, ob die erwartete Dateigrösse zurückgegeben wird und assertEqual wird erwartet.
    def test_get_file_size(self):
        file_name = "importSAD.csv"
        # Möglicherweise ist die Dateigrösse auf unterschiedlichen Betriebssystemen nicht immer gleich
        self.assertEqual(self.data_import.get_file_size(file_name), 319)

    # Testet die statische Methode check_column_count der DataControl-Klasse, um zu überprüfen,
    # ob die Anzahl der Spalten in einer CSV-Datei korrekt ist. Erzeugt eine CSV-Datenzeichenkette und überprüft,
    # ob die Methode True zurückgibt und assertTrue wird erwartet.
    def test_check_column_count(self):
        file_name = "importSAD.csv"
        csv_data = "header1,header2\nvalue1,value2\nvalue3,value4"
        with patch('builtins.open', return_value=StringIO(csv_data)):
            self.assertTrue(DataControl.check_column_count(file_name))


if __name__ == '__main__':
    unittest.main()
