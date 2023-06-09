import pandas as pd
import os
from Komponenten.Import.Import_and_Control import DataImport
from Komponenten.Textanalyse.Sentiment import SentimentAnalyse


class TabelleAusDataframe:
    @staticmethod
    def html(df):
        # Erstellen der Bootstrap-Tabelle
        table_html = '<table class="table table-striped">\n'

        # Spaltenüberschriften hinzufügen
        table_html += '<thead>\n<tr>'
        for column in df.columns:
            if str(column).strip() != '0':  # Prüfen, ob die Spaltenüberschrift nur eine 0 enthält
                table_html += f'<th scope="col">{column}</th>'
        table_html += '</tr>\n</thead>\n'

        # Datenzeilen hinzufügen
        table_html += '<tbody>\n'
        for _, row in df.iterrows():
            table_html += '<tr>'
            for value in row:
                table_html += f'<td>{value}</td>'
            table_html += '</tr>\n'
        table_html += '</tbody>\n'

        # Abschließende HTML-Tags hinzufügen
        table_html += '</table>'

        return table_html


class VerzeichnisErstellen:
    @staticmethod
    def erstellen(pfad):
        if os.path.isfile(pfad):
            raise FileExistsError(f'Fehler: Eine Datei mit dem Namen {pfad} existiert bereits.')
        elif not os.path.isdir(pfad):
            os.makedirs(pfad)


class UISentimentPipeline:
    def __init__(self, ordner, datei):
        data_importer = DataImport()
        data_importer.import_data(os.path.join(ordner, datei))
        rows = data_importer.get_rows()

        # Führe Sentiment-Analyse durch
        sentiment_analyse = SentimentAnalyse()
        sentiment_analyse.set_rows(rows)
        sentiment_result = sentiment_analyse.get_sentiments()
        self.result_dict = sentiment_result.get_result_as_dict()

        # Erstelle Tabelle mit Sentiment-Ergebnissen

        sentiment_dataframe = pd.DataFrame(list(zip(sentiment_analyse.rows, sentiment_analyse.sentiments)),
                                           columns=['Text', 'Sentiment']).head(n=10)

        self.sentiment_tabelle = TabelleAusDataframe.html(sentiment_dataframe)
