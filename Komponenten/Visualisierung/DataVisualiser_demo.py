import pandas as pd
from Komponenten.Textanalyse.Sentiment import SentimentResult, SentimentAnalyse

from DataVisualiser import DataVisualiser
# Beispielverwendung der Klasse mit dem Dataframe "sentiments_df"

data = sentiments_df
#sentiments_df = pd.DataFrame({"Sentiment": ['Positiv', 'Negativ', 'Neutral'],
                               #"Count": [30, 20, 50]})
data.set_index("Sentiment", inplace=True)

visualizer = DataVisualiser(sentiments_df)

#
#visualizer.plot_bar_chart()
#
#visualizer.plot_pie_chart()
#
visualizer.display_table()
