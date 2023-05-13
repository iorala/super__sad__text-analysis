# super().\__sad__(text_analysis): Ein Datenvisualisierungsprojekt

## Abhängigkeiten 


## Projektstruktur 
- README.Md: diese Datei 
- main.py: Dieses Skript startet die Webapplikation
- static/: enthält statische Elemente für die Webapplikation (z.B CSS)
- templates/: enthält die Templates für die dynamischen Seiten der Webapplikation
- Komponenten/: Enthält die Ordner der einzelnen Komponenten 
  - Komponenten/<NAME_KOMPONENTE>/: Unterordner der Komponente 
    - Komponenten/<NAME_KOMPONENTE>/<NAME_SKRIPT>.py: Datei mit einer, oder mehreren zusammengehörenden Klassen einer Komponente
    - Komponenten/<NAME_KOMPONENTE>/<NAME_SKRIPT>_test.py: Unit-tests für die Klassen der Datei. Diese sind entweder mit unittest oder pytest kompatibel 
      - https://docs.python.org/3/library/unittest.html
      - https://docs.pytest.org/en/7.3.x/contents.html
