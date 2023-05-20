from export import Exporter

class PNGExporter(Exporter):
    def __init__(self, name: str, data: bytes, quality: int):
        super().__init__(name, data)
        self.quality = quality
