import pandas as pd
import plotly.express as px
from Sentiment import SentimentResult

class DataVisualiser:
    def __init__(self, data):
        self.data = data

    def plot_bar_chart(self):
        fig = px.bar(self.data, x=self.data.index, y="Count")
        fig.update_layout(
            xaxis_title="Kategorien",
            yaxis_title="Werte",
            title="Sentimentanalyse Ergebnis"
        )
        return fig

    def plot_pie_chart(self):
        fig = px.pie(self.data, values="Count", names=self.data.index)
        fig.update_layout(
            title="Sentimentanalyse Ergebnis"
        )
        return fig

    def display_table(self):
        table = pd.DataFrame(self.data)
        return table


sentiment_result.set_index("Sentiment", inplace=True)
visualizer = DataVisualiser(sentiment_result)

fig = visualizer.plot_bar_chart()
fig = visualizer.plot_pie_chart()
table = visualizer.display_table()
