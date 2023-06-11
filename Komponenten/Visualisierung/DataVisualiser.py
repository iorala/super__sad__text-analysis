import pandas as pd
import plotly.express as px


class DataVisualiser:
    def __init__(self, data):
        self.data = data

    # Erstellt ein Balkendiagramm (Bar Chart) basierend auf den Daten und gibt das Plotly-Figure-Objekt zurück.
    def plot_bar_chart(self):
        fig_1 = px.bar(x=list(self.data.keys()), y=list(self.data.values()), color=self.data.keys(),
                       color_discrete_map={'Neutral': 'lightgrey', 'Negativ': 'indianred', 'Positiv': 'forestgreen'})
        fig_1.update_layout(
            xaxis_title="Kategorien",
            yaxis_title="Werte",
            title="Sentimentanalyse Ergebnis",
            plot_bgcolor='white',
            paper_bgcolor='white',
        )
        fig_1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#878787')
        return fig_1

    # Erstellt ein Kreisdiagramm (Pie Chart) basierend auf den Daten und gibt das Plotly-Figure-Objekt zurück.
    def plot_pie_chart(self):
        fig = px.pie(values=list(self.data.values()), names=list(self.data.keys()), color=self.data.keys(),
                     color_discrete_map={'Neutral': 'lightgrey', 'Negativ': 'indianred', 'Positiv': 'forestgreen'})
        fig.update_layout(
            title="Sentimentanalyse Ergebnis"
        )
        return fig

    # Erstellt eine Pandas DataFrame-Tabelle basierend auf den Daten und gibt sie zurück.
    def display_table(self):
        table = pd.DataFrame(list(self.data.items()), columns=["Sentiment", "Count"])
        return table

    #  Speichert die generierten Visualisierungen (Bar Chart und Pie Chart)
    #  als Bilddateien ab und gibt die Dateinamen zurück.
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
        self.visualizer = DataVisualiser(self.data_dict)
        self.result = VisResult()

    # Führt die Handhabung von beiden Visualisierungen (Pie Chart und Bar Chart) durch.
    def handle_all(self):
        self.handle_pie()
        self.handle_bar()

    # Führt die Handhabung des Pie Charts durch.
    def handle_pie(self):
        if self.result.pie is None:
            self.result.pie = self.visualizer.plot_pie_chart()

    # Führt die Handhabung des Bar Charts durch.
    def handle_bar(self):
        if self.result.bar is None:
            self.result.bar = self.visualizer.plot_bar_chart()

    # Speichert das Pie Chart als Bilddatei ab und gibt den Dateinamen zurück.
    def save_pie(self, file_prefix):
        pie_chart_file = file_prefix + "_pie_chart.png"
        # Pie Chart speichern
        self.result.pie.write_image(pie_chart_file)
        return pie_chart_file

    # Speichert das Bar Chart als Bilddatei ab und gibt den Dateinamen zurück.
    def save_bar(self, file_prefix):
        bar_chart_file = file_prefix + "_pie_chart.png"
        # Pie Chart speichern
        self.result.bar.write_image(bar_chart_file)
        return bar_chart_file
