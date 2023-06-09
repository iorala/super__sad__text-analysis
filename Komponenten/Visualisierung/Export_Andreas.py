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

    def plot_bar_chart(self):
        fig_1 = px.bar(x=list(self.data.keys()), y=list(self.data.values()))
        fig_1.update_layout(
            xaxis_title="Kategorien",
            yaxis_title="Werte",
            title="Sentimentanalyse Ergebnis"
        )
        return fig_1

    def plot_pie_chart(self):
        fig = px.pie(values=list(self.data.values()), names=list(self.data.keys()))
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


# Teil für test
sentiments_dict = {"Positiv": 2, "Negativ": 1, "Neutral": 3}
visualizer = DataVisualiser(sentiments_dict)

# Diagramme erstellen
fig_1 = visualizer.plot_bar_chart()
fig = visualizer.plot_pie_chart()

# Diagramme speichern
bar_chart_file, pie_chart_file = visualizer.save_visualizations("sentiment_analysis")

print("Bar Chart wurde gespeichert unter:", bar_chart_file)
print("Pie Chart wurde gespeichert unter:", pie_chart_file)
