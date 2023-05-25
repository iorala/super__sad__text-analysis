import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate


class DataVisualiser:
    def __init__(self, data):
        self.data = data

    def plot_bar_chart(self):
        x = self.data.index
        y = self.data["Count"]
        plt.bar(x, y, align='center')
        plt.xlabel('Kategorien')
        plt.ylabel('Werte')
        plt.title('Sentimentanalyse Ergebnis')
        plt.show()

    def plot_pie_chart(self):
        labels = self.data.index
        values = self.data["Count"]
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.title('Sentimentanalyse Ergebnis')
        plt.show()

    def display_table(self):
        table = tabulate(self.data, headers='keys', tablefmt='fancy_grid')
        print(table)


# Kommentar Andreas: Bitte kein Beispielcode in den Klassendefinitionen, sonst kann ich diese in der UI nicht laden
# → nach DataVisualizer_demo.py verschoben
