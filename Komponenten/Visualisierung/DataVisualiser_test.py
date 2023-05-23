import unittest
from unittest.mock import patch
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate
from DataVisualiser import DataVisualiser

class TestDataVisualiser(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({"Sentiment": ['Positiv', 'Negativ', 'Neutral'],
                                  "Count": [30, 20, 50]})
        self.data.set_index("Sentiment", inplace=True)
        self.colors = ["lightgreen", "red", "lightgray"]
        self.visualizer = DataVisualiser(self.data, self.colors)

    def tearDown(self):
        plt.close()

    def test_plot_bar_chart(self):
        with patch('builtins.print') as mock_print:
            self.visualizer.plot_bar_chart()
            plt.close()
            self.assertEqual(mock_print.call_count, 0)

    def test_plot_pie_chart(self):
        with patch('builtins.print') as mock_print:
            self.visualizer.plot_pie_chart()
            plt.close()
            self.assertEqual(mock_print.call_count, 0)

    def test_display_table(self):
        with patch('builtins.print') as mock_print:
            self.visualizer.display_table()
            self.assertEqual(mock_print.call_count, 1)
            expected_table = tabulate(self.data, headers='keys', tablefmt='fancy_grid')
            mock_print.assert_called_with(expected_table)

if __name__ == '__main__':
    unittest.main()
