from Corpus import Corpus
from Sentiment import Sentiments
from Sentiment import SentimentResult


def main():
    #Filename wird von Import geliefert
    filename = 'test.csv'

    # Korpus erstellen
    corpus = Corpus(filename)
    rows = corpus.read_csv_file()

    # Sentimentanalyse durchführen
    analyzer = Sentiments(rows)
    sentiments = analyzer.get_sentiments()

    # Results
    #SentimentResult.create_amount_sentiment()
    #print(SentimentResult.sentiments_result())

    # Dict wird erstellt:
    sentiment_dataframe = SentimentResult(rows)
    sentiment_dataframe.create_dataframe(sentiments)
    #Test, wie sieht das DataFrame aus:
    print(sentiment_dataframe.result_dict)
    #print(sentiments_df['Sentiment'])



if __name__ == '__main__':
    main()