import unittest
from unittest.mock import patch, MagicMock
from Komponenten.Import.Import_and_Control import DataImport, DataControl
from Komponenten.Textanalyse.Sentiment import Sentiments, SentimentResult
from Komponenten.Visualisierung.DataVisualiser_1 import DataVisualiser_1


class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.test_file = "ImportSAD.csv"
        self.test_data = [
            ["This is a positive sentence."],
            ["This is a negative sentence."],
            ["This is a neutral sentence."]
        ]

    def tearDown(self):
        pass

    def test_data_import(self):
        data_import = DataImport()
        data_import.check_file_exists = MagicMock(return_value=True)
        data_import.get_file_format = MagicMock(return_value="csv")
        data_import.get_file_size = MagicMock(return_value=0)
        data_control_mock = MagicMock()
        data_control_mock.check_column_count.return_value = True
        data_control_mock.check_string_values.return_value = True
        DataControl.check_column_count = MagicMock(return_value=data_control_mock.check_column_count())
        DataControl.check_string_values = MagicMock(return_value=data_control_mock.check_string_values())

        data_import.import_data(self.test_file)

        self.assertEqual(data_import.file_name, self.test_file)
        self.assertEqual(data_import.file_format, "csv")
        self.assertEqual(data_import.file_size, 0)
        self.assertEqual(data_import.status, "SUCCESS")

    def test_data_control(self):
        data_control = DataControl()
        data_control.check_column_count = MagicMock(return_value=True)
        data_control.check_string_values = MagicMock(return_value=True)

        column_count_result = data_control.check_column_count(self.test_file)
        string_values_result = data_control.check_string_values(self.test_file)

        self.assertEqual(column_count_result, True)
        self.assertEqual(string_values_result, True)

    def test_sentiments(self):
        sentiments = Sentiments(self.test_data)
        result = sentiments.get_sentiments()

        expected_result = ['Positiv', 'Negativ', 'Neutral']
        self.assertEqual(result, expected_result)

    def test_sentiment_result(self):
        sentiment_result = SentimentResult(self.test_data)
        sentiment_result.create_dataframe(['Positiv', 'Negativ', 'Neutral'])

        self.assertIsNotNone(sentiment_result.sentiments_df)

    def test_data_visualiser(self):
        data = {'Sentiment': ['Positiv', 'Negativ', 'Neutral'], 'Count': [10, 5, 3]}
        visualiser = DataVisualiser_1(data)

        bar_chart = visualiser.plot_bar_chart()
        pie_chart = visualiser.plot_pie_chart()
        table = visualiser.display_table()

        self.assertIsNotNone(bar_chart)
        self.assertIsNotNone(pie_chart)
        self.assertIsNotNone(table)


if __name__ == "__main__":
    unittest.main()


    
