from Komponenten.UI.UI import UISentimentPipeline, TabelleAusDataframe, upload_verzeichnis_erstellen
import pandas as pd

freme = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

tabelle = TabelleAusDataframe.html(freme)

print(tabelle)