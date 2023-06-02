import pandas as pd
import plotly.express as px
#from Sentiment import SentimentResult

class DataVisualiser:
    def __init__(self, data):
        self.data = data

    def plot_bar_chart(self):
        fig_1 = px.bar(self.data, x=self.data.index, y="Count")
        fig_1.update_layout(
            xaxis_title="Kategorien",
            yaxis_title="Werte",
            title="Sentimentanalyse Ergebnis"
        )
        return fig_1

    def plot_pie_chart(self):
        fig = px.pie(self.data, values="Count", names=self.data.index)
        fig.update_layout(
            title="Sentimentanalyse Ergebnis"
        )
        return fig

    def display_table(self):
        table = pd.DataFrame(self.data)
        return table

class VisResult:
    bar = None
    pie = None
    table = None
    def __init__(self):
        pass


class VisualisationHandler:
    def __init__(self, data_df):
        self.data_df = data_df

    def handle_all(self):
        visualizer = DataVisualiser(self.data_df)
        result = VisResult()
        result.pie = visualizer.plot_pie_chart()
        result.bar = visualizer.plot_bar_chart()
        result.table = visualizer.display_table()
        return result
