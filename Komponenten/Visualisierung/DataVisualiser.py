import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

class DataVisualiser:
    def __init__(self, data, colors=None):
        self.data = data
        self.colors = colors

    def plot_bar_chart(self):
        x = self.data.index
        y = self.data["Count"]
        if self.colors:
            plt.bar(x, y, align='center', color=self.colors)
        else:
            plt.bar(x, y, align='center')
        plt.xlabel('Kategorien')
        plt.ylabel('Werte')
        plt.title('Sentimentanalyse Ergebnis')
        plt.show()

    def plot_pie_chart(self):
        labels = self.data.index
        values = self.data["Count"]
        if self.colors:
            plt.pie(values, labels=labels, colors=self.colors, autopct='%1.1f%%')
        else:
            plt.pie(values, labels=labels, colors=self.colors)
        plt.axis('equal')
        plt.title('Sentimentanalyse Ergebnis')
        plt.show()

    def display_table(self):
        table = tabulate(self.data, headers='keys', tablefmt='fancy_grid')
        print (table)

# Beispielverwendung der Klasse mit dem Dataframe "sentiments_df"
sentiments_df = pd.DataFrame({"Sentiment": ['Positiv', 'Negativ', 'Neutral'],
                              "Count": [30, 20, 50]})
sentiments_df.set_index("Sentiment", inplace=True)
colors = ["lightgreen", "red", "lightgray"]
visualizer = DataVisualiser(sentiments_df, colors)
#
visualizer.plot_bar_chart()
#
visualizer.plot_pie_chart()
#
visualizer.display_table()
