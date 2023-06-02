import unittest
from unittest.mock import patch
from io import StringIO
from Import_and_Control import DataImport, DataControl

class TestDataImport(unittest.TestCase):
    def setUp(self):
        self.data_import = DataImport()

    def test_check_file_exists(self):
        file_name = "importSAD.csv"
        self.assertTrue(self.data_import.check_file_exists(file_name))

    def test_check_file_existsnot(self):
        file_name = "filedoesnotexist.csv"
        self.assertFalse(self.data_import.check_file_exists(file_name))

    def test_get_file_format(self):
        file_name = "importSAD.csv"
        self.assertEqual(self.data_import.get_file_format(file_name), "csv")

    def test_get_file_size(self):
        file_name = "importSAD.csv"
        self.assertEqual(self.data_import.get_file_size(file_name), 319)

    def test_check_column_count(self):
        file_name = "importSAD.csv"
        csv_data = "header1,header2\nvalue1,value2\nvalue3,value4"
        with patch('builtins.open', return_value=StringIO(csv_data)):
            self.assertTrue(DataControl.check_column_count(file_name))


if __name__ == '__main__':
    unittest.main()
