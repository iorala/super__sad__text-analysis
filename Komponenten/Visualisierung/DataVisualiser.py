import pandas as pd
import plotly.express as px
import plotly.io as pio
# from Sentiment import SentimentResult

import pandas as pd
import plotly.express as px


# from Sentiment import SentimentResult

class DataVisualiser:
    def __init__(self, data):
        self.data = data
        self.charts = {"Kuchendiagramm": self.plot_pie_chart(), "Balkendiagramm": self.plot_bar_chart()}

    def plot_bar_chart(self):
        fig_1 = px.bar(x=list(self.data.keys()), y=list(self.data.values()), color = self.data.keys(), color_discrete_map = {'Neutral': 'lightgrey','Negativ': 'indianred', 'Positiv':'forestgreen'})
        fig_1.update_layout(
            xaxis_title="Kategorien",
            yaxis_title="Werte",
            title="Sentimentanalyse Ergebnis",
            plot_bgcolor='white',
            paper_bgcolor='white',
        )
        fig_1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#878787')
        return fig_1

    def plot_pie_chart(self):
        fig = px.pie(values=list(self.data.values()), names=list(self.data.keys()), color = self.data.keys() ,color_discrete_map = {'Neutral': 'lightgrey','Negativ': 'indianred', 'Positiv':'forestgreen'})
        fig.update_layout(
            title="Sentimentanalyse Ergebnis"
        )
        return fig

    def display_table(self):
        table = pd.DataFrame(list(self.data.items()), columns=["Sentiment", "Count"])
        return table

    def save_visualizations(self, file_prefix):
        bar_chart_file = file_prefix + "_bar_chart.png"
        pie_chart_file = file_prefix + "_pie_chart.png"

        # Bar Chart speichern
        bar_chart = self.plot_bar_chart()
        bar_chart.write_image(bar_chart_file)

        # Pie Chart speichern
        pie_chart = self.plot_pie_chart()
        pie_chart.write_image(pie_chart_file)

        return bar_chart_file, pie_chart_file

    def dump(self) -> dict[str, int]:
        return self.__dict__


class VisResult:
    bar = None
    pie = None
    table = None

    def __init__(self):
        pass


class VisualisationHandler:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def handle_all(self):
        visualizer = DataVisualiser(self.data_dict)
        result = VisResult()
        result.pie = visualizer.plot_pie_chart()
        result.bar = visualizer.plot_bar_chart()
        result.table = visualizer.display_table()
        return result
