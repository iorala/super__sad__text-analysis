import unittest
from Komponenten.Textanalyse.Sentiment import SentimentResult
from Komponenten.Textanalyse.Sentiment import SentimentAnalyse


class TestSentimentAnalyse(unittest.TestCase):
    # Testet die Funktion get_sentiments der SentimentAnalyse-Klasse, um die Sentiment-Analyse für eine Liste von
    # Textzeilen durchzuführen. Überprüft die Anzahl der positiven, negativen und neutralen Sentiments und verwendet
    # assertEqual, um die erwarteten Ergebnisse zu überprüfen.
    def test_get_sentiments(self):
        # Test data
        rows = [
            'Es ist ein wunderschöner Tag.',
            'Der Service ist nicht gut.',
            'Es ist okay.',
            'Das Buch ist schlecht.',
            'Ich liebe es.'
        ]
        analyser = SentimentAnalyse()
        analyser.set_rows(rows)
        result = analyser.get_sentiments()

        # Resultat überprüfen
        self.assertEqual(result.positiv_count, 2)
        self.assertEqual(result.negativ_count, 2)
        self.assertEqual(result.neutral_count, 1)


if __name__ == '__main__':
    unittest.main()


class TestSentimentResult(unittest.TestCase):
    # Testet die Funktion get_result_as_dict der SentimentResult-Klasse, um das Ergebnis der Sentiment-Analyse als
    # Wörterbuch zurückzugeben. Setzt zuvor die Werte für die positiven, negativen und neutralen Zählungen. Überprüft,
    # ob das Wörterbuch den erwarteten Zählungen entspricht, und verwendet assertEqual für die Überprüfung.
    def test_get_result_as_dict(self):
        result = SentimentResult()
        # Test data
        result.positiv_count = 2
        result.negativ_count = 3
        result.neutral_count = 1

        # Get the result as a dictionary
        sentiment_counts = result.get_result_as_dict()

        # Verify the results
        expected_counts = {
            'Positiv': 2,
            'Negativ': 3,
            'Neutral': 1
        }
        self.assertEqual(sentiment_counts, expected_counts)


if __name__ == '__main__':
    unittest.main()
