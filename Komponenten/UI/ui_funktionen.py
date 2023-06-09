import pandas as pd
import os

class UISentimentPipeline:
    def __init__(self):
        self.x = ""
    def start(self):
        # Importiere Daten
        data_importer = DataImport()
        data_importer.import_data(os.path.join(app.config['UPLOAD_FOLDER'], session['dateiname_csv']))
        rows = data_importer.get_rows()

        # Führe Sentiment-Analyse durch
        sentiment_analyse = SentimentAnalyse()
        sentiment_analyse.set_rows(rows)
        sentiment_result = sentiment_analyse.get_sentiments()
        result_dict = sentiment_result.get_result_as_dict()
        session['sentiment_result_dict'] = result_dict

        sentiment_tabelle = bs_tabelle_aus_df(
            pd.DataFrame(list(zip(sentiment_analyse.rows, sentiment_analyse.sentiments)),
                         columns=['Text', 'Sentiment']).head(n=10))

        # Minimales Objekt DataVisualiser erstellen, um die möglichen Diagrammtypen zu erhalten
        diagramm_typen = DataVisualiser({0: None}).charts.keys()

def bs_tabelle_aus_df(df):
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


def upload_verzeichnis_erstellen(pfad):
    if os.path.isfile(pfad):
        print(f'Fehler: Eine Datei mit dem Namen {pfad} existiert bereits.')
    elif not os.path.isdir(pfad):
        os.makedirs(pfad)
        print(f'Verzeichnis {pfad} wurde erstellt.')
