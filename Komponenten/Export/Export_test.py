import unittest
from Export import Export
import Visualization


class ExportTest(unittest.TestCase):
    def test_save_file(self):
        # Test für das Speichern der Datei
        export = Export("test", b"test data")
        success = export.save_file()
        self.assertTrue(success)  # Beispiel: Überprüfung des Speicherns


if __name__ == '__main__':
    unittest.main()
