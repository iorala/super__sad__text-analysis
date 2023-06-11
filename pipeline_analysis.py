import nltk

from Komponenten.Import.Import_and_Control import DataImport
from Komponenten.Textanalyse.Sentiment import SentimentAnalyse
from Komponenten.Visualisierung.DataVisualiser import VisualisationHandler, DataVisualiser


# Die Hauptfunktion der Anwendung, die den Ablauf der Sentiment-Analyse-Pipeline steuert. Importiert Daten,
# führt die Sentiment-Analyse durch, visualisiert die Ergebnisse und speichert die Diagramme.
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
    visualisation_handler = VisualisationHandler(result_dict)
    visualisation_handler.handle_all()

    # Zeige das Bar Chart an
    visualisation_handler.result.bar.show()

    # Zeige das Pie Chart an
    visualisation_handler.result.pie.show()

    # Zeige die Tabelle an
    print("Tabellarische Darstellung:")
    print(visualisation_handler.result.table)

    # Speichere die Diagramme
    visualizer = DataVisualiser(result_dict)
    bar_chart_file = visualisation_handler.save_bar("sentiment_analysis")
    pie_chart_file = visualisation_handler.save_pie("sentiment_analysis")
    print("Bar Chart wurde gespeichert unter:", bar_chart_file)
    print("Pie Chart wurde gespeichert unter:", pie_chart_file)

# Lädt das 'punkt'-Ressourcenpaket aus dem NLTK-Modul herunter, das für die Tokenisierung benötigt wird.
if __name__ == "__main__":
    nltk.download('punkt')  # Lade das 'punkt'-Ressourcenpaket herunter
    main("test.csv")
