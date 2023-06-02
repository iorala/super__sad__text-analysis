import sys
sys.path.append(r'/super__sad__text-analysis')
from Komponenten.Import.Import_and_Control import DataImport
from Komponenten.Textanalyse.Sentiment import SentimentAnalyse, SentimentResult

data_importer = DataImport()
data_importer.import_data("test.csv")
rows = data_importer.get_rows()
print(rows)
sentiment_analyse = SentimentAnalyse()
sentiment_analyse.set_rows(rows)

sentiment_result = sentiment_analyse.get_sentiments()
print(sentiment_result.get_result_as_dict())

#print(rows)
#counter = SentimentResult(rows)
#sentiment_counts = counter.count_sentiments()
#print(sentiment_counts)
