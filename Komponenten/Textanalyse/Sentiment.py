from textblob_de import TextBlobDE
import pandas as pd


class Sentiments:
    def __init__(self, rows):
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
        sentiments = []
        for row in self.rows:
            # Andreas: der Code stürzt sonst ab, wenn die Zeile leer ist
            if row:
                sentiment = self.analyze_sentiment(row[0])
                sentiments.append(sentiment)
        return sentiments


# -------------------------------------------------------------------------------------------------------

class SentimentResult:
    def __init__(self, rows):
        self.rows = rows
        self.sentiments_df = None

    # Die importierten Daten werden mit den Klassifikationen aus der Sentiment-Analyse in ein DataFrame gespeichert
    def create_dataframe(self, sentiments):
        self.sentiments_df = pd.DataFrame({"Text": [row[0] for row in self.rows if row], "Sentiment": sentiments})
        self.sentiments_result = self.sentiments_df['Sentiment'].value_counts().to_dict()
        self.result_dict = {"Sentiment": list(self.sentiments_result.keys()), "Count": list(self.sentiments_result.values())}





