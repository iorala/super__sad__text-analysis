from textblob_de import TextBlobDE
import pandas as pd
from collections import Counter


class SentimentAnalyse: # in SentimentAnalyse umbenennen
    def __init__(self):
        self.rows = None

    def set_rows(self, rows):
        self.rows = rows

    def analyze_sentiment(self, text):
        # mit Hilfe der Bibliothek BlobDE (für Deutsche Texte) werden die einzelnen Texte klassifiziert dafür wird aus dem Text ein TextBlob Objekt generiert
        text_blob = TextBlobDE(text)
        # mit Polarity wird ein Float zwischen -1 und 1 zurückgeben, wobei -1 negativ, 1 positiv und 0 neutral ist
        polarity = text_blob.sentiment.polarity
        # Die Float Werte sollen direkt in den drei Klassen Positiv, Negativ und Neutral ausgeben werden
        if polarity > 0:
            return 'Positiv'
        elif polarity < 0:
            return 'Negativ'
        else:
            return 'Neutral'

    # Jeder Zeile wird eine Klassifikation mittels analyse_sentiment zugewiesen. Das Resultat wir in einer Liste gespeichert.
    def get_sentiments(self):
        # prüfen, ob self.rows wahr ist
        sentiments = []
        for row in self.rows:
            # Andreas: der Code stürzt sonst ab, wenn die Zeile leer ist
            if row:
                sentiment = self.analyze_sentiment(row[0])
                print(sentiment)
                sentiments.append(sentiment)
        sentiment_result = SentimentResult()
        sentiment_result.positiv_count = sentiments.count('Positiv')
        sentiment_result.negativ_count = sentiments.count('Negativ')
        sentiment_result.neutral_count = sentiments.count('Neutral')
        return sentiment_result


# -------------------------------------------------------------------------------------------------------

class SentimentResult:
    def __init__(self):
        self.positiv_count = -1
        self.negativ_count = -1
        self.neutral_count = -1

    # Die importierten Daten werden mit den Klassifikationen aus der Sentiment-Analyse in ein DataFrame gespeichert
    def get_result_as_dict(self):
        sentiment_counts = {
            'Positiv': self.positiv_count,
            'Negativ': self.negativ_count,
            'Neutral': self.neutral_count
        }
        return sentiment_counts




