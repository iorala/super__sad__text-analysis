import csv
class Corpus:
    def __init__(self, filename):
        self.filename = filename


    #CSV einlesen und in einer Liste speichern
    def read_csv_file(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = []
            for row in reader:
                rows.append(row)
            return rows
