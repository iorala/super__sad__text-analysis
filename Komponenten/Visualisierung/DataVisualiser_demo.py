import pandas as pd
from Sentiment import SentimentDataFrame

from DataVisualiser import DataVisualiser
# # Beispielverwendung der Klasse mit dem Dataframe "sentiments_df"

data = sentiments_df
#sentiments_df = pd.DataFrame({"Sentiment": ['Positiv', 'Negativ', 'Neutral'],
                               #"Count": [30, 20, 50]})
data.set_index("Sentiment", inplace=True)

# Andreas: wieso setzt du hier den parameter colors? Dieser wird nirgendwo definiert
# und ist auch nicht notwendig für die Klasse
#visualizer = DataVisualiser(sentiments_df, colors)
visualizer = DataVisualiser(sentiments_df)

#
#visualizer.plot_bar_chart()
#
#visualizer.plot_pie_chart()
#
visualizer.display_table()