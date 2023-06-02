import unittest
import pandas as pd
from Sentiment import SentimentResult
from Sentiment import SentimentAnalyse

class SentimentResultTest(unittest.TestCase):
    def setUp(self):
        self.rows = [('Es ist ein wunderschöner Tag.',), ('Das Leben ist scheisse.',)]
        self.sentiments = ['Positiv', 'Negativ']
        self.sentiment_dataframe = SentimentResult(self.rows)

    def test_create_dataframe(self):
        self.sentiment_dataframe.create_dataframe(self.sentiments)
        data_dict = self.sentiment_dataframe.result_dict()
        expected_dataframe = pd.DataFrame({'Sentiment': ['Es ist ein wunderschöner Tag.', 'Das Leben ist scheisse.'],
                                           'Count': ['Positiv', 'Negativ']})
        self.assertEqual(data_dict.equals(expected_dataframe), True)


class SentimentsTest(unittest.TestCase):
    def setUp(self):
        self.rows = [('Es ist ein wunderschöner Tag.',), ('Das Buch ist schlecht.',)]
        self.sentiments = SentimentAnalyse(self.rows)

    def test_get_sentiments(self):
        expected_sentiments = ["Positiv", "Negativ"]
        sentiments = self.sentiments.get_sentiments()
        self.assertEqual(sentiments, expected_sentiments)


if __name__ == '__main__':
    unittest.main()