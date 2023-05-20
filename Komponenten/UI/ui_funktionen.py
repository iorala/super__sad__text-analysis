import pandas as pd

def bs_tabelle_aus_df(df):
    # Erstellen der Bootstrap-Tabelle
    table_html = '<table class="table table-striped">\n'

    # Spaltenüberschriften hinzufügen
    table_html += '<thead>\n<tr>'
    for column in df.columns:
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