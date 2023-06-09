from textblob_de import TextBlobDE


class SentimentAnalyse:  # in SentimentAnalyse umbenennen
    def __init__(self):
        self.rows = None
        self.sentiment_rows = None
        self.sentiments = []

    def set_rows(self, rows):
        # leere Zeilen entfernen, da Textblob sonst unter get_sentiments einen Fehler ausgibt ber row[0]
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
        # jeder Zeile wird ein Sentiment zugewiesen. Die Sentiments werden in einer Liste gespeichert
        for row in self.rows:
            sentiment = self.analyze_sentiment(row)
            self.sentiments.append(sentiment)
        sentiment_result = SentimentResult()

        # die Klassifikationen werden summiert
        sentiment_result.positiv_count = self.sentiments.count('Positiv')
        sentiment_result.negativ_count = self.sentiments.count('Negativ')
        sentiment_result.neutral_count = self.sentiments.count('Neutral')

        return sentiment_result


# -------------------------------------------------------------------------------------------------------

class SentimentResult:
    def __init__(self):
        self.positiv_count = -1
        self.negativ_count = -1
        self.neutral_count = -1

    # das summierte Resultat der Sentiment-Analyse wird in ein Dictionary gespeichert
    def get_result_as_dict(self):
        sentiment_counts = {
            'Positiv': self.positiv_count,
            'Negativ': self.negativ_count,
            'Neutral': self.neutral_count
        }
        return sentiment_counts
