#Teil für Klasse
class DataVisualiser:
    # ...

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

       
       
  #Teil für test
sentiments_dict = {"Positiv": 2, "Negativ": 1, "Neutral": 3}
visualizer = DataVisualiser(sentiments_dict)

# Diagramme erstellen
fig_1 = visualizer.plot_bar_chart()
fig = visualizer.plot_pie_chart()

# Diagramme speichern
bar_chart_file, pie_chart_file = visualizer.save_visualizations("sentiment_analysis")

print("Bar Chart wurde gespeichert unter:", bar_chart_file)
print("Pie Chart wurde gespeichert unter:", pie_chart_file)
