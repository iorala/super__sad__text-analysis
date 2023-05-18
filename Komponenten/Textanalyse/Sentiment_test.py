import unittest
import pandas as pd
from Sentiment import SentimentDataFrame
from Sentiment import Sentiments

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


class SentimentsTest(unittest.TestCase):
    def setUp(self):
        self.rows = [('Es ist ein wunderschöner Tag.',), ('Das Buch ist schlecht.',)]
        self.sentiments = Sentiments(self.rows)

    def test_get_sentiments(self):
        expected_sentiments = ["Positiv", "Negativ"]
        sentiments = self.sentiments.get_sentiments()
        self.assertEqual(sentiments, expected_sentiments)


if __name__ == '__main__':
    unittest.main()