# Für Visualisierung Teil Test und Demo sind gleich, also in diesem File zusammengefasst
from Komponenten.Visualisierung.DataVisualiser import DataVisualiser

sentiments_dict = {'Positiv': 2, 'Negativ': 1, 'Neutral': 3}

visualizer = DataVisualiser(sentiments_dict)

# Zeigt das Balkendiagramm an.
fig_1 = visualizer.plot_bar_chart()
# Zeigt das Kreisdiagramm an.
fig = visualizer.plot_pie_chart()

table = visualizer.display_table()

fig_1.show()
fig.show()
# Gibt die Tabelle mit den Sentiment-Daten aus.
print(table)

# Diagramme speichern
bar_chart_file, pie_chart_file = visualizer.save_visualizations("sentiment_analysis")

# Gibt den Dateinamen des gespeicherten Balkendiagramms aus.
print("Bar Chart wurde gespeichert unter:", bar_chart_file)
# Gibt den Dateinamen des gespeicherten Kreisdiagramms aus.
print("Pie Chart wurde gespeichert unter:", pie_chart_file)
