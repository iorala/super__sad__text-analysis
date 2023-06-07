# Für Visualisierung Teil Test und Demo sind gleich, also in diesem File zusammengefasst
import pandas as pd
from ...Komponenten.Visualisierung.DataVisualiser import VisualisationHandler
from ...Komponenten.Visualisierung.DataVisualiser import DataVisualiser

sentiments_dict = {'Positiv':2, 'Negativ':1, 'Neutral':3}

visualizer = DataVisualiser(sentiments_dict)

fig_1 = visualizer.plot_bar_chart()
fig = visualizer.plot_pie_chart()
table = visualizer.display_table()

fig_1.show()
fig.show()
print(table)

# Diagramme speichern
bar_chart_file, pie_chart_file = visualizer.save_visualizations("sentiment_analysis")

print("Bar Chart wurde gespeichert unter:", bar_chart_file)
print("Pie Chart wurde gespeichert unter:", pie_chart_file)
