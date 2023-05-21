import Visualization


class Export:
    def __init__(self, name: str, data: bytes):
        self.name = name
        self.data = data

    def save_file(self) -> bool:
        # Implementiere das Speichern der Datei
        try:
            with open(self.name, "wb") as file:
                file.write(self.data)
            return True
        except Exception as e:
            print(f"Fehler beim Speichern der Datei: {str(e)}")
            return False
