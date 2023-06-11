from textblob_de import TextBlobDE


class SentimentAnalyse:  # in SentimentAnalyse umbenennen
    def __init__(self):
        self.rows = None
        self.sentiment_rows = None
        self.sentiments = []

   # Setzt die Zeilen (Texte), die analysiert werden sollen.
    def set_rows(self, rows):
        # leere Zeilen entfernen, da Textblob sonst unter get_sentiments einen Fehler ausgibt ber row[0]
        self.rows = rows

    # Analysiert das Sentiment eines gegebenen Texts mithilfe der TextBlobDE-Bibliothek
    # und gibt die Klassifikation (Positiv, Negativ oder Neutral) zurück.
    def analyze_sentiment(self, text):
        # mithilfe der Bibliothek BlobDE (für Deutsche Texte) werden die einzelnen Texte klassifiziert dafür wird aus dem Text ein TextBlob Objekt generiert
        text_blob = TextBlobDE(text)
        # mit Polarity wird ein Float zwischen -1 und 1 zurückgeben, wobei -1 negativ, 1 positiv und 0 neutral ist
        polarity = text_blob.sentiment.polarity
        # Die Float-Werte sollen direkt in den drei Klassen Positiv, Negativ und Neutral ausgeben werden
        if polarity > 0:
            return 'Positiv'
        elif polarity < 0:
            return 'Negativ'
        else:
            return 'Neutral'

    # Weist jedem Text in den Zeilen eine Sentiment-Klassifikation zu und speichert die Ergebnisse in einer Liste.
    # Gibt ein SentimentResult-Objekt zurück, das die Summen der Klassifikationen enthält

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

    # Gibt das summierte Ergebnis der Sentiment-Analyse als Wörterbuch (Dictionary) zurück,
    # das die Anzahl der positiven, negativen und neutralen Klassifikationen enthält.
    def get_result_as_dict(self):
        sentiment_counts = {
            'Positiv': self.positiv_count,
            'Negativ': self.negativ_count,
            'Neutral': self.neutral_count
        }
        return sentiment_counts
