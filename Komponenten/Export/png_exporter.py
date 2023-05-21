from Export import Export

class PNGExporter(Export):
    def __init__(self, name: str, data: bytes, quality: int):
        super().__init__(name, data)
        self.quality = quality
