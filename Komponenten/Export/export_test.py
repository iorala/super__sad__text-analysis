import unittest
from export import Export
import Visualization


class ExportTest(unittest.TestCase):
    def test_compress_data(self):
        # Test für die Komprimierung der Daten
        export = Export("test", b"test data")
        compressed_data = export.compress_data()
        self.assertEqual(compressed_data, b"compressed data")  # Beispiel: Überprüfung der Komprimierung

    def test_save_file(self):
        # Test für das Speichern der Datei
        export = Export("test", b"test data")
        success = export.save_file()
        self.assertTrue(success)  # Beispiel: Überprüfung des Speicherns


if __name__ == '__main__':
    unittest.main()
