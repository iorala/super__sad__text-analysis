import unittest
import pandas as pd
from Sentiment import SentimentDataFrame

class SentimentDataFrameTest(unittest.TestCase):
    def setUp(self):
        self.rows = [('Es ist ein wunderschöner Tag.',), ('Das Leben ist scheisse.',)]
        self.sentiments = ['Positiv', 'Negativ']
        self.sentiment_dataframe = SentimentDataFrame(self.rows)

    def test_create_dataframe(self):
        self.sentiment_dataframe.create_dataframe(self.sentiments)
        dataframe = self.sentiment_dataframe.get_dataframe()
        expected_dataframe = pd.DataFrame({'Text': ['Es ist ein wunderschöner Tag.', 'Das Leben ist scheisse.'],
                                           'Sentiment': ['Positiv', 'Negativ']})
        self.assertEqual(dataframe.equals(expected_dataframe), True)

if __name__ == '__main__':
    unittest.main()