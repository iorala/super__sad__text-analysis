import nltk
import pandas as pd
from Komponenten.Import.Import_and_Control import DataImport, Import_Constants
from Komponenten.Textanalyse.Sentiment import SentimentAnalyse
from Komponenten.Visualisierung.DataVisualiser import VisualisationHandler, DataVisualiser


def main(datei):
    print("Starte Pipeline")

    # Importiere Daten
    data_importer = DataImport()
    data_importer.import_data(datei)
    rows = data_importer.get_rows()

    # Prüfe Datenkontrolle
    if data_importer.status != data_importer.constants.SUCCESS:
        print("Fehler beim Importieren der Daten.")
        return

    # Führe Sentiment-Analyse durch
    sentiment_analyse = SentimentAnalyse()
    sentiment_analyse.set_rows(rows)
    sentiment_result = sentiment_analyse.get_sentiments()

    # Zeige das Ergebnis an
    print("Sentiment-Analyse Ergebnis:")
    result_dict = sentiment_result.get_result_as_dict()
    for sentiment, count in result_dict.items():
        print(f"{sentiment}: {count}")

    # Visualisiere das Ergebnis
    result_df = result_dict
    visualisation_handler = VisualisationHandler(result_df)
    vis_result = visualisation_handler.handle_all()

    # Zeige das Bar Chart an
    vis_result.bar.show()

    # Zeige das Pie Chart an
    vis_result.pie.show()

    # Zeige die Tabelle an
    print("Tabellarische Darstellung:")
    print(vis_result.table)

    # Speichere die Diagramme
    visualizer = DataVisualiser(result_dict)
    bar_chart_file, pie_chart_file = visualizer.save_visualizations("sentiment_analysis")
    print("Bar Chart wurde gespeichert unter:", bar_chart_file)
    print("Pie Chart wurde gespeichert unter:", pie_chart_file)


if __name__ == "__main__":
    nltk.download('punkt')  # Lade das 'punkt'-Ressourcenpaket herunter
    main("test.csv")
