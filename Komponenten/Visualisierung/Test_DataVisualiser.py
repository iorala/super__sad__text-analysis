import DataVisualiser_px
import pandas as pd
from DataVisualiser import VisualisationHandler
from DataVisualiser import DataVisualiser

sentiments_df = pd.DataFrame({"Sentiment": ['Positiv', 'Negativ', 'Neutral'],
                              "Count": [30, 20, 50]})
sentiments_df.set_index("Sentiment", inplace=True)
visualizer = DataVisualiser(sentiments_df)

fig_1 = visualizer.plot_bar_chart()
fig = visualizer.plot_pie_chart()
table = visualizer.display_table()

fig_1.show()
fig.show()
print(table)
