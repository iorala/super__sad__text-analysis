import Visualization

class Export:
    def __init__(self, name: str, data: bytes):
        self.name = name
        self.data = data

    def compress_data(self) -> bytes:
        # Implementiere die Komprimierung des Datenstroms
        compressed_data = Visualization.compress(self.data)
        return compressed_data

    def save_file(self) -> bool:
       # Implementiere das Speichern der Datei
        try:
            with open(self.name, "wb") as file:
                file.write(self.data)
            return True
        except Exception as e:
            print(f"Fehler beim Speichern der Datei: {str(e)}")
            return False
