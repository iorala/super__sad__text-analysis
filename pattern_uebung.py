# Visitor Patter
# Mit Import ausprobieren
from Komponenten.UI.ui_funktionen import bs_tabelle_aus_df
from Komponenten.Visitor import Visitor
from Komponenten.Import.Import_and_Control import DataImport


# Import um HTML-Output erweitern
class HTMLVisitor(Visitor):
    def __init__(self):
        self.html_tabelle = None

    def visit(self, data: DataImport):
        self.html_tabelle = bs_tabelle_aus_df(data.get_dataframe())

    def get_html_tabelle(self):
        return self.html_tabelle


if __name__ == "__main__":
    visitor = HTMLVisitor()
    data_import = DataImport()
    data_import.import_data("test.csv")
    data_import.accept(visitor)
    print(visitor.get_html_tabelle())

