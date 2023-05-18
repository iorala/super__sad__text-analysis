from Corpus import Corpus
from Sentiment import Sentiments
from Sentiment import SentimentDataFrame


def main():
    #Filename wird von Import geliefert
    filename = 'test.csv'

    # Korpus erstellen
    corpus = Corpus(filename)
    rows = corpus.read_csv_file()

    # Sentimentanalyse durchführen
    analyzer = Sentiments(rows)
    sentiments = analyzer.get_sentiments()

    # DataFrame wird erstellt:
    sentiment_dataframe = SentimentDataFrame(rows)
    sentiment_dataframe.create_dataframe(sentiments)
    sentiments_df = sentiment_dataframe.get_dataframe()

    #Test, wie sieht das DataFrame aus:
    print(sentiments_df.head())
    print(sentiments_df['Sentiment'])



if __name__ == '__main__':
    main()