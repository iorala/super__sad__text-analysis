import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

class DataVisualizer:
    def __init__(self, data, data_1, colors=None):
        self.data = data
        self.data_1 = data_1
        self.colors = colors

"""Kommentar Sara: Daten kommen als DataFrame aus der Analyse, deswegen folgender Änderungsvorschlag für
     def __init__(self, sentiments_df, colors=None):
        self.sentiments_df = sentiments_df

Die Spalte mit der Klassifikation "neutra", "positiv", "negativ" heisst "Sentiment"
"""

#Wenn das Ergebnis einer Sentimentanalyse in einem CSV- oder DataFrame-Format vorliegt, kann der Code entsprechend angepasst werden.
    #def load_data_from_csv(self):
    #     df = pd.read_csv(self.csv_file)
    #     categories = df.columns[0]                         # Annahme: Die erste Spalte enthält die Kategorien
    #     values = df.columns[1]                             # Annahme: Die zweite Spalte enthält die Werte
    #     data = df.set_index(categories)[values].to_dict()  # Konvertieren in ein Dictionary
    #     return data

    def plot_bar_chart(self):
        #data = self.load_data_from_csv()
        x = range(len(self.data))
        if self.colors:
            plt.bar(x, self.data.values(), align='center', color=self.colors)
        else:
            plt.bar(x, self.data.values(), align='center')

        plt.xticks(x, self.data.keys())
        plt.xlabel('Kategorien')
        plt.ylabel('Werte in %')
        plt.title('Sentimentanalyse Ergebnis ')
        plt.show()

    def plot_pie_chart(self):
        #data = self.load_data_from_csv()
        if self.colors:
            plt.pie(self.data.values(), labels=self.data.keys(), colors=self.colors, autopct='%1.1f%%')
        else:
            plt.pie(self.data.values(), labels=self.data.keys(), autopct='%1.1f%%')
        plt.axis('equal')
        plt.title('Sentimentanalyse Ergebnis')
        plt.show()

    def display_table(self):
        table = tabulate(self.data_1, headers='keys', tablefmt='fancy_grid')
        print(table)

# Beispielverwendung der Klasse
##csv_file = 'data.csv'
data = {'Positiv':30, 'Neutral':50, 'Negativ':20}
data_1 = {'Category': ['Positiv', 'Neutral', 'Negativ'],
        'Value': [30, 50, 20]}
colors =["lightgreen", "lightgray", "red"]

visualizer = DataVisualizer(data, data_1, colors)

visualizer.plot_bar_chart()

visualizer.plot_pie_chart()

visualizer.display_table()
